from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('devolvido', 'Devolvido'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.username}"
