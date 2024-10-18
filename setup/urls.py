# setup/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para acessar o admin do Django
    path('', include('task_manager.urls')),  # Inclui as URLs do app task_manager na raiz do projeto
]
