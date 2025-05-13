from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Autor(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome completo",
        help_text="Digite o nome completo do autor"
    )
    biografia = models.TextField(
        blank=True,
        null=True,
        verbose_name="Biografia",
        help_text="Uma breve biografia do autor"
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de nascimento"
    )
    nacionalidade = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="Brasileira",
        verbose_name="Nacionalidade"
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )
    foto = models.ImageField(
        upload_to='autores/',
        null=True,
        blank=True,
        verbose_name="Foto do autor"
    )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome']),
        ]

class Livro(models.Model):
    GENERO_CHOICES = [
        ('ROM', 'Romance'),
        ('FIC', 'Ficção'),
        ('INF', 'Infantil'),
        ('TEC', 'Técnico'),
        ('OUT', 'Outros'),
    ]
    
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título"
    )
    autores = models.ManyToManyField(
        Autor,
        related_name='livros',
        verbose_name="Autores"
    )
    isbn = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="ISBN",
        help_text="Formato: 978-85-7522-xxx-x"
    )
    editora = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Editora"
    )
    ano_publicacao = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(timezone.now().year)
        ],
        verbose_name="Ano de publicação"
    )
    quantidade_disponivel = models.PositiveIntegerField(
        default=1,
        verbose_name="Quantidade disponível"
    )
    sinopse = models.TextField(
        blank=True,
        null=True,
        verbose_name="Sinopse"
    )
    genero = models.CharField(
        max_length=3,
        choices=GENERO_CHOICES,
        default='OUT',
        verbose_name="Gênero"
    )
    paginas = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Número de páginas"
    )
    capa = models.ImageField(
        upload_to='capas/',
        null=True,
        blank=True,
        verbose_name="Capa do livro"
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )

    def __str__(self):
        return self.titulo
    
    @property
    def disponivel(self):
        return self.quantidade_disponivel > 0
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ['titulo']
        indexes = [
            models.Index(fields=['titulo']),
            models.Index(fields=['ano_publicacao']),
        ]

class PerfilUsuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('AL', 'Aluno'),
        ('PROF', 'Professor'),
        ('FUNC', 'Funcionário'),
        ('BIB', 'Bibliotecário'),
    ]
    
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Telefone"
    )
    endereco = models.TextField(
        blank=True,
        null=True,
        verbose_name="Endereço completo"
    )
    tipo_usuario = models.CharField(
        max_length=4,
        choices=TIPO_USUARIO_CHOICES,
        default='AL',
        verbose_name="Tipo de usuário"
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de nascimento"
    )
    foto = models.ImageField(
        upload_to='usuarios/',
        null=True,
        blank=True,
        verbose_name="Foto do usuário"
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )
    
    def __str__(self):
        return f"{self.usuario.get_full_name() or self.usuario.username}"
    
    class Meta:
        verbose_name = "Perfil de Usuário"
        verbose_name_plural = "Perfis de Usuários"
        ordering = ['usuario__username']

class Emprestimo(models.Model):
    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='emprestimos'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='emprestimos'
    )
    data_emprestimo = models.DateTimeField(
        default=timezone.now,
        verbose_name="Data do empréstimo"
    )
    data_devolucao_prevista = models.DateTimeField(
        verbose_name="Data prevista para devolução"
    )
    data_devolucao_efetiva = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Data efetiva de devolução"
    )
    observacoes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observações"
    )
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('devolvido', 'Devolvido'),
        ('atrasado', 'Atrasado'),
        ('renovado', 'Renovado'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='emprestado',
        verbose_name="Status"
    )

    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.username} (Status: {self.get_status_display()})"
    
    def save(self, *args, **kwargs):
        # Se for um novo empréstimo
        if not self.pk:
            # Define a data de devolução prevista padrão (15 dias após o empréstimo)
            if not hasattr(self, 'data_devolucao_prevista') or not self.data_devolucao_prevista:
                self.data_devolucao_prevista = self.data_emprestimo + timezone.timedelta(days=15)
            
            # Atualiza o estoque do livro
            if self.livro.quantidade_disponivel > 0:
                self.livro.quantidade_disponivel -= 1
                self.livro.save()
            else:
                raise ValueError("Não há exemplares disponíveis deste livro")
        
        # Atualiza status para atrasado se passou da data
        if self.status != 'devolvido' and timezone.now() > self.data_devolucao_prevista:
            self.status = 'atrasado'
        
        super().save(*args, **kwargs)
    
    @property
    def dias_atraso(self):
        if self.status == 'atrasado' and not self.data_devolucao_efetiva:
            return (timezone.now() - self.data_devolucao_prevista).days
        return 0
    
    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ['-data_emprestimo']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['data_devolucao_prevista']),
        ]