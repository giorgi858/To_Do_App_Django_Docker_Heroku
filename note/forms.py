from django.forms import ModelForm
from .models import Todo
from django import forms
   # myapp/forms.py
from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model

User = get_user_model()

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

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