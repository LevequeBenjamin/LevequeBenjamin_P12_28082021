"""Contains the views of accounts app."""

# rest_framework
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

# models
from accounts.models import User

# serializers
from accounts.serializers import UserSerializer


class UserListView(ListAPIView):
    """
    Concrete view for listing a queryset or creating a CustomUser instance.
    """

    # Overrides attributes in GenericApiView
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveView(RetrieveAPIView):
    """
    Concrete view for listing a queryset or creating a CustomUser instance.
    """

    # Overrides attributes in GenericApiView
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
