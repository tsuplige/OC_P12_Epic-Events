from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Modifie un utilisateur existant'

    # def add_arguments(self, parser):
    #     parser.add_argument('username', type=str, help='Nom d\'utilisateur')
    #     parser.add_argument('--email', type=str, help='Nouvelle adresse e-mail')
    #     parser.add_argument('--department', type=str, help='Nouveau département')

    def handle(self, *args, **kwargs):
        username = input('username: ')

        try:
            user = get_user_model().objects.get(username=username)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f"L'utilisateur avec le nom '{username}' n'existe pas."))
            return
        new_email = input('email: ')
        new_department = input('department: ')
        new_first_name = input('firstname: ')
        new_last_name = input('lastname: ')

        if new_email:
            user.email = new_email
        if new_department:
            user.department = new_department
        if new_first_name:
            user.first_name = new_first_name
        if new_last_name:
            user.last_name = new_last_name

        user.save()
        self.stdout.write(self.style.SUCCESS(f"Utilisateur '{username}' modifié avec succès"))