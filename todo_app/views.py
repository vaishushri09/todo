from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm  # Import TaskForm
from .models import Task,CustomTask 

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
    tasks = CustomTask.objects.all()
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
        print(form.data)
        if form.is_valid():
            print("yess")
            task = form.save(commit=False)  # Create a task object without saving to the database yet
            task.user = request.user  # Assign the current user to the task (if you have user authentication)
            task.save()  # Save the task to the database
            return redirect('todo_list') 
    else:
        form = TaskForm()
        print(form.data)

    return render(request, 'todo_app/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = CustomTask.objects.get(pk=task_id)
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
    task = CustomTask.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/delete_task.html', {'task': task})
def all_user_tasks(request):
    tasks = CustomTask.objects.all()
    return render(request, 'todo_app/all_user_tasks.html', {'tasks': tasks})

from django.shortcuts import render, redirect
from .forms import CustomTaskForm

def add_custom_task(request):
    if request.method == 'POST':
        form = CustomTaskForm(request.POST)
        if form.is_valid():
            custom_task = form.save(commit=False)
            custom_task.user = request.user if request.user.is_authenticated else None  # Assign the user if authenticated
            custom_task.save()
            return redirect('todo_list')  # Redirect to the task list page after successful submission
    else:
        form = CustomTaskForm()

    return render(request, 'todo_app/add_custom_task.html', {'form': form})
