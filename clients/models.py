"""Contains the models of accounts app."""

# django
from django.db import models
from django.utils.translation import gettext_lazy as _

# accounts
from accounts.models import User


class Client(models.Model):
    """This is a class allowing to create a Client."""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    company_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 2}
    )

    def __str__(self):
        """Overrides method in Model."""
        return f"{self.email}"
