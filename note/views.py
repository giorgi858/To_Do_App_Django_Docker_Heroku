from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import CustomerUserCreationForm, TodoForm
from django.urls import reverse_lazy
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            task = form.cleaned_data['task']
            describtion = form.cleaned_data['describtion']
            print('task', task)
            print('describtion', describtion)
            form = TodoForm()
        return redirect('home')

    context = {
        "todos": todos,
         "form": form 
    }
    return render(request,"home.html", context)


def note_update_view(request, pk):
    obj = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=obj)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save() 
        return redirect('home')
    return render(request, 'task_edit.html', { 'form': form })

def note_delete_view(request, pk):
    obj = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {
        'object': obj
    }
    return render(request, 'delete_task.html', context)




class SignupPageView(generic.CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
     
def myform(request):
    Todos = Todo.objects.all()
    context = {
        'todos': Todos
    }
    return render(request, 'form.html', context)