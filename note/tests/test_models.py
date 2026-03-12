from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from note.models import Todo
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import translation


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
        
        

class CustomerUserTests(TestCase):
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username = "giorgi232",email = "new23@gmail.com")        
        self.assertEqual(admin_user.username, "giorgi232")
        self.assertEqual(admin_user.email, "new23@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
            
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="giorgi232",
            email="new23@gmail.com",
            password="testpass123"
        )

        self.assertEqual(user.username, "giorgi232")
        self.assertEqual(user.email, "new23@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_user_with_hashed_password(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="giorgi232",
            email="new23@gmail.com",
            password="testpass123"
        )

        # password should NOT be stored as plain text
        self.assertNotEqual(user.password, "testpass123")

        # password should be correctly hashed and verified
        self.assertTrue(user.check_password("testpass123"))

        
class HomePageTests(SimpleTestCase):
    def setUp(self):
        translation.activate('en')
        url = reverse('home')
        self.response = self.client.get(url)
        
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

        
        
