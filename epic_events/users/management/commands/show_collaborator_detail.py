from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Affiche le détail d\'un user'

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         'username',
    #         type=str,
    #         help='Username du collaborateur a afficher')

    def handle(self, *args, **kwargs):

        if is_authenticated('Gestion'):
            username = input('username: ')

            try:
                user = get_user_model().objects.get(username=username)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"L'utilisateur avec le nom '{username}' n'existe pas."))
                return
            self.stdout.write(self.style.SUCCESS(
                f"Information sur le collaborateur n°{user.id}"))
            self.stdout.write(self.style.SUCCESS(f"username:{user.username}\n"
                                                 f"email:{user.email}\n"
                                                 f"name:{user.first_name} {user.last_name}\n"
                                                 f"department:{user.department}\n"))
        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à acceder au données'))
