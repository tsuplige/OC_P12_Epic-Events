from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from contracts.models import Contract
from events.models import Event
from users.models import Client
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Créé un evenement'

    def handle(self, *args, **kwargs):
        if is_authenticated('Commercial'):

            title = input('title: ')
            contract_id = input('contract_id: ')
            try:
                contract = Client.objects.get(id=contract_id)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                        f"Le contrat avec l'ID '{contract_id}' n'existe pas."
                        ))
                return
            date_start = input('date_start: ')
            date_end = input('date_end: ')
            client_id = input('client_id: ')
            try:
                client = Client.objects.get(id=client_id)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                        f"Le client avec l'ID '{client_id}' n'existe pas."
                        ))
                return
            support_contact_name = input('support_contact_name: ')
            try:
                support_contact = get_user_model().objects.get(
                    username=support_contact_name)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Le collaborateur avec l'username"
                    f"'{support_contact_name}' n'existe pas."))
                return

            event = Event.objects.create(title=title,
                                        contract=contract,
                                        date_start=date_start,
                                        date_end=date_end,
                                        client=client,
                                        support_contact=support_contact
                                        )

            self.stdout.write(self.style.SUCCESS(
                    "évenement créé avec succès !"))

        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à créé des contrats'))
