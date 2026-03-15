from django.test import TestCase
from django.contrib.auth.models import User
from note.models import Todo

class TodoModelTest(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(
            username='giorgi',
            password='12345'
        )
    def test_create_todo(self):
        todo = Todo.objects.create(
            author = self.author,
            title = 'Test Title',
            description = "Test Description"
        )
        self.assertEqual(todo.title, 'Test Title')
        
        
  

