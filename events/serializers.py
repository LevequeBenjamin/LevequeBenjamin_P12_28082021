from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    event_date = serializers.DateTimeField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"])

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
