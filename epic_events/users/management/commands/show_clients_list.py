from django.core.management.base import BaseCommand
from users.models import Client
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Affiche la liste des clients'

    def handle(self, *args, **kwargs):

        if is_authenticated('any'):
            clients = Client.objects.all()
            for client in clients:
                self.stdout.write(self.style.SUCCESS(
                    f"id:{client.id} |"
                    f" name:{client.name} |"
                    f" email:{client.email} |"
                    f" phone:{client.telephone}"))
        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à acceder au données'))
