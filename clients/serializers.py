"""Contains the serializers of client app."""

# rest_framework
from rest_framework import serializers

# models
from accounts.serializers import UserSerializer
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    sales_contact = UserSerializer(read_only=True)

    class Meta:
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
