from django.core.management.base import BaseCommand
from contracts.models import Contract
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Affiche la liste des Contrats'

    def handle(self, *args, **kwargs):

        if is_authenticated('any'):
            contracts = Contract.objects.all()
            for contract in contracts:
                self.stdout.write(self.style.SUCCESS(
                    f"id:{contract.id} "
                    f"| total_amount:{contract.total_amount} "
                    f"| status:{contract.status} "
                    f"| client:{contract.client} "
                    f"| support_contact:{contract.support_contact}"))
        else:
            self.stdout.write(self.style.ERROR('vous n\'etes pas autorisé à acceder au données'))
