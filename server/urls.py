from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main/area/news/', admin.site.urls),
    path('', include('note.urls')),
    path('accounts/', include('allauth.urls')),

    
]
