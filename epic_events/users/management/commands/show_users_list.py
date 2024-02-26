from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Affiche la liste des utilisateurs'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            self.stdout.write(self.style.SUCCESS(
                f"id:{user.id} | username:{user.username} |"
                f" first_name:{user.first_name} |"
                f"last_name:{user.last_name} |"
                f" email:{user.email} | department:{user.department}"))
