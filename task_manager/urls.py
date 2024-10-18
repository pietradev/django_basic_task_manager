# task_manager/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL para listar todas as tarefas
    path('task/new/', views.task_create, name='task_create'),  # URL para criar uma nova tarefa
    path('task/edit/<int:id>/', views.task_edit, name='task_edit'),  # URL para editar uma tarefa existente
    path('task/delete/<int:id>/', views.task_delete, name='task_delete'),  # URL para excluir uma tarefa
]
