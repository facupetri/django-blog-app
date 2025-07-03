from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('acerca', acerca, name='acerca'),
    path('post_lista/', Post_lista.as_view(), name='ListarPosts'),
    path('crear_post/', PostCreateView.as_view(), name='CrearPost'),
    path('buscar_post/', SearchResultsView.as_view(), name='buscarpost'),
    path('post/<int:pk>/', Post_detail.as_view(), name='post_detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]
