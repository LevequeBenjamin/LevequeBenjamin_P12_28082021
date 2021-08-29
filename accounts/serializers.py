from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Docstrings.
    """
    class Meta:
        """
        Docstrings.
        """
        model = User
        fields = ("id", "username", "role", "password")
