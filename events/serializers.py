from rest_framework import serializers

from accounts.serializers import UserSerializer
from clients.serializers import ClientSerializer
from contracts.serializers import ContractSerializer
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    event_date = serializers.DateTimeField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"])
    client = ClientSerializer(read_only=True)
    contract = ContractSerializer(read_only=True)
    support_contact = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "client",
            "contract",
            "event_date",
            "attendees",
            "notes",
            "is_finished",
            "support_contact",
        )
