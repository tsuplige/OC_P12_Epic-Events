from django.core.management.base import BaseCommand
from events.models import Event
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'Affiche la liste des evenements'

    def handle(self, *args, **kwargs):

        if is_authenticated('any'):
            events = Event.objects.all()
            for event in events:
                self.stdout.write(self.style.SUCCESS(
                    f"id:{event.id} | title:{event.title} | contract:{event.contract} | client:{event.client} | support_contact:{event.support_contact}"))
        else:
            self.stdout.write(self.style.ERROR('vous n\'etes pas autorisé à acceder au données'))