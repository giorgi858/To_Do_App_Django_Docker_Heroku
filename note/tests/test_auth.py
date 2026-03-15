from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from note.models import Todo

class AuthTest(APITestCase):
    def setUp(self):
        
        self.user1 = User.objects.create_user(
            username="user1",
            password="12345"
        )

        self.user2 = User.objects.create_user(
            username="user2",
            password="12345"
        )

        self.todo = Todo.objects.create(
            author=self.user1,
            title="test"
        )
    def test_user_cannot_edit_other_user_todo(self):

        self.client.login(
            username="user2",
            password="12345"
        )
        
        url = reverse("note_detail",kwargs={"product_id": self.todo.id}
)
        
        
        response = self.client.put(url, 
                                   data={"title": "othertitle"},
                                    content_type="application/json")
        self.assertNotEqual(response.status_code, 200)

