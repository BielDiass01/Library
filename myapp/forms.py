from django import forms
from .models import Autor, Livro, PerfilUsuario, Emprestimo

class AutorForm(forms.ModelForm):
    class Meta:  # <- Esta linha deve estar indentada dentro de AutorForm
        model = Autor
        fields = ['nome', 'biografia', 'data_nascimento', 'nacionalidade']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'nome': 'Nome completo',
            'data_nascimento': 'Data de nascimento',
        }

class LivroForm(forms.ModelForm):
    class Meta:  # <- Mesma indentação para todas as classes de formulário
        model = Livro
        fields = ['titulo', 'autores', 'isbn', 'editora', 'ano_publicacao', 
                 'quantidade_disponivel', 'sinopse', 'genero', 'paginas']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['telefone', 'endereco']
        widgets = {
            'endereco': forms.Textarea(attrs={'rows': 3}),
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'usuario', 'data_devolucao_prevista', 'observacoes']
        widgets = {
            'data_devolucao_prevista': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }