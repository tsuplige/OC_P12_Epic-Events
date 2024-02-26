from django.db import models
from django.conf import settings
from contracts.models import Contract
from users.models import Client


class Event(models.Model):
    title = models.CharField(max_length=50)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='event_support_contacts', null=True)

    def __str__(self):
        return self.title
