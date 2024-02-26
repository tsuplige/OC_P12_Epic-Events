from django.core.management.base import BaseCommand
from events.models import Event
from django.core.exceptions import ObjectDoesNotExist
from users.permissions import is_authenticated


class Command(BaseCommand):
    help = 'affiche le detail d\'un evenements'

    def add_arguments(self, parser):
        parser.add_argument(
            'event_id',
            type=int,
            help='ID de l\'event à modifier')

    def handle(self, *args, **kwargs):
        if is_authenticated('any'):
            event_id = kwargs['event_id']

            try:
                event = Event.objects.get(pk=event_id)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Le client avec l'ID '{event_id}' n'existe pas."))
                return

            self.stdout.write(self.style.SUCCESS(
                f"Information sur le client n°{event.id}"))
            self.stdout.write(self.style.SUCCESS(f"title:{event.title}\n"
                                                 f"contract:{event.contract}\n"
                                                 f"client:{event.client}\n"
                                                 f"date_start:{event.date_start}\n"
                                                 f"date_end:{event.date_end}\n"
                                                 f"support_contact:{event.support_contact}"))
        else:
            self.stdout.write(self.style.ERROR('vous n\'etes pas autorisé à acceder au données'))
