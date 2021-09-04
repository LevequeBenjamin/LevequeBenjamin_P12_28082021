from django.db import models

from accounts.models import User
from clients.models import Client
from contracts.models import Contract


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 3}
    )
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=False)
    attendees = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.client} -  {self.created_at.strftime('%d/%m/%Y - %H:%M:%S')}"
