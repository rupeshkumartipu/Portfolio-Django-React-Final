from django.core.management.base import BaseCommand
from portfolio_app.models import Conference
from datetime import datetime

class Command(BaseCommand):
    help = 'Inserts initial data into the Conference table and removes duplicates'

    def handle(self, *args, **kwargs):
        # Insert data
           conference_data = [
               {
                   'title_of_paper': 'International conference on computer communication and informatics (ICCCI)',
                   'title_of_conference': 'International conference on computer communication and informatics (ICCCI)',
                   'type': 'Online',
                   'date_of_conference': '2024-01-29',
                   'organizing_institute': 'SHRI SHAKTHI INSTITUTE OF ENGINEERING AND TECHNOLOGY',
                   'authors': 'Rupesh Kumar Tipu',
                   'location_of_conference': 'Online',
                   'link_of_conference': ''
               },
               {
                   'title_of_paper': 'International conference on computer communication and informatics (ICCCI)',
                   'title_of_conference': 'International conference on computer communication and informatics (ICCCI)',
                   'type': 'Online',
                   'date_of_conference': '2024-01-29',
                   'organizing_institute': 'SHRI SHAKTHI INSTITUTE OF ENGINEERING AND TECHNOLOGY',
                   'authors': 'Rupesh Kumar Tipu',
                   'location_of_conference': 'Online',
                   'link_of_conference': ''
               },
               {
                   'title_of_paper': 'One-Week Online National Faculty Development Programme on "MOOCs and e-Content Development"',
                   'title_of_conference': 'One-Week Online National Faculty Development Programme on "MOOCs and e-Content Development"',
                   'type': 'Online',
                   'date_of_conference': '2023-04-29',
                   'organizing_institute': 'K. R. Mangalam University',
                   'authors': 'Rupesh Kumar Tipu',
                   'location_of_conference': 'Gurugram',
                   'link_of_conference': ''
               },
               {
                   'title_of_paper': 'Advanced Engineering Optimization Through Intelligent Techniques',
                   'title_of_conference': 'Advanced Engineering Optimization Through Intelligent Techniques',
                   'type': 'Online',
                   'date_of_conference': '2022-01-28',
                   'organizing_institute': 'SVNIT',
                   'authors': 'Rupesh Kumar Tipu',
                   'location_of_conference': 'Surat',
                   'link_of_conference': ''
               },
               {
                   'title_of_paper': 'International Conference on Application of Intelligent Computing in Engineering and Science',
                   'title_of_conference': 'International Conference on Application of Intelligent Computing in Engineering and Science',
                   'type': 'Online',
                   'date_of_conference': '2022-02-12',
                   'organizing_institute': 'NIT',
                   'authors': 'Rupesh Kumar Tipu',
                   'location_of_conference': 'Raipur',
                   'link_of_conference': ''
               },
               {
                   'title_of_paper': 'Cleaner Energy and Carbon-Capture, Utilization, Sequestration and Funding Opportunities for Researchers',
                   'title_of_conference': 'Cleaner Energy and Carbon-Capture, Utilization, Sequestration and Funding Opportunities for Researchers',
                   'type': 'Lecture',
                   'date_of_conference': '2022-10-11',
                   'organizing_institute': 'CHARUSAT University',
                   'authors': 'Rupesh Kumar Tipu',
                   'location_of_conference': 'Anand',
                   'link_of_conference': ''
               }
           ]

           for data in conference_data:
               Conference.objects.create(**data)

           self.stdout.write(self.style.SUCCESS('Successfully inserted conference data'))

           # Remove duplicates
           unique_entries = set()
           duplicates = []

           for conference in Conference.objects.all():
               identifier = (
                   conference.title_of_paper,
                   conference.title_of_conference,
                   conference.type,
                   conference.date_of_conference,
                   conference.organizing_institute,
                   conference.authors,
                   conference.location_of_conference,
                   conference.link_of_conference
               )
               if identifier in unique_entries:
                   duplicates.append(conference.id)
               else:
                   unique_entries.add(identifier)

           if duplicates:
               Conference.objects.filter(id__in=duplicates).delete()
               self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
           else:
               self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
