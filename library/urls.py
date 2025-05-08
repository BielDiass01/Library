from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('django.contrib.auth.urls')),  # Inclui login/logout padrão
    path('', include('myapp.urls')),  # Rotas da aplicação principal
]
