"""Customizing the administrator interface."""

# django
from django.contrib import admin
from django import forms

# models
from events.models import Event


class EventForm(forms.ModelForm):
    """EventForm inherits from ModelForm for creating Event form."""
    class Meta:
        """Meta options."""
        model = Event
        fields = (
            'client', 'contract', 'support_contact', 'event_date', 'is_finished',
            'attendees', 'notes'
        )


class EventAdmin(admin.ModelAdmin):
    """Overrides attributes in BaseModelAdmin."""
    form = EventForm
    list_display = (
        "id", 'client', 'contract', 'support_contact', 'event_date', 'is_finished',
        'attendees', 'notes'
    )


admin.site.register(Event, EventAdmin)
