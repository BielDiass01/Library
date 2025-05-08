from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Livro, Emprestimo
from .forms import LivroForm

# Listar livros
@login_required
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros_list.html', {'livros': livros})

# Cadastrar um livro
@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livro_form.html', {'form': form})

# Excluir um livro
@login_required
def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'confirm_delete.html', {'objeto': livro})

# Listar empréstimos
@login_required
def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos_list.html', {'emprestimos': emprestimos})
