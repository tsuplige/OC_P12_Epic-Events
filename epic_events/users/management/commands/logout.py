from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Déconnecte l\'utilisateur en supprimant le jeton JWT'

    def handle(self, *args, **kwargs):
        if os.path.exists('jwt_token.txt'):
            os.remove('jwt_token.txt')
            self.stdout.write(self.style.SUCCESS(
                "Déconnexion réussie. Le jeton JWT a été supprimé."))
        else:
            self.stdout.write(self.style.ERROR(
                "Aucun jeton JWT trouvé. Vous êtes déjà déconnecté."))
