from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("task", "created", "updated")
    ordering = ("-created",)