from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated

class Command(BaseCommand):
    help = 'Modifie un utilisateur existant'

    # def add_arguments(self, parser):
    #     parser.add_argument('username', type=str, help='Nom d\'utilisateur')
    #     parser.add_argument('--email', type=str, help='Nouvelle adresse e-mail')
    #     parser.add_argument('--department', type=str, help='Nouveau département')

    def handle(self, *args, **kwargs):
        if is_authenticated('Gestion'):
            username = input('username: ')

            try:
                user = get_user_model().objects.get(username=username)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"L'utilisateur avec le nom '{username}' n'existe pas."))
                return
            new_username = input('new_username: ')
            new_email = input('new_email: ')
            new_department = input('new_department: ')
            new_first_name = input('new_firstname: ')
            new_last_name = input('new_lastname: ')

            if new_username:
                user.username = new_username
            if new_email:
                user.email = new_email
            if new_department:
                user.department = new_department
            if new_first_name:
                user.first_name = new_first_name
            if new_last_name:
                user.last_name = new_last_name

            user.save()
            self.stdout.write(self.style.SUCCESS(
                f"Utilisateur '{username}' modifié avec succès"))
        else:
            self.stdout.write(self.style.ERROR(
                'vous n\'etes pas autorisé à modifier ses données'))
