from django.core.management.base import BaseCommand
from portfolio_app.models import AreaOfInterest

class Command(BaseCommand):
    help = 'Inserts initial data into the AreaOfInterest table'

    def handle(self, *args, **kwargs):
        area_of_interest_data = [
            {
                'interest': 'Currently Teaching and Mentoring B. Tech. (CSE) and MCA students',
                'projects_done_in_this_area': ''
            },
            {
                'interest': 'Subjects Taught/Teaching (CSE): Python Language, Natural Language Processing, Machine Learning, Deep Learning, Web programming using Python and JavaScript including HTML, CSS, SASS, Git, GitHub etc.',
                'projects_done_in_this_area': ''
            },
            {
                'interest': 'Subjects Taught/Teaching (Civil Engineering): Structural Design, Structural Analysis, Soil Mechanics, Transportation Engineering, Concrete Technology, and Surveying.',
                'projects_done_in_this_area': ''
            },
            {
                'interest': 'Civil engineering software skills: Staad Pro, ETABS, AutoCAD, 3ds Max.',
                'projects_done_in_this_area': ''
            },
            {
                'interest': 'Designed many buildings as structural design engineer.',
                'projects_done_in_this_area': ''
            },
            {
                'interest': 'Corporate Member of The Institution of Engineers (India) [IEI]',
                'projects_done_in_this_area': ''
            }
        ]

        for data in area_of_interest_data:
            AreaOfInterest.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully inserted area of interest data'))
