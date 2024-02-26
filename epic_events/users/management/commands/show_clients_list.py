from django.core.management.base import BaseCommand
from users.models import Client


class Command(BaseCommand):
    help = 'Affiche la liste des clients'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(self.style.SUCCESS(
                f"id:{client.id} | name:{client.name} | email:{client.email} | phone:{client.telephone}"))
