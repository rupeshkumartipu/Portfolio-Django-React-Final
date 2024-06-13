from django.core.management.base import BaseCommand
from portfolio_app.models import Experience

class Command(BaseCommand):
    help = 'Removes duplicate entries from the Experience table'

    def handle(self, *args, **kwargs):
        unique_entries = set()
        duplicates = []

        for experience in Experience.objects.all():
            identifier = (experience.organization, experience.positions_held, experience.from_date, experience.to_date, experience.duration)
            if identifier in unique_entries:
                duplicates.append(experience.id)
            else:
                unique_entries.add(identifier)

        if duplicates:
            Experience.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
