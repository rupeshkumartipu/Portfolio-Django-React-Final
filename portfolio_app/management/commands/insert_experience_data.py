from django.core.management.base import BaseCommand
from portfolio_app.models import Experience
from datetime import date


class Command(BaseCommand):
    help = 'Inserts initial data into the Experience table'

    def handle(self, *args, **kwargs):
        experience_data = [
            {
                'sr_no': 1,
                'organization': 'K. R. Mangalam University, Gurugram, Haryana',
                'positions_held': 'Assistant Professor',
                'from_date': date(2023, 2, 15),
                'to_date': date.today(),  # Assuming "Till date" means the current date
                'duration': '1+ Year',
                'key_responsibilities': ''
            },
            {
                'sr_no': 2,
                'organization': 'CHARUSAT University, Changa (Anand), Gujarat',
                'positions_held': 'Research Scholar cum Teaching Assistant',
                'from_date': date(2019, 11, 5),
                'to_date': date(2022, 12, 31),
                'duration': '3 Years',
                'key_responsibilities': ''
            },
            {
                'sr_no': 3,
                'organization': 'BITS EDU CAMPUS, Vadodara, Gujarat',
                'positions_held': 'Assistant Professor',
                'from_date': date(2017, 8, 4),
                'to_date': date(2019, 5, 22),
                'duration': '1 Years, 9 Months',
                'key_responsibilities': ''
            },
            {
                'sr_no': 4,
                'organization': 'KJIT CAMPUS, Savli (Vadodara), Gujarat',
                'positions_held': 'Assistant Professor',
                'from_date': date(2016, 2, 1),
                'to_date': date(2017, 8, 3),
                'duration': '1 Years, 6 Months',
                'key_responsibilities': ''
            },
            {
                'sr_no': 5,
                'organization': 'DITMR, Faridabad, Delhi-NCR',
                'positions_held': 'Lecturer',
                'from_date': date(2013, 2, 1),
                'to_date': date(2014, 6, 1),
                'duration': '1 Years, 4 Months',
                'key_responsibilities': ''
            },
            {
                'sr_no': 6,
                'organization': 'CHARUSAT University, Changa (Anand), Gujarat',
                'positions_held': 'Structural Designer',
                'from_date': date(2019, 11, 5),
                'to_date': date(2022, 12, 31),
                'duration': '3 Years',
                'key_responsibilities': ''
            },
            {
                'sr_no': 7,
                'organization': 'IVRCL LTD.',
                'positions_held': 'Internship',
                'from_date': date(2013, 6, 15),
                'to_date': date(2013, 7, 30),
                'duration': '6 Weeks',
                'key_responsibilities': ''
            },
            {
                'sr_no': 8,
                'organization': 'AMRAPALI PRINCELY ESTATE PVT. LTD.',
                'positions_held': 'Internship',
                'from_date': date(2011, 6, 28),
                'to_date': date(2011, 8, 12),
                'duration': '6 Weeks',
                'key_responsibilities': ''
            }
        ]

        for data in experience_data:
            Experience.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully inserted experience data'))
