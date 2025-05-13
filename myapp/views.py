from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Livro, Emprestimo, Autor, PerfilUsuario
from .forms import LivroForm, AutorForm, EmprestimoForm, UsuarioForm

def pagina_inicial(request):

    context = {
        'total_livros': Livro.objects.count(),
        'total_autores': Autor.objects.count(),
        'total_emprestimos': Emprestimo.objects.filter(status='emprestado').count(),
        'ultimos_livros': Livro.objects.order_by('-data_cadastro')[:5]
    }
    return render(request, 'myapp/pagina_inicial.html', context)

@login_required
def listar_livros(request):
    livros = Livro.objects.all().order_by('titulo')
    return render(request, 'myapp/livros/lista.html', {'livros': livros})

@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'myapp/livros/formulario.html', {'form': form})

@login_required
def visualizar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'myapp/livros/detalhes.html', {'livro': livro})

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
    return render(request, 'myapp/livros/formulario.html', {'form': form})

@login_required
def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'myapp/livros/confirmar_exclusao.html', {'livro': livro})

@login_required
def listar_autores(request):
    autores = Autor.objects.all().order_by('nome')
    return render(request, 'myapp/autores/lista.html', {'autores': autores})

@login_required
def cadastrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)  
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
def listar_usuarios(request):
    usuarios = PerfilUsuario.objects.all()
    return render(request, 'myapp/usuarios/lista.html', {'usuarios': usuarios})

@login_required
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'myapp/usuarios/formulario.html', {'form': form})

@login_required
def visualizar_usuario(request, pk):
    usuario = get_object_or_404(PerfilUsuario, pk=pk)
    return render(request, 'myapp/usuarios/detalhes.html', {'usuario': usuario})

@login_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(PerfilUsuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('visualizar_usuario', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'myapp/usuarios/formulario.html', {'form': form})

@login_required
def excluir_usuario(request, pk):
    usuario = get_object_or_404(PerfilUsuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'myapp/usuarios/confirmar_exclusao.html', {'usuario': usuario})

@login_required
def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all().order_by('-data_emprestimo')
    return render(request, 'myapp/emprestimos/lista.html', {'emprestimos': emprestimos})

@login_required
def cadastrar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save()
            # Atualiza a quantidade disponível do livro
            livro = emprestimo.livro
            livro.quantidade_disponivel -= 1
            livro.save()
            return redirect('visualizar_emprestimo', pk=emprestimo.pk)
    else:
        form = EmprestimoForm()
    return render(request, 'myapp/emprestimos/formulario.html', {'form': form})

@login_required
def visualizar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    return render(request, 'myapp/emprestimos/detalhes.html', {'emprestimo': emprestimo})

@login_required
def registrar_devolucao(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        emprestimo.data_devolucao_efetiva = timezone.now()
        emprestimo.status = 'devolvido'
        emprestimo.save()
        # Atualiza a quantidade disponível do livro
        livro = emprestimo.livro
        livro.quantidade_disponivel += 1
        livro.save()
        return redirect('visualizar_emprestimo', pk=emprestimo.pk)
    return render(request, 'myapp/emprestimos/registrar_devolucao.html', {'emprestimo': emprestimo})

@login_required
def cancelar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        # Atualiza a quantidade disponível do livro antes de cancelar
        livro = emprestimo.livro
        livro.quantidade_disponivel += 1
        livro.save()
        emprestimo.delete()
        return redirect('listar_emprestimos')
    return render(request, 'myapp/emprestimos/confirmar_cancelamento.html', {'emprestimo': emprestimo})