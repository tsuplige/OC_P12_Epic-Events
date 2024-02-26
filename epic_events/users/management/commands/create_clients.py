from django.core.management.base import BaseCommand
from users.models import Client


class Command(BaseCommand):
    help = 'Crée un nouveau client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Nom du client')
        parser.add_argument('email', type=str, help='Adresse e-mail')
        parser.add_argument('telephone', type=str, help='Numéro de téléphone')
        parser.add_argument('company_name', type=str, help='Nom de la société')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        telephone = kwargs['telephone']
        company_name = kwargs['company_name']
        client = Client.objects.create(name=name,
                                       email=email,
                                       telephone=telephone,
                                       company_name=company_name)
        self.stdout.write(self.style.SUCCESS(
            f"Client '{name}' créé avec succès"))
