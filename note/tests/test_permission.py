from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from note.models import Todo


class PermissionTests(APITestCase):

    def setUp(self):

        self.user1 = User.objects.create_user(
            username="user1",
            password="12345"
        )

        self.user2 = User.objects.create_user(
            username="user2",
            password="12345"
        )

        self.todo1 = Todo.objects.create(
            title="todo1",
            author=self.user1
        )

        self.todo2 = Todo.objects.create(
            title="todo2",
            author=self.user2
        )

    # -----------------------
    # NOT AUTHENTICATED
    # -----------------------
    def test_auth_required(self):

        url = reverse("api_home")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)


    # -----------------------
    # USER SEE ONLY OWN TODOS
    # -----------------------
    def test_user_sees_only_own_todos(self):

        self.client.login(
            username="user1",
            password="12345"
        )

        url = reverse("api_home")

        response = self.client.get(url)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "todo1")


    # -----------------------
    # USER CANNOT EDIT OTHER TODO
    # -----------------------
    def test_user_cannot_edit_other_user_todo(self):

        self.client.login(
            username="user2",
            password="12345"
        )

        url = reverse(
            "note_detail",
            kwargs={"product_id": self.todo1.id}
        )

        response = self.client.put(
            url,
            data={"title": "hack"},
            format="json"
        )

        self.assertEqual(response.status_code, 404)


    # -----------------------
    # USER CANNOT DELETE OTHER TODO
    # -----------------------
    def test_user_cannot_delete_other_user_todo(self):

        self.client.login(
            username="user2",
            password="12345"
        )

        url = reverse(
            "note_detail",
            kwargs={"product_id": self.todo1.id}
        )

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 404)


    # -----------------------
    # USER CAN EDIT OWN TODO
    # -----------------------
    def test_user_can_edit_own_todo(self):

        self.client.login(
            username="user1",
            password="12345"
        )

        url = reverse(
            "note_detail",
            kwargs={"product_id": self.todo1.id}
        )

        response = self.client.put(
            url,
            data={"title": "updated"},
            format="json"
        )

        self.assertEqual(response.status_code, 200)