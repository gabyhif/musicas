from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='musicas')
    lancamento = models.DateField()

    def __str__(self):
        return self.titulo
