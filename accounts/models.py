"""
Contains class User which will allow us to manage the relational
databases of the accounts application.
"""

# django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# managers
from accounts.managers import UserManager


class User(AbstractUser):
    """This is a class allowing to create a User."""

    # These fields tie to the roles!
    MANAGEMENT = 1
    SALES = 2
    SUPPORT = 3

    ROLE_CHOICES = (
        (MANAGEMENT, 'management'),
        (SALES, 'sales'),
        (SUPPORT, 'support')
    )

    role = models.PositiveSmallIntegerField(_('role'), choices=ROLE_CHOICES, blank=True, null=True)

    object = UserManager()

    class Meta:
        """Meta options."""
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ["role"]
