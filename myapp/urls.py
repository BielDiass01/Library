from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    
    # URLs para gerenciamento de autores
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/cadastrar/', views.cadastrar_autor, name='cadastrar_autor'),
    path('autores/<int:pk>/', views.visualizar_autor, name='visualizar_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/excluir/<int:pk>/', views.excluir_autor, name='excluir_autor'),
    
    # URLs para gerenciamento de livros
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('livros/<int:pk>/', views.visualizar_livro, name='visualizar_livro'),
    path('livros/editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('livros/excluir/<int:pk>/', views.excluir_livro, name='excluir_livro'),
    
    # URLs para gerenciamento de usuários
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/<int:pk>/', views.visualizar_usuario, name='visualizar_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),
    
    # URLs para gerenciamento de empréstimos
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
    path('emprestimos/cadastrar/', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),
    path('emprestimos/<int:pk>/', views.visualizar_emprestimo, name='visualizar_emprestimo'),
    path('emprestimos/devolucao/<int:pk>/', views.registrar_devolucao, name='registrar_devolucao'),
    path('emprestimos/cancelar/<int:pk>/', views.cancelar_emprestimo, name='cancelar_emprestimo'),
]