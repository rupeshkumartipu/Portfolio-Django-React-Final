from django.core.management.base import BaseCommand
from portfolio_app.models import Skill

class Command(BaseCommand):
    help = 'Inserts initial data into the Skill table'

    def handle(self, *args, **kwargs):
        skill_data = [
            {'name': 'Python', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'Django', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'ASP.NET Core', 'level': 'Intermediate', 'project_for_which_used': ''},
            {'name': 'MATLAB (Learning)', 'level': 'Beginner', 'project_for_which_used': ''},
            {'name': 'JavaScript', 'level': 'Intermediate', 'project_for_which_used': ''},
            {'name': 'Node.js', 'level': 'Intermediate', 'project_for_which_used': ''},
            {'name': 'Angular.js', 'level': 'Intermediate', 'project_for_which_used': ''},
            {'name': 'HTML', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'CSS', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'Machine Learning', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'Deep Learning', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'Natural Language Processing', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'Website Development (Full Stack)', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'Conventional Optimization', 'level': 'Intermediate', 'project_for_which_used': ''},
            {'name': 'Computational Optimization: PSO, GA, MOPSO, NSGA', 'level': 'Advanced', 'project_for_which_used': ''},
            {'name': 'Hyperparameters Optimization of ML models', 'level': 'Advanced', 'project_for_which_used': ''}
        ]

        for data in skill_data:
            Skill.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully inserted skill data'))
