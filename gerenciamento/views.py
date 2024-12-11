from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Artista, Musica


class ArtistaList(ListView):
    model = Artista
    template_name = 'artista_list.html'

class ArtistaCreate(CreateView):
    model = Artista
    fields = ['nome', 'data_nascimento']
    template_name = 'gerenciamento/artista_form.html'
    success_url = reverse_lazy('artista_list')

class ArtistaUpdate(UpdateView):
    model = Artista
    fields = ['nome', 'data_nascimento']
    template_name = 'gerenciamento/artista_form.html'
    success_url = reverse_lazy('artista_list')

class ArtistaDelete(DeleteView):
    model = Artista
    template_name = 'gerenciamento/artista_confirm_delete.html'
    success_url = reverse_lazy('artista_list')

class MusicaList(ListView):
    model = Musica
    template_name = 'gerenciamento/musica_list.html'

class MusicaCreate(CreateView):
    model = Musica
    fields = ['titulo', 'artista', 'lancamento']
    template_name = 'gerenciamento/musica_form.html'
    success_url = reverse_lazy('musica_list')

class MusicaUpdate(UpdateView):
    model = Musica
    fields = ['titulo', 'artista', 'lancamento']
    template_name = 'gerenciamento/musica_form.html'
    success_url = reverse_lazy('musica_list')

class MusicaDelete(DeleteView):
    model = Musica
    template_name = 'gerenciamento/musica_confirm_delete.html'
    success_url = reverse_lazy('musica_list')
