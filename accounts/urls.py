"""Contains the urls of accounts app."""

# django
from django.urls import path, include

# rest_framework
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # POST
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    # POST
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
