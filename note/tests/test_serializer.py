from django.test import TestCase
from django.contrib.auth.models import User

from note.models import Todo
from api.serializer import TodoSerializer, UserSerializer


class TodoSerializerTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
    )

        self.todo = Todo.objects.create(
            title="test todo",
            author=self.user
        )

# -----------------------
# VALID SERIALIZER
# -----------------------
    def test_todo_serializer_valid(self):

        data = {
            "title": "new todo"
        }
        serializer = TodoSerializer(data=data)
        self.assertTrue(serializer.is_valid())


# -----------------------
# INVALID SERIALIZER
# -----------------------
    def test_todo_serializer_invalid(self):

      data = {
            "title": ""
        }
      serializer = TodoSerializer(data=data)
      self.assertFalse(serializer.is_valid())
    
# -----------------------
# SERIALIZER DATA
# -----------------------
    def test_todo_serializer_data(self):

        serializer = TodoSerializer(instance=self.todo)

        self.assertEqual(
            serializer.data["title"],
            "test todo"
        )


# -----------------------
# CREATE TODO
# -----------------------

    def test_todo_serializer_create(self):

        data = {
            "title": "created todo"
        }

        serializer = TodoSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        todo = serializer.save(author=self.user)
        self.assertEqual(todo.title, "created todo")
        self.assertEqual(todo.author, self.user)


class UserSerializerTest(TestCase):

    # -----------------------
    # CREATE USER
    # -----------------------
    def test_user_serializer(self):

        data = {
            "username": "newuser",
            "password": "12345"
        }

        serializer = UserSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        user = serializer.save()

        self.assertEqual(user.username, "newuser")