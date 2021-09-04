from django.contrib import admin
from django import forms
from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'client', 'contract', 'support_contact', 'event_date', 'is_finished',
            'attendees', 'notes'
        )


class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = (
        "id", 'client', 'contract', 'support_contact', 'event_date', 'is_finished',
        'attendees', 'notes'
    )


admin.site.register(Event, EventAdmin)
