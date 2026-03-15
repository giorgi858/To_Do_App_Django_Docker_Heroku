from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.utils import translation

class TodoAPITest(APITestCase):
    def setUp(self):
        self.author = User.objects.create_user(
        username='giorgi',
        password='giorgi12345'
        )
        refresh = RefreshToken.for_user(self.author)

        self.client.credentials(
            HTTP_AUTHORIZATION= f'Bearer {refresh.access_token}'
        )
    def test_get_todos(self):
        translation.activate('en')
        url = reverse('api_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)