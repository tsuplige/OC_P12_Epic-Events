from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from django.core.exceptions import PermissionDenied
import os
from django.contrib.auth import authenticate
from dotenv import load_dotenv


class Command(BaseCommand):
    help = 'Crée un nouvel utilisateur'

    # def add_arguments(self, parser):
    #     parser.add_argument('username', type=str, help='Nom d\'utilisateur')
    #     parser.add_argument('email', type=str, help='Adresse e-mail')
    #     parser.add_argument('department', type=str, help='Département')

    def handle(self, *args, **kwargs):
        load_dotenv()
        usern = os.getenv('USER_NAME')
        passw = os.getenv('PASSWORD')
        connected_user = authenticate(username=usern, password=passw)

        if connected_user.department == 'Gestion':

            User = get_user_model()
            username = input('username: ')
            email = input('email: ')
            department = input('department: ')
            password = input('password: ')
            user = User.objects.create_user(username=username,
                                            email=email,
                                            department=department,
                                            password=password)
            self.stdout.write(self.style.SUCCESS(
                f"Utilisateur '{username}' créé avec succès : {user}"))
        else:
            self.stdout.write(self.style.SUCCESS(
                f"vous n'avez pas les droit pour faire cette commande"))
