from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/<int:pk>/', views.detalhes_livro, name='detalhes_livro'),
    path('livros/novo/', views.gerenciar_livro, name='novo_livro'),
    path('livros/<int:pk>/editar/', views.gerenciar_livro, name='editar_livro'),
    path('livros/<int:pk>/excluir/', views.excluir_livro, name='excluir_livro'),
]
