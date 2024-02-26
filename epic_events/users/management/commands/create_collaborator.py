from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Crée un nouvel utilisateur'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Nom d\'utilisateur')
        parser.add_argument('email', type=str, help='Adresse e-mail')
        parser.add_argument('department', type=str, help='Département')

    def handle(self, *args, **kwargs):

        if is_authenticated('Gestion'):
            User = get_user_model()
            username = input('username: ')
            first_name = input('first_name: ')
            last_name = input('last_name: ')
            email = input('email: ')
            department = input('department: ')
            password = input('password: ')
            user = User.objects.create_user(username=username,
                                            email=email,
                                            department=department,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name)

            self.stdout.write(self.style.SUCCESS(
                f"Utilisateur '{username}' créé avec succès : {user}"))

        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à créé des collaborateurs'))
