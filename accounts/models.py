
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

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

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    object = UserManager()

    class Meta:
        """
        Docstrings.
        """
        verbose_name = 'user'
        verbose_name_plural = 'users'
