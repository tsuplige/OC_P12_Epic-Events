from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    class DEPARTMENT_CHOICES(models.TextChoices):
        COMMERCIAL = 'Commercial'
        SUPPORT = 'Support'
        GESTION = 'Gestion'

    email = models.EmailField()
    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES.choices,
        verbose_name='Département'
    )

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.department}"


class Client(models.Model):

    information = models.CharField(max_length=50)
    name = models.fields.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=13)
    compagny_name = models.CharField(max_length=50)
    last_update = models.DateField(auto_now_add=True)
    creation_date = models.DateField(auto_now_add=True)

    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='client_support_contacts', null=True)

    def __str__(self):
        return self.name
