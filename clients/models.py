"""Contains the models of accounts app."""

# django
from django.db import models
from django.utils.translation import gettext_lazy as _

# accounts
from accounts.models import User


class Client(models.Model):
    """This is a class allowing to create a Client."""
    first_name = models.CharField(_('first name'), max_length=25)
    last_name = models.CharField(_('last name'), max_length=25)
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A client with that email address already exists."),
        },
    )
    phone = models.CharField(
        _('phone number'),
        max_length=20,
        unique=True,
        error_messages={
            'unique': _("A client with that phone number already exists."),
        },
    )
    mobile = models.CharField(
        _('mobile number'),
        max_length=20,
        unique=True,
        error_messages={
            'unique': _("A client with that mobile number exists."),
        },
    )
    company_name = models.CharField(_('company name'), max_length=250)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    sales_contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 2},
        error_messages={
            'limit_choices_to': _("This user is not part of the sales team."),
        },
        verbose_name=_('sales contact'),
    )

    class Meta:
        """Meta options."""
        verbose_name = _('client')
        verbose_name_plural = _('clients')

    def __str__(self):
        """Overrides method in Model."""
        return f"{self.email}"
