from django.conf import settings
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="todos",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return f"{self.title[:30]} — {self.author}"
