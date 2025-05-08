from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Emprestimo, Autor
from .forms import LivroForm, EmprestimoForm

# Listar todos os livros
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'myapp/livros_list.html', {'livros': livros})

# Detalhes de um livro
def detalhes_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'myapp/livros_detail.html', {'livro': livro})

# Adicionar ou editar um livro
def gerenciar_livro(request, pk=None):
    if pk:
        livro = get_object_or_404(Livro, pk=pk)
    else:
        livro = None
    
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    
    return render(request, 'myapp/livro_form.html', {'form': form})

# Excluir um livro
def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'myapp/confirm_delete.html', {'objeto': livro})
# Listar todos os empréstimos
def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'myapp/emprestimos_list.html', {'emprestimos': emprestimos})

# Detalhes de um empréstimo
def detalhes_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    return render(request, 'myapp/emprestimos_detail.html', {'emprestimo': emprestimo})

# Criar um novo empréstimo
def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'myapp/emprestimo_form.html', {'form': form})

# Encerrar um empréstimo
def encerrar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        emprestimo.status = 'devolvido'
        emprestimo.save()
        return redirect('listar_emprestimos')
    return render(request, 'myapp/confirm_devolucao.html', {'objeto': emprestimo})
