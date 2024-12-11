from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('artista_list')),  
    path('artistas/', include('gerenciamento.urls')),
    path('musicas/', include('gerenciamento.urls')),
]
