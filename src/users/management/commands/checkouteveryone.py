from django.core.management.base import BaseCommand, CommandError
from users.models import Person

class Command(BaseCommand):
    help = 'Check-out everyone'

    def handle(self, *args, **options):
        people = Person.objects.all()
        i = 0
        for person in people:
            person.checked_in = False
            person.save()
            i+=1

        self.stdout.write('Successfully checked out %s people' % i)
