"""Contains the serializers of contracts app."""

# rest_framework
from rest_framework import serializers

# models
from contracts.models import Contract

# serializers
from accounts.serializers import UserSerializer
from clients.serializers import ClientSerializer


class ContractSerializer(serializers.ModelSerializer):
    """
    Allows to serialize or deserialize the contract according
    to the verb of the request.
    """
    client = ClientSerializer(read_only=True)
    payment_due_date = serializers.DateTimeField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"])
    sales_contact = UserSerializer(read_only=True)

    class Meta:
        """Meta options."""
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
