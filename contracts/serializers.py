"""Contains the serializers of client app."""

# rest_framework
from rest_framework import serializers

# models
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    payment_due_date = serializers.DateTimeField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"])

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
