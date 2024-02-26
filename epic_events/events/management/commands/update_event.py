from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from contracts.models import Contract
from events.models import Event
from users.models import Client
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Modifie un evenement existant'

    def handle(self, *args, **kwargs):
        if is_authenticated('Gestion') or is_authenticated('Support'):
            event_id = input('event_id: ')

            try:
                event = Event.objects.get(id=event_id)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"L'evenement avec l'id: '{event_id}' n'existe pas."))
                return

            new_title = input('new_title: ')
            new_contract_id = input('new_contract_id: ')
            new_date_start = input('new_date_start: ')
            new_date_end = input('new_date_end: ')
            new_client_id = input('new_client_id: ')
            new_support_contact_name = input('new_support_contact_name: ')

            if new_title:
                event.title = new_title
            if new_support_contact_name:
                try:
                    new_support_contact = get_user_model().objects.get(
                        username=new_support_contact_name)
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f"Le collaborateur avec l'username"
                        f"'{new_support_contact_name}' n'existe pas."))
                    return
                event.support_contact = new_support_contact
            if new_date_start:
                event.date_start = new_date_start
            if new_date_end:
                event.date_end = new_date_end
            if new_contract_id:
                try:
                    new_contract = Client.objects.get(id=new_contract_id)
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f"Le contrat avec l'ID '{new_contract_id}' n'existe pas."
                        ))
                    return
                event.contract = new_contract
            if new_client_id:
                try:
                    new_client = Client.objects.get(id=new_client_id)
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f"Le client avec l'ID '{new_client_id}' n'existe pas."
                        ))
                    return
                event.client = new_client

            event.save()
            self.stdout.write(self.style.SUCCESS(
                f"Evenement '{event.id}' modifié avec succès"))
        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à modifier ses données'))
