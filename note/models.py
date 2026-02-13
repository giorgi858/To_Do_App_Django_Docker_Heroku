from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    task = models.CharField(max_length=150)
    describtion = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', default=1)
    created = models.DateTimeField(auto_now_add=True)  # when note is created
    updated = models.DateTimeField(auto_now=True)      # when note is edited
    
    def __str__(self):
        return f' Task : {self.task[0:20]} and author {self.author}'


