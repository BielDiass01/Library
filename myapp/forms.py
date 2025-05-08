from django import forms
from .models import Livro, Emprestimo

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'ano', 'genero', 'quantidade', 'autores']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro', 'data_devolucao', 'status']
