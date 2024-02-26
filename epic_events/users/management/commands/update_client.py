from django.core.management.base import BaseCommand
from users.models import Client
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Modifie un client existant'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='ID du client à modifier')
        parser.add_argument('--email', type=str, help='Nouvelle adresse e-mail')
        parser.add_argument('--telephone', type=str, help='Nouveau numéro de téléphone')
        parser.add_argument('--company_name', type=str, help='Nouveau nom de la société')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        new_email = kwargs.get('email')
        new_telephone = kwargs.get('telephone')
        new_company_name = kwargs.get('company_name')

        try:
            client = Client.objects.get(pk=client_id)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f"Le client avec l'ID '{client_id}' n'existe pas."))
            return

        if new_email:
            client.email = new_email
        if new_telephone:
            client.telephone = new_telephone
        if new_company_name:
            client.company_name = new_company_name

        client.save()
        self.stdout.write(self.style.SUCCESS(f"Client avec l'ID '{client_id}' modifié avec succès"))
