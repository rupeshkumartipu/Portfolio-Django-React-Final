from django.core.management.base import BaseCommand
from portfolio_app.models import AreaOfInterest

class Command(BaseCommand):
    help = 'Removes duplicate entries from the AreaOfInterest table'

    def handle(self, *args, **kwargs):
        unique_entries = set()
        duplicates = []

        for area in AreaOfInterest.objects.all():
            identifier = (area.interest, area.projects_done_in_this_area)
            if identifier in unique_entries:
                duplicates.append(area.id)
            else:
                unique_entries.add(identifier)

        if duplicates:
            AreaOfInterest.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
