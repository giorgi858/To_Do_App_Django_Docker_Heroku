from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import TodoForm, UsernameChangeForm
from .models import Todo
from celery import shared_task
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q

class SearchResultListView(ListView):
    model = Todo
    context_object_name = "searched_todo"
    template_name = 'search_result.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if 'q' in self.request.GET and not self.request.GET.get('q').strip():
            return redirect(self.request.path)
        return Todo.objects.filter(
            Q(title__icontains=query)
        )



@shared_task
def test_task():
    print("Celery works!")


# -----------------------------
# Home & About Pages
# -----------------------------
def home(request):
    return render(request, "home.html")


def aboutView(request):
    return render(request, "About.html")


# -----------------------------
# Username Change
# -----------------------------
@login_required
def change_username(request):
    """
    Allow logged-in users to change their username.
    """
    form = UsernameChangeForm(request.POST or None, instance=request.user)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Username updated successfully.")
        return redirect("home")  # or another page if needed

    return render(request, "account/username_change.html", {"form": form})


# -----------------------------
# Todo Views
# -----------------------------
@login_required
def todolistView(request):
    """
    Display all todos for the current user and handle new todo creation.
    """
    todos = Todo.objects.filter(author=request.user)
    form = TodoForm(request.POST or None)
   


    if request.method == "POST" and form.is_valid():
        todo = form.save(commit=False)
        todo.author = request.user
        todo.save()
        return redirect("todo")  # refresh page
    
    paginator = Paginator(todos, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "todos": todos,
        "form": form,
        'page_obj': page_obj
    }
    return render(request, "todo.html", context)


@login_required
def note_update_view(request, pk):
    """
    Edit a todo task.
    """
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo")

    return render(request, "task_edit.html", {"form": form})


@login_required
def note_delete_view(request, pk):
    """
    Delete a todo task with confirmation.
    """
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.delete()
        messages.success(request, f"Task '{todo.title}' deleted successfully.")
        return redirect("todo")

    return render(request, "delete_task.html", {"object": todo})


@login_required
def myform(request):
    """
    Display all tasks (read-only overview).
    """
    todos = Todo.objects.filter(author=request.user)
    return render(request, "form.html", {"todos": todos})
