from django.urls import path
from .views import NoteLIstCreateAPIView, NoteDetailAPIView

urlpatterns = [
    path('todos/', NoteLIstCreateAPIView.as_view() , name="api_home"),
    path('todos/<uuid:product_id>/', NoteDetailAPIView.as_view(), name='note_detail'),    
]
