from django.db import models
from users.models import Client
from django.conf import settings


class Contract(models.Model):

    class Status(models.TextChoices):
        SIGN = "Sign"
        TO_SIGN = "To-sign"

    total_amount = models.fields.FloatField()
    remaining_amount = models.fields.FloatField()
    status = models.fields.CharField(choices=Status.choices, max_length=10)
    creation_date = models.DateField(auto_now_add=True)

    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE,
        related_name='contracts', null=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='contract_support_contacts', null=True)

    def __str__(self):
        return str(self.id)
