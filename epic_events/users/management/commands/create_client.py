from django.core.management.base import BaseCommand
from users.models import Client
from users.permissions import is_authenticated
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Crée un nouveau client'

    # def add_arguments(self, parser):
    #     parser.add_argument('name', type=str, help='Nom du client')
    #     parser.add_argument('email', type=str, help='Adresse e-mail')
    #     parser.add_argument(
    # 'telephone', type=str, help='Numéro de téléphone')
    #     parser.add_argument(
    # 'company_name', type=str, help='Nom de la société')

    def handle(self, *args, **kwargs):
        if is_authenticated('Commercial'):
            name = input('name: ')
            email = input('email: ')
            telephone = input('telephone: ')
            compagny_name = input('compagny_name_name: ')
            support_contact_name = input('support_contact_username: ')
            try:
                support_contact = get_user_model().objects.get(
                    username=support_contact_name)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Le collaborateur avec l'username'{support_contact_name}' n'existe pas."))
                return
            client = Client.objects.create(name=name,
                                           email=email,
                                           telephone=telephone,
                                           compagny_name=compagny_name,
                                           support_contact=support_contact)
            self.stdout.write(self.style.SUCCESS(
                f"Client '{client.name}' créé avec succès"))
        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à créé des clients'))
