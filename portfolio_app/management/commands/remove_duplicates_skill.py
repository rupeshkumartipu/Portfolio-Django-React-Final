from django.core.management.base import BaseCommand
from portfolio_app.models import Skill

class Command(BaseCommand):
    help = 'Removes duplicate entries from the Skill table'

    def handle(self, *args, **kwargs):
        unique_entries = set()
        duplicates = []

        for skill in Skill.objects.all():
            identifier = (skill.name, skill.level, skill.project_for_which_used)
            if identifier in unique_entries:
                duplicates.append(skill.id)
            else:
                unique_entries.add(identifier)

        if duplicates:
            Skill.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
