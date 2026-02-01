from django.forms import ModelForm
from .models import Todo
from django import forms
   # myapp/forms.py
from allauth.account.forms import LoginForm

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # This removes the injected "Forgot your password?" link
        if "password" in self.fields:
            self.fields["password"].help_text = None
   
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('task', 'describtion')
        labels = {
        'task': '',
        'describtion': '',
    }
        widgets = {
        'task': forms.TextInput(attrs={
            'class': 'todo-input',
            'placeholder': 'Enter task name...'
        }),
        'describtion': forms.Textarea(attrs={
            'class': 'todo-textarea',
            'rows': 3,
            'placeholder': 'Enter description name...',
        }),
        }    