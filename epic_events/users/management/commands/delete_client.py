from django.core.management.base import BaseCommand
from users.models import Client
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Supprime un client existant'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='ID du client à supprimer')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']

        try:
            client = Client.objects.get(pk=client_id)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(
                f"Le client avec l'ID '{client_id}' n'existe pas."))
            return

        client.delete()
        self.stdout.write(self.style.SUCCESS(
            f"Client avec l'ID '{client_id}' supprimé avec succès"))
