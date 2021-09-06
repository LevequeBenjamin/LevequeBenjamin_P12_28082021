"""Contains the serializers of contracts app."""

# rest_framework
from rest_framework import serializers

# serializers
from accounts.serializers import UserSerializer
from clients.serializers import ClientSerializer
from contracts.serializers import ContractSerializer

# models
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Allows to serialize or deserialize the event according
    to the verb of the request.
    """
    event_date = serializers.DateTimeField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"])
    client = ClientSerializer(read_only=True)
    contract = ContractSerializer(read_only=True)
    support_contact = UserSerializer(read_only=True)

    class Meta:
        """Meta options."""
        model = Event
        fields = (
            "id",
            "title",
            "client",
            "contract",
            "event_date",
            "attendees",
            "notes",
            "is_finished",
            "support_contact",
        )
