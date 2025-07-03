from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from users.models import Avatar
from users.forms import UserRegisterForm, UserEditForm, AdminUserEditForm
from django.urls import reverse_lazy
from base.models import Post
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, FormView

class UserLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        contrasena = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=contrasena)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Usuario o contraseña incorrecta!')
            return self.form_invalid(form)

    def form_invalid(self, form):
        if form.errors.get('__all__'):
            messages.error(self.request, 'Usuario o contraseña incorrecta!')
        else:
            messages.error(self.request, 'Formulario inválido!')
        return super().form_invalid(form)


class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Usuario creado con éxito!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores.')
        return super().form_invalid(form)


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/edit_user.html'
    success_url = reverse_lazy('user_dashboard')

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(UserEditView, self).get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields.pop('is_staff', None) 
        return form

    def form_valid(self, form):
        response = super(UserEditView, self).form_valid(form)
        avatar = form.cleaned_data.get('imagen')
        if avatar:
            avatar_instance, created = Avatar.objects.get_or_create(user=self.request.user)
            avatar_instance.imagen = avatar
            avatar_instance.save()
        return response


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(autor=self.request.user).order_by('-fecha_creacion')
        if self.request.user.is_superuser:
            context['usuarios'] = User.objects.all().exclude(username=self.request.user.username)
        return context


class CambiarContrasena(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/change_pass.html'
    success_url = reverse_lazy('user_dashboard')

    def form_valid(self, form):
        messages.success(self.request, '¡Tu contraseña ha sido cambiada exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al cambiar tu contraseña. Por favor, intenta nuevamente.')
        return super().form_invalid(form)


class UserProfileView(LoginRequiredMixin, View):

    def get(self, request, username):
        user = get_object_or_404(User, username=username)

        if user == request.user:
            return redirect('user_dashboard')
        else:
            avatar = Avatar.objects.filter(user=user).first()
            context = {
                'user_profile': user,
                'avatar': avatar,
            }
            return render(request, 'users/profile.html', context)
        

class AdminDashboardView(TemplateView):
    template_name = 'users/admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_usuarios'] = User.objects.count()
        context['total_posteos'] = Post.objects.count()
        context['usuarios_recientes'] = User.objects.order_by('-date_joined')[:5]
        context['posts_recientes'] = Post.objects.order_by('-fecha_creacion')[:5]
        return context


class AdminUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/admin_confirm_delete.html'
    success_url = reverse_lazy('user_dashboard')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_success_url(self):
        if self.request.user.pk == self.object.pk:
            return reverse_lazy('logout')
        return super().get_success_url()


class AdminUserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = AdminUserEditForm
    template_name = 'users/admin_edit_user.html'
    success_url = reverse_lazy('user_dashboard')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class AdminPostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'posteo', 'imagen']
    template_name = 'base/edit_post.html'
    success_url = reverse_lazy('admin_dashboard')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class AdminPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'base/delete_post.html'
    success_url = reverse_lazy('admin_dashboard')  

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser