from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_text = {k: '' for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    username = forms.CharField(label='Nuevo nombre de usuario', required=False)
    email = forms.EmailField(label='Ingrese su nuevo email')
    last_name = forms.CharField(label='Apellido', required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    imagen = forms.ImageField(label='Avatar', required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'username', 'imagen']


class AdminUserEditForm(forms.ModelForm):
    is_staff = forms.BooleanField(label='Permisos de administrador', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff',]

    def __init__(self, *args, **kwargs):
        super(AdminUserEditForm, self).__init__(*args, **kwargs)

        if self.instance.is_superuser:
            self.fields.pop('is_staff')
