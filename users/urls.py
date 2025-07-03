from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *



urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name='base/index.html'), name='logout'),
    path('edit-user/', UserEditView.as_view(), name='edit_user'),
    path('change-pass/', CambiarContrasena.as_view(), name='change_pass'),
    path('dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/edit-user/<int:pk>/', AdminUserEditView.as_view(), name='admin_edit_user'),
    path('admin/delete-user/<int:pk>/', AdminUserDeleteView.as_view(), name='admin_delete_user'),
    path('perfil/<str:username>/', UserProfileView.as_view(), name='perfil_usuario'),
]
