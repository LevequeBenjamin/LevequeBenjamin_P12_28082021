"""Contains the models of contracts app."""

# django
from django.db import models
from django.utils.translation import gettext_lazy as _

# models
from accounts.models import User
from clients.models import Client


class Contract(models.Model):
    """This is a class allowing to create a Contract."""
    title = models.CharField(_('title'), max_length=50)
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        verbose_name=_('client')
    )
    sales_contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 2},
        error_messages={
            'limit_choices_to': _("This user is not part of the sales team."),
        },
        verbose_name=_('sales contact')
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    amount = models.IntegerField(_('amount'))
    payment_due_date = models.DateTimeField(_('payment due date'))
    is_finished = models.BooleanField(_('is finished'), default=False)
    is_paid = models.BooleanField(_('is paid'), default=False)

    class Meta:
        """Meta options."""
        verbose_name = _('contract')
        verbose_name_plural = _('contracts')

    def __str__(self):
        """Overrides method in Model."""
        return f"{self.title}"
