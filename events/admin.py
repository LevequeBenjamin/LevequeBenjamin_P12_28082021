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
            "title", 'contract', 'support_contact', 'event_date', 'is_finished',
            'attendees', 'notes'
        )

    def save(self, commit=True):
        """Overrides method in BaseModelForm."""
        event = super().save(commit=False)
        event.client = self.cleaned_data['contract'].client
        if commit:
            event.save()
        return event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Overrides attributes in BaseModelAdmin."""
    form = EventForm
    list_display = (
        "id", "title", 'client', 'contract', 'support_contact', 'event_date', 'is_finished',
        'attendees', 'notes'
    )
    search_fields = ('title',)
    list_filter = ('client', 'contract', 'support_contact', 'is_finished')
    autocomplete_fields = ('client', 'contract', 'support_contact')
    list_per_page = 25
