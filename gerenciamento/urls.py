from django.urls import path
from . import views

urlpatterns = [
    path('artistas/', views.ArtistaList.as_view(), name='artista_list'),
    path('artistas/novo/', views.ArtistaCreate.as_view(), name='artista_create'),
    path('artistas/<int:pk>/editar/', views.ArtistaUpdate.as_view(), name='artista_update'),
    path('artistas/<int:pk>/deletar/', views.ArtistaDelete.as_view(), name='artista_delete'),
    path('musicas/', views.MusicaList.as_view(), name='musica_list'),
    path('musicas/nova/', views.MusicaCreate.as_view(), name='musica_create'),
    path('musicas/<int:pk>/editar/', views.MusicaUpdate.as_view(), name='musica_update'),
    path('musicas/<int:pk>/deletar/', views.MusicaDelete.as_view(), name='musica_delete'),
]
