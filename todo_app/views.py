from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Task

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('todo_list')  # Replace 'todo_list' with the name of your todo list view
    else:
        form = AuthenticationForm()
    return render(request, 'todo_app/login.html', {'form': form})


from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional logic for user registration
            return redirect('success_page')  # Redirect to a success page
    else:
        form = UserRegistrationForm()
    return render(request, 'todo_app/register.html', {'form': form})

def test_view(request):
    return render(request,'todo_app/add_task.html')

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_app/todo_list.html', {'tasks': tasks})
# def add_task(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         Task.objects.create(title=title, description=description)
#         return redirect('todo_list')
#     return render(request, 'todo_app/add_task.html')
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do other actions
    else:
        form = TaskForm()

    return render(request, 'todo_app/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed')
        task.title = title
        task.description = description
        task.completed = bool(completed)
        task.save()
        return redirect('todo_list')
    return render(request, 'todo_app/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/delete_task.html', {'task': task})
def all_user_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'todo_app/all_user_tasks.html', {'tasks': tasks})