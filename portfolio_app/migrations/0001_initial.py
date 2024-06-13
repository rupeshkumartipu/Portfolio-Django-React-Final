# Generated by Django 5.0.6 on 2024-06-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=200)),
                ('projects_done_in_this_area', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('date_awarded', models.DateField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('summary', models.TextField(blank=True)),
                ('isbn_issn', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_paper', models.CharField(max_length=200)),
                ('title_of_conference', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('date_of_conference', models.DateField()),
                ('organizing_institute', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=300)),
                ('location_of_conference', models.CharField(max_length=200)),
                ('link_of_conference', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DissertationGuided',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('level', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=50)),
                ('year_of_passing', models.IntegerField()),
                ('specialization', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('organization', models.CharField(max_length=100)),
                ('positions_held', models.CharField(max_length=100)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('duration', models.CharField(max_length=50)),
                ('key_responsibilities', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('patent_title', models.CharField(max_length=200)),
                ('inventors', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=100)),
                ('application_number', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('biography', models.TextField()),
                ('professional_background', models.TextField()),
                ('interests_hobbies', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('granting_agency', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('authors', models.CharField(max_length=300)),
                ('publication_type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('journal', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('publisher', models.CharField(max_length=200)),
                ('indexing', models.CharField(max_length=200)),
                ('impact_factor', models.FloatField()),
                ('doi', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchPublicationSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_type', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
                ('indexing', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('organizer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=50)),
                ('project_for_which_used', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='STTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('organizer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('organizer', models.CharField(max_length=200)),
            ],
        ),
    ]
