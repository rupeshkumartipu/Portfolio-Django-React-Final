from django.core.management.base import BaseCommand
from portfolio_app.models import Education


class Command(BaseCommand):
    help = 'Removes duplicate entries from the Education table'

    def handle(self, *args, **kwargs):
        unique_entries = set()
        duplicates = []

        for education in Education.objects.all():
            identifier = (education.degree, education.university, education.result, education.year_of_passing,
                          education.specialization)
            if identifier in unique_entries:
                duplicates.append(education.id)
            else:
                unique_entries.add(identifier)

        if duplicates:
            Education.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
