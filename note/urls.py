from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.aboutView, name='about'),
    path('todolist/', views.todolistView, name='todo'),
    path('form/', views.myform, name='myform'),
    path('task/<uuid:pk>/', views.note_update_view, name='edit_task'),
    path('task/delete/<uuid:pk>/', views.note_delete_view, name='product_delete'),
    path("username/change/", views.change_username, name="account_change_username"),
    path('search/', views.SearchResultListView.as_view(), name='search_results'),


   
]
