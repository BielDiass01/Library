# Generated by Django 5.2.1 on 2025-05-16 18:54

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import myapp.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('biografia', models.TextField(blank=True, help_text='Uma breve biografia do autor', null=True, verbose_name='Biografia')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('nacionalidade', models.CharField(blank=True, default='Brasileira', max_length=100, null=True, verbose_name='Nacionalidade')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='autores/', verbose_name='Foto do autor')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['nome'],
                'indexes': [models.Index(fields=['nome'], name='myapp_autor_nome_1f6497_idx')],
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('isbn', models.CharField(help_text='Formato: 978-85-7522-xxx-x', max_length=20, unique=True, verbose_name='ISBN')),
                ('editora', models.CharField(blank=True, max_length=200, null=True, verbose_name='Editora')),
                ('ano_publicacao', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2025)], verbose_name='Ano de publicação')),
                ('quantidade_disponivel', models.PositiveIntegerField(default=1, verbose_name='Quantidade disponível')),
                ('sinopse', models.TextField(blank=True, null=True, verbose_name='Sinopse')),
                ('genero', models.CharField(choices=[('ROM', 'Romance'), ('FIC', 'Ficção'), ('INF', 'Infantil'), ('TEC', 'Técnico'), ('OUT', 'Outros')], default='OUT', max_length=3, verbose_name='Gênero')),
                ('paginas', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de páginas')),
                ('capa', models.ImageField(blank=True, null=True, upload_to='capas/', verbose_name='Capa do livro')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('autores', models.ManyToManyField(related_name='livros', to='myapp.autor', verbose_name='Autores')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data do empréstimo')),
                ('data_devolucao_prevista', models.DateTimeField(default=myapp.models.calcular_data_devolucao, verbose_name='Data prevista para devolução')),
                ('data_devolucao_efetiva', models.DateTimeField(blank=True, null=True, verbose_name='Data efetiva de devolução')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('status', models.CharField(choices=[('emprestado', 'Emprestado'), ('devolvido', 'Devolvido'), ('atrasado', 'Atrasado'), ('renovado', 'Renovado')], default='emprestado', max_length=10, verbose_name='Status')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos', to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos', to='myapp.livro')),
            ],
            options={
                'verbose_name': 'Empréstimo',
                'verbose_name_plural': 'Empréstimos',
                'ordering': ['-data_emprestimo'],
            },
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('endereco', models.TextField(blank=True, null=True, verbose_name='Endereço completo')),
                ('tipo_usuario', models.CharField(choices=[('AL', 'Aluno'), ('PROF', 'Professor'), ('FUNC', 'Funcionário'), ('BIB', 'Bibliotecário')], default='AL', max_length=4, verbose_name='Tipo de usuário')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios/', verbose_name='Foto do usuário')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de Usuário',
                'verbose_name_plural': 'Perfis de Usuários',
                'ordering': ['usuario__username'],
            },
        ),
        migrations.AddIndex(
            model_name='livro',
            index=models.Index(fields=['titulo'], name='myapp_livro_titulo_2879fa_idx'),
        ),
        migrations.AddIndex(
            model_name='livro',
            index=models.Index(fields=['ano_publicacao'], name='myapp_livro_ano_pub_c7933a_idx'),
        ),
        migrations.AddIndex(
            model_name='emprestimo',
            index=models.Index(fields=['status'], name='myapp_empre_status_0645ae_idx'),
        ),
        migrations.AddIndex(
            model_name='emprestimo',
            index=models.Index(fields=['data_devolucao_prevista'], name='myapp_empre_data_de_d3e4ee_idx'),
        ),
    ]
