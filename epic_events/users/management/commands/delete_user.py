from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Supprime un utilisateur existant'

    # def add_arguments(self, parser):
    #     parser.add_argument('username', type=str, help='Nom d\'utilisateur')

    def handle(self, *args, **kwargs):
        username = input('username: ')

        try:
            user = get_user_model().objects.get(username=username)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f"L'utilisateur avec le nom '{username}' n'existe pas."))
            return

        user.delete()
        self.stdout.write(self.style.SUCCESS(f"Utilisateur '{username}' supprimé avec succès"))
