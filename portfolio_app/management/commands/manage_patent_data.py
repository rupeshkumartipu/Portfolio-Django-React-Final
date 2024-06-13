from django.core.management.base import BaseCommand
from portfolio_app.models import Patent
from datetime import datetime

class Command(BaseCommand):
    help = 'Inserts initial data into the Patent table and removes duplicates'

    def handle(self, *args, **kwargs):
        # Insert data
        patent_data = [
            {
                'sr_no': 1,
                'patent_title': 'SMARTPREDICT: CONCRETE STRENGTH ESTIMATION VIA MACHINE LEARNING',
                'inventors': 'Rupesh Kumar Tipu',
                'country': 'India',
                'application_number': '202411014830',
                'publication_date': '2024-03-08',
                'status': 'Published'
            },
            {
                'sr_no': 2,
                'patent_title': 'MACHINE LEARNING-BASED GUI FOR ESTIMATING THE STRENGTH OF RECYCLED AGGREGATE CONCRETE',
                'inventors': 'Rupesh Kumar Tipu',
                'country': 'India',
                'application_number': '202411011153',
                'publication_date': '2024-02-23',
                'status': 'Published'
            },
            {
                'sr_no': 3,
                'patent_title': 'INNOVATIVE GUI-BASED APPROACH FOR PREDICTING FLOW AND COMPRESSIVE STRENGTH IN HIGH-PERFORMANCE CONCRETE',
                'inventors': 'Rupesh Kumar Tipu',
                'country': 'India',
                'application_number': '202411007500',
                'publication_date': '2024-02-16',
                'status': 'Published'
            },
            {
                'sr_no': 4,
                'patent_title': 'INTELLIGENT PREDICTIVE SYSTEM AND USER INTERFACE FOR HIGHPERFORMANCE CONCRETE COMPRESSIVE STRENGTH ASSESSMENT',
                'inventors': 'Rupesh Kumar Tipu',
                'country': 'India',
                'application_number': '202411007359',
                'publication_date': '2024-02-02',
                'status': 'Published'
            },
            {
                'sr_no': 5,
                'patent_title': 'Machine Learning-Enhanced Graphical Interface for Optimized Concrete Mix Design',
                'inventors': 'Rupesh Kumar Tipu',
                'country': 'India',
                'application_number': '202411019684',
                'publication_date': '2024-03-16',
                'status': 'Published'
            }
        ]

        for data in patent_data:
            Patent.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully inserted patent data'))

        # Remove duplicates
        unique_entries = set()
        duplicates = []

        for patent in Patent.objects.all():
            identifier = (
                patent.sr_no,
                patent.patent_title,
                patent.inventors,
                patent.country,
                patent.application_number,
                patent.publication_date,
                patent.status
            )
            if identifier in unique_entries:
                duplicates.append(patent.id)
            else:
                unique_entries.add(identifier)

        if duplicates:
            Patent.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
