from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Supprime un utilisateur existant'

    # def add_arguments(self, parser):
    #     parser.add_argument('username', type=str, help='Nom d\'utilisateur')

    def handle(self, *args, **kwargs):

        if is_authenticated('Gestion'):
            username = input('username: ')

            try:
                user = get_user_model().objects.get(username=username)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"L'utilisateur avec le nom '{username}' n'existe pas."))
                return

            user.delete()
            self.stdout.write(self.style.SUCCESS(
                f"Utilisateur '{username}' supprimé avec succès"))
        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à supprimer ses données'))
