from django.core.management.base import BaseCommand
from portfolio_app.models import Education


class Command(BaseCommand):
    help = 'Inserts initial data into the Education table'

    def handle(self, *args, **kwargs):
        education_data = [
            {
                'sr_no': 1,
                'degree': 'Ph.D.',
                'university': 'CHARUSAT University Anand, Gujarat',
                'result': 'Awarded',
                'year_of_passing': 2024,
                'specialization': 'Structural Engineering (ML based Predictive Modelling)',
                'description': ''
            },
            {
                'sr_no': 2,
                'degree': 'M.Tech.',
                'university': 'MDU, Rohtak',
                'result': '74.81%',
                'year_of_passing': 2016,
                'specialization': 'Structural Engineering',
                'description': ''
            },
            {
                'sr_no': 3,
                'degree': 'B.Tech.',
                'university': 'MDU, Rohtak',
                'result': '69.66%',
                'year_of_passing': 2013,
                'specialization': 'Civil Engineering',
                'description': ''
            },
        ]

        for data in education_data:
            Education.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully inserted education data'))
