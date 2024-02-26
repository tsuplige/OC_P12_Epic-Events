# Création d'un nouvel utilisateur
# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
from django.contrib.auth import authenticate


class Command(BaseCommand):
    help = 'Connecte un utilisateur'

    def handle(self, *args, **kwargs):
        load_dotenv()
        username = os.getenv('USER_NAME')
        password = os.getenv('PASSWORD')
        user = authenticate(username=username, password=password)
        if user is not None:
            self.stdout.write(self.style.SUCCESS(f'Connexion réussie {user}'))
        else:
            self.stdout.write(self.style.ERROR(
                'Nom d\'utilisateur ou mot de passe incorrect'))
