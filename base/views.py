from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from base.models import *

class IndexView(ListView):
    model = Post
    template_name = 'base/index.html'
    context_object_name = 'Post'
    ordering = ['-fecha_creacion']
    paginate_by = 6 


def acerca(request):
    return render(request, 'base/acerca.html')


class Post_lista(ListView):
    model = Post
    context_object_name = 'Post'
    template_name = 'base/listarpost.html'
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.all().order_by('-fecha_creacion')


class Post_detail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'base/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'posteo', 'imagen']
    template_name = 'base/crear_post.html'
    success_url = reverse_lazy('ListarPosts')
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class SearchResultsView(LoginRequiredMixin, ListView):
    model = Post
    template_name= 'base/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(autor__icontains=query)


class PostEditView(UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'posteo', 'imagen']
    template_name = 'base/edit_post.html'
    success_url = reverse_lazy('ListarPosts')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autor=self.request.user)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'base/delete_post.html'
    success_url = reverse_lazy('ListarPosts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor or self.request.user.is_staff

