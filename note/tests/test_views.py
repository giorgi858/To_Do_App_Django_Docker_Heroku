from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from note.models import Todo
from django.urls import reverse
from django.utils import translation



class TodoViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="giorgi",
            password="giorgi12345"
        )

        self.todo = Todo.objects.create(
            title="Test todo",
            author=self.user
        )

    def test_todo_list_view_logged_in(self):
        self.client.login(
            username="giorgi",
            password="giorgi12345"
        )

        url = reverse("todo") 
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test todo")

    def test_todo_list_view_not_logged_in(self):
        url = reverse("todo")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        
        
class HomePageTests(SimpleTestCase):
    def setUp(self):
        translation.activate('en')
        url = reverse('home')
        self.response = self.client.get(url)
        
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

        
        