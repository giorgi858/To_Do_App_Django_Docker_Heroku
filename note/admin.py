from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """
    Admin configuration for Todo model.
    - Makes 'created' and 'updated' readonly.
    - Displays task, created, updated in list view.
    - Orders newest tasks first.
    """
    readonly_fields = ("created", "updated")
    list_display = ("task", "created", "updated")
    list_filter = ("created", "updated")  # optional: filter sidebar
    search_fields = ("task", "describtion")  # optional: quick search
    ordering = ("-created",)
