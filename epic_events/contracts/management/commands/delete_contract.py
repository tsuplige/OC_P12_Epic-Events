# from django.core.management.base import BaseCommand
# from contracts.models import Contract
# from django.core.exceptions import ObjectDoesNotExist


# class Command(BaseCommand):
#     help = 'Supprime un contrat existant'

#     def add_arguments(self, parser):
#         parser.add_argument('contract_id', type=int, help='ID du contrat à supprimer')

#     def handle(self, *args, **kwargs):
#         contract_id = kwargs['contract_id']

#         try:
#             contract = Contract.objects.get(pk=contract_id)
#         except ObjectDoesNotExist:
#             self.stdout.write(self.style.ERROR(
#                 f"Le contrat avec l'ID '{contract_id}' n'existe pas."))
#             return

#         contract.delete()
#         self.stdout.write(self.style.SUCCESS(
#             f"Contrat avec l'ID '{contract_id}' supprimé avec succès"))
