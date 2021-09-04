"""Contains the models of contracts app."""

# django
from django.db import models

# models
from accounts.models import User
from clients.models import Client


class Contract(models.Model):
    """This is a class allowing to create a Contract."""
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
    )
    sales_contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 2}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()
    payment_due_date = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        """Overrides method in Model."""
        return f"{self.client} -  {self.created_at.strftime('%d/%m/%Y - %H:%M:%S')}"
