from django.core.management.base import BaseCommand
from portfolio_app.models import SocialLink

class Command(BaseCommand):
    help = 'Inserts initial data into the SocialLink table and removes duplicates'

    def handle(self, *args, **kwargs):
        # Insert data
        social_link_data = [
            {
                'platform_name': 'ORCID ID',
                'url': 'https://orcid.org/0000-0001-8476-8364'
            },
            {
                'platform_name': 'ResearchGate',
                'url': 'https://www.researchgate.net/profile/Rupesh-Kumar-Tipu?ev=hdr_xprf'
            },
            {
                'platform_name': 'Google Scholar',
                'url': 'https://scholar.google.com/citations?user=uZzLU8IAAAAJ&hl=en&oi=ao'
            },
            {
                'platform_name': 'WoS',
                'url': 'https://www.webofscience.com/wos/author/record/AFC-1290-2022'
            },
            {
                'platform_name': 'LinkedIn',
                'url': 'https://www.linkedin.com/in/dr-rupesh-kumar-a60096270/'
            },
            {
                'platform_name': 'VIDWAN',
                'url': 'https://vidwan.inflibnet.ac.in/profile/344917'
            }
        ]

        for data in social_link_data:
            SocialLink.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully inserted social link data'))

        # Remove duplicates
        unique_entries = set()
        duplicates = []

        for social_link in SocialLink.objects.all():
            identifier = (
                social_link.platform_name,
                social_link.url
            )
            if identifier in unique_entries:
                duplicates.append(social_link.id)
            else:
                unique_entries.add(identifier)

        if duplicates:
            SocialLink.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
