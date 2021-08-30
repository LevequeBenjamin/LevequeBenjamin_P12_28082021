"""Contains the serializers of accounts app."""

# rest_framework
from rest_framework import serializers

# models
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Allows to serialize or deserialize the user according
    to the verb of the request.
    """
    class Meta:
        """Meta options."""
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "role")
