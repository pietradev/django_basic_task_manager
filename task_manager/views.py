from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

#Listar Tarefas
def task_list(request):
    ##Criando um objeto task que recebe info da DB (todas as tarefas)
    task = Task.objects.all()

    #Vamos renderizar o template html que lista as tasks e passar task como um objeto
    return render(request, 'task_manager/task_list.html', {'tasks':task})

#Criar nova tarefa
def task_create(request):
    if request.method == 'POST':
        #Criamos um objeto formulario
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('task_list') #Depois de enviar a info p o banco, retornamos para o template que lista as tasks
    #Se não houver um POST request, iremos renderizar o form em branco
    else:
        form = TaskForm()
    return render(request, 'task_manager/task_form.html', {'form': form})

#Editar uma Tarefa
def task_edit(request, id):
    #Usando get_object_or_404 para buscar objeto no DB (passamos o modelo definido em models.py e o filtro que usamos para procurar o objeto)
    task = get_object_or_404(Task, id=id)

    #Ao preenchermos a info, e apertarmos em submit, geramos um POST request
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        #Cria formulario com as info preenchidas
        form = TaskForm(instance = task)
    return render(request, 'task_manager/task_form.html', {'form': form})

#Excluir uma tarefa
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return render(request, 'task_manager/task_confirm_delete.html', {'task':task})