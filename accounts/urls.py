"""Contains the urls of accounts app."""

# django
from django.urls import path

# rest_framework
from rest_framework_simplejwt import views as jwt_views

# views
from accounts.views import UserListView

urlpatterns = [
    # POST
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    # POST
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # GET
    path('users/', UserListView.as_view(), name='users'),
]
