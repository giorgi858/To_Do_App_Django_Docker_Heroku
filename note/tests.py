from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomerUserTests(TestCase):
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username = "giorgi",email = "", password = 'giorgi12345')
        self.assertEqual(admin_user.username, "giorgi")
        self.assertEqual(admin_user.email, "")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
