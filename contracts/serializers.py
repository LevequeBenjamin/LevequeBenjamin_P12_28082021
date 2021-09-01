"""Contains the serializers of client app."""

# rest_framework
from rest_framework import serializers

# models
from accounts.serializers import UserSerializer
from clients.serializers import ClientSerializer
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    payment_due_date = serializers.DateTimeField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"])
    sales_contact = UserSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = (
            "id",
            "client",
            "amount",
            "payment_due_date",
            "sales_contact",
            "is_finished",
            "is_paid",
        )
