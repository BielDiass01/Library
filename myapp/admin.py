from django.contrib import admin
from .models import Livro, Emprestimo, Autor

admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Autor)
