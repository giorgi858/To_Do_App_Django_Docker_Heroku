from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import CreateUserView

urlpatterns = [
    path('main/area/news/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('', include('note.urls')),    
    path('api/user/register/',CreateUserView.as_view(), name='register'),
    path('api/token/',TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token-refresh'),
]


