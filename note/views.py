from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import CustomerUserCreationForm
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html', {})

class SignupPageView(generic.CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    