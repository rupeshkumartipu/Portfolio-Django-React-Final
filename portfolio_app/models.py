from django.db import models


class Education(models.Model):
    sr_no = models.IntegerField()
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    result = models.CharField(max_length=50)
    year_of_passing = models.IntegerField()
    specialization = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.university}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)  # e.g., Beginner, Intermediate, Advanced
    project_for_which_used = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Experience(models.Model):
    sr_no = models.IntegerField()
    organization = models.CharField(max_length=100)
    positions_held = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    duration = models.CharField(max_length=50)
    key_responsibilities = models.TextField(blank=True)

    def __str__(self):
        return f"{self.positions_held} at {self.organization}"


class Publication(models.Model):
    sr_no = models.IntegerField()
    authors = models.CharField(max_length=300)
    publication_type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    year = models.IntegerField()
    publisher = models.CharField(max_length=200)
    indexing = models.CharField(max_length=200)
    impact_factor = models.FloatField()
    doi = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Patent(models.Model):
    sr_no = models.IntegerField()
    patent_title = models.CharField(max_length=200)
    inventors = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    application_number = models.CharField(max_length=100)
    publication_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.patent_title


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    granting_agency = models.CharField(max_length=200)
    amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name


class Award(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    date_awarded = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Conference(models.Model):
    title_of_paper = models.CharField(max_length=200)
    title_of_conference = models.CharField(max_length=200)
    type = models.CharField(max_length=50)  # e.g., National, International
    date_of_conference = models.DateField()
    organizing_institute = models.CharField(max_length=200)
    authors = models.CharField(max_length=300)
    location_of_conference = models.CharField(max_length=200)
    link_of_conference = models.URLField(blank=True)

    def __str__(self):
        return self.title_of_paper


class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    summary = models.TextField(blank=True)
    isbn_issn = models.CharField(max_length=100)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    platform_name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.platform_name


class AreaOfInterest(models.Model):
    interest = models.CharField(max_length=200)
    projects_done_in_this_area = models.TextField(blank=True)

    def __str__(self):
        return self.interest


class ResearchPublicationSummary(models.Model):
    publication_type = models.CharField(max_length=100)
    total = models.IntegerField()
    indexing = models.CharField(max_length=200)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.publication_type


class Workshop(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    date = models.DateField()
    organizer = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Seminar(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    date = models.DateField()
    organizer = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class STTP(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    date = models.DateField()
    organizer = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class DissertationGuided(models.Model):
    student_name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    level = models.CharField(max_length=50)  # e.g., B.Tech, M.Tech, PhD
    year = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name


class PersonalDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/')
    biography = models.TextField()
    professional_background = models.TextField()
    interests_hobbies = models.TextField()

    def __str__(self):
        return self.name
