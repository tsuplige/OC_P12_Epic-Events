from django.core.management.base import BaseCommand
from users.models import Client
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'affiche le detail d\'un client'

    def add_arguments(self, parser):
        parser.add_argument(
            'client_id',
            type=int,
            help='ID du client à modifier')

    def handle(self, *args, **kwargs):
        if is_authenticated('any'):
            client_id = kwargs['client_id']

            try:
                client = Client.objects.get(pk=client_id)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Le client avec l'ID '{client_id}' n'existe pas."))
                return

            self.stdout.write(self.style.SUCCESS(
                f"Information sur le client n°{client.id}"))
            self.stdout.write(self.style.SUCCESS(f"{client.information}\n"
                                                 f"name:{client.name}\nemail:{client.email}\n"
                                                 f"telephone:{client.telephone}\n"
                                                 f"compagny_name:{client.compagny_name}\n"
                                                 f"creation_date:{client.creation_date}\n"
                                                 f"support_contact:{client.support_contact}"))
        else:
            self.stdout.write(self.style.ERROR('vous n\'etes pas autorisé à acceder au données'))
