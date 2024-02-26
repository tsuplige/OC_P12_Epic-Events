from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from contracts.models import Contract
from users.models import Client
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated, is_support_contact


class Command(BaseCommand):
    help = 'Modifie un contrat existant'

    def handle(self, *args, **kwargs):
        contract_id = input('contract_id: ')

        try:
            contract = Contract.objects.get(id=contract_id)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(
                f"Le contrat avec l'id: '{contract_id}' n'existe pas."))
            return

        if is_authenticated('Gestion') or is_support_contact(contract):
            new_total_amount = input('new_total_amount: ')
            new_remaining_amount = input('new_remaining_amount: ')
            new_status = input('new_status: ')
            new_client_id = input('new_client_id: ')
            new_support_contact_name = input('new_support_contact_name: ')

            if new_total_amount:
                contract.total_amount = new_total_amount
            if new_support_contact_name:
                try:
                    new_support_contact = get_user_model().objects.get(
                        username=new_support_contact_name)
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f"Le collaborateur avec l'username"
                        f"'{new_support_contact_name}' n'existe pas."))
                    return
                contract.support_contact = new_support_contact
            if new_remaining_amount:
                contract.remaining_amount = new_remaining_amount
            if new_status:
                contract.status = new_status
            if new_client_id:
                try:
                    new_client = Client.objects.get(id=new_client_id)
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f"Le client avec l'ID '{new_client_id}' n'existe pas."
                        ))
                    return
                contract.client = new_client

            contract.save()
            self.stdout.write(self.style.SUCCESS(
                f"Contrat '{contract.id}' modifié avec succès"))
        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à modifier ses données'))
