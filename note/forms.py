from django.forms import ModelForm
from .models import Todo
from django import forms
   # myapp/forms.py
from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper


class CustomLoginForm(LoginForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # This removes the injected "Forgot your password?" link
    #     if "password" in self.fields:
    #         self.fields["password"].help_text = None
    #         self.helper = FormHelper()
    #         self.helper.form_show_labels = False

   
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