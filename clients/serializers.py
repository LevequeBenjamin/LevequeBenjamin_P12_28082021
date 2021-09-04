"""Contains the serializers of clients app."""

# rest_framework
from rest_framework import serializers

# serializers
from accounts.serializers import UserSerializer

# models
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """
    Allows to serialize or deserialize the client according
    to the verb of the request.
    """
    sales_contact = UserSerializer(read_only=True)

    class Meta:
        """Meta options."""
        model = Client
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "company_name",
            "sales_contact",
        )
