from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import CustomerUserCreationForm, TodoForm
from django.urls import reverse_lazy
from .models import Todo
from django.contrib.auth.decorators import login_required

def aboutView(request):
    return render(request, 'About.html', {})

@login_required
def todolistView(request):
    todos = Todo.objects.filter(author=request.user)
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            # Commit False prevents saving to the database immediately
            post = form.save(commit=False)
            print(request.user)
            # Assign the current logged-in user to the note
            post.author  = request.user
            # Now save the instance to the database
            post.save()
            return redirect('todo') # Redirect to the note list page
        else:
            form = TodoForm()
    context = {
        "todos": todos,
         "form": form 
    }
    return render(request,"todo.html", context)


def home(request):
    return render(request,"home.html", {})

@login_required
def note_update_view(request, pk):
    obj = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=obj)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save() 
        return redirect('todo')
    return render(request, 'task_edit.html', { 'form': form })

@login_required
def note_delete_view(request, pk):
    obj = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('todo')
    context = {
        'object': obj
    }
    return render(request, 'delete_task.html', context)





def myform(request):
    Todos = Todo.objects.filter(author=request.user)
    context = {
        'todos': Todos
    }
    return render(request, 'form.html', context)