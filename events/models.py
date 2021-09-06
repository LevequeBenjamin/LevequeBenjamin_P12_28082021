"""Contains the models of events app."""

# django
from django.db import models
from django.utils.translation import gettext_lazy as _

# models
from accounts.models import User
from clients.models import Client
from contracts.models import Contract


class Event(models.Model):
    """This is a class allowing to create a Event."""
    title = models.CharField(_('title'), max_length=50)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name=_('client'))
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, verbose_name=_('contract'))
    support_contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 3},
        error_messages={
            'limit_choices_to': _("This user is not part of the support team."),
        },
        verbose_name=_('support contact')
    )
    event_date = models.DateTimeField(_('event date'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    is_finished = models.BooleanField(_('is finished'), default=False)
    attendees = models.IntegerField(_('attendees'))
    notes = models.TextField(_('notes'))

    class Meta:
        """Meta options."""
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __str__(self):
        """Overrides method in Model."""
        return f"{self.title}"
