from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('excluir/<int:pk>/', views.excluir_livro, name='excluir_livro'),
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
]
