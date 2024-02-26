from django.core.management.base import BaseCommand
from contracts.models import Contract
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'affiche le detail d\'un contrat'

    def add_arguments(self, parser):
        parser.add_argument(
            'contract_id',
            type=int,
            help='ID du contrat à modifier')

    def handle(self, *args, **kwargs):
        if is_authenticated('any'):
            contract_id = kwargs['contract_id']

            try:
                contract = Contract.objects.get(pk=contract_id)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Le client avec l'ID '{contract_id}' n'existe pas."))
                return

            self.stdout.write(self.style.SUCCESS(
                f"Information sur le client n°{contract.id}"))
            self.stdout.write(self.style.SUCCESS(f"total_amount:{contract.total_amount}\n"
                                                 f"remaining_amount:{contract.remaining_amount}\n"
                                                 f"status:{contract.status}\n"
                                                 f"creation_date:{contract.creation_date}\n"
                                                 f"client:{contract.client}\n"
                                                 f"support_contact:{contract.support_contact}"))
        else:
            self.stdout.write(self.style.ERROR('vous n\'etes pas autorisé à acceder au données'))
