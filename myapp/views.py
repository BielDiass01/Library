from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Livro, Emprestimo, Autor, PerfilUsuario
from .forms import LivroForm, AutorForm, EmprestimoForm, UsuarioForm



def pagina_inicial(request):
    return render(request, 'myapp/templates/pagina_inicial.html')

@login_required
def cadastrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)  # Você precisará criar AutorForm
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'myapp/autores/formulario.html', {'form': form})

@login_required
def visualizar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'myapp/autores/detalhes.html', {'autor': autor})

@login_required
def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('visualizar_autor', pk=autor.pk)
    else:
        form = AutorForm(instance=autor)
    return render(request, 'myapp/autores/formulario.html', {'form': form})

@login_required
def excluir_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'myapp/autores/confirmar_exclusao.html', {'autor': autor})

@login_required
def visualizar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livro_detail.html', {'livro': livro})

@login_required
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('visualizar_livro', pk=livro.pk)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro_form.html', {'form': form})

@login_required
def listar_usuarios(request):
    usuarios = PerfilUsuario.objects.all()
    return render(request, 'usuarios_list.html', {'usuarios': usuarios})

@login_required
def cadastrar_usuario(request):
    # Implementação similar às outras funções de cadastro
    pass

@login_required
def visualizar_usuario(request, pk):
    usuario = get_object_or_404(PerfilUsuario, pk=pk)
    return render(request, 'usuario_detail.html', {'usuario': usuario})

@login_required
def editar_usuario(request, pk):
    # Implementação similar às outras funções de edição
    pass

@login_required
def excluir_usuario(request, pk):
    # Implementação similar às outras funções de exclusão
    pass

@login_required
def cadastrar_emprestimo(request):
    # Implementação para criar novo empréstimo
    pass

@login_required
def visualizar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    return render(request, 'emprestimo_detail.html', {'emprestimo': emprestimo})

@login_required
def registrar_devolucao(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        emprestimo.data_devolucao_efetiva = timezone.now()
        emprestimo.status = 'devolvido'
        emprestimo.save()
        return redirect('visualizar_emprestimo', pk=emprestimo.pk)
    return render(request, 'registrar_devolucao.html', {'emprestimo': emprestimo})

@login_required
def cancelar_emprestimo(request, pk):
    # Implementação para cancelar empréstimo
    pass