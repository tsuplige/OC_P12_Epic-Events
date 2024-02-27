from django.core.management.base import BaseCommand
from contracts.models import Contract
from django.contrib.auth import get_user_model
from users.models import Client
from users.permissions import is_authenticated
from django.core.exceptions import ObjectDoesNotExist
import sentry_sdk


class Command(BaseCommand):
    help = 'Crée un nouveau contrat'

    def handle(self, *args, **kwargs):

        if is_authenticated('Gestion'):

            total_amount = input('total_amount: ')
            remaining_amount = input('remaining_amount: ')
            status = input('status: ')
            client_id = input('client_id: ')
            try:
                client = Client.objects.get(id=client_id)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Le client avec l'ID '{client_id}' n'existe pas."))
                return
            support_contact_name = input('support_contact_username: ')
            try:
                support_contact = get_user_model().objects.get(
                    username=support_contact_name)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Le collaborateur avec l'username'{support_contact_name}' n'existe pas."))
                return

            contract = Contract.objects.create(total_amount=total_amount,
                                               remaining_amount=remaining_amount,
                                               status=status,
                                               support_contact=support_contact,
                                               client=client)

            self.stdout.write(self.style.SUCCESS(
                f"Contrat : {contract} créé avec succès !"))
            sentry_sdk.capture_message('Un contrat a été Créé')
            if status == 'Sign':
                sentry_sdk.capture_message(
                    f'le contrat n°{contract.id} a été Signé!')

        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à créé des contrats'))
