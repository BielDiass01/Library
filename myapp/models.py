from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField(blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Autores"
        ordering = ['nome']

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor, related_name='livros')
    isbn = models.CharField(max_length=20, unique=True)
    editora = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    quantidade_disponivel = models.IntegerField(default=1)
    sinopse = models.TextField(blank=True)
    genero = models.CharField(max_length=100, blank=True)
    paginas = models.IntegerField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['titulo']

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField(blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.usuario.username

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao_prevista = models.DateTimeField()
    data_devolucao_efetiva = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(blank=True)
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('devolvido', 'Devolvido'),
        ('atrasado', 'Atrasado'),
        ('renovado', 'Renovado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='emprestado')

    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.username}"
    
    class Meta:
        verbose_name_plural = "Empréstimos"
        ordering = ['-data_emprestimo']