import jwt
from django.core.management.base import BaseCommand
from django.contrib.auth import authenticate
from dotenv import load_dotenv
import os


class Command(BaseCommand):
    help = 'Connecte un utilisateur et enregistre un jeton JWT dans un fichier texte'

    def handle(self, *args, **kwargs):
        load_dotenv()

        username = os.getenv('USER_NAME')
        password = os.getenv('PASSWORD')

        user = authenticate(username=username, password=password)

        if user is not None:
            payload = {'username': user.username,
                       'department': user.department}
            jwt_token = jwt.encode(payload, 'secret', algorithm='HS256')

            with open('jwt_token.txt', 'w') as file:
                file.write(jwt_token)

            self.stdout.write(self.style.SUCCESS(
                "Connexion réussie. Jeton JWT enregistré dans 'jwt_token.txt'"))
        else:
            self.stdout.write(self.style.ERROR(
                "Échec de la connexion. Vérifiez les identifiants dans le fichier .env"))
