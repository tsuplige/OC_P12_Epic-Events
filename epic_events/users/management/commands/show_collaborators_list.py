from django.core.management.base import BaseCommand
from users.models import User
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Affiche la liste des utilisateurs'

    def handle(self, *args, **kwargs):

        if is_authenticated('Gestion'):
            users = User.objects.all()
            for user in users:
                self.stdout.write(self.style.SUCCESS(
                    f"id:{user.id} | username:{user.username} |"
                    f" first_name:{user.first_name} |"
                    f"last_name:{user.last_name} |"
                    f" email:{user.email} | department:{user.department}"))
        else:
            self.stdout.write(self.style.ERROR('vous n\'etes pas autorisé à acceder au données'))
