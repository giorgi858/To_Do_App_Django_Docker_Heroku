from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model

from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper

from .models import Todo

User = get_user_model()


# -----------------------------
# Username Change Form
# -----------------------------
class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This username is already taken.")
        return username


# -----------------------------
# Custom Login Form
# -----------------------------
class CustomLoginForm(LoginForm):
    """
    Optional: Customize login form
    Example: hide labels, remove "Forgot password?"
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False  # show only placeholders
        # Remove help text on password field if needed
        if "password" in self.fields:
            self.fields["password"].help_text = None


# -----------------------------
# Todo Form
# -----------------------------
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('task', 'describtion')
        labels = {
            'task': '',
            'describtion': '',
        }
        widgets = {
            'task': forms.TextInput(
                attrs={
                    'class': 'todo-input form-control',
                    'placeholder': 'Enter task name...',
                }
            ),
            'describtion': forms.Textarea(
                attrs={
                    'class': 'todo-textarea form-control',
                    'rows': 3,
                    'placeholder': 'Enter task description...',
                }
            ),
        }
