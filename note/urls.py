from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.SignupPageView.as_view(), name='signup'),
    path('form/', views.myform, name='myform'),
    path('task/<int:pk>/', views.note_update_view, name='edit_task'),
    path('task/delete/<int:pk>/', views.note_delete_view, name='product_delete'),

   
]
