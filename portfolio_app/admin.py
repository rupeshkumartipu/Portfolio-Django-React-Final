from django.contrib import admin
from .models import Education, Skill, Experience, Publication, Patent, Project, Award, Conference, Book, SocialLink, \
    AreaOfInterest, ResearchPublicationSummary, Workshop, Seminar, STTP, DissertationGuided, PersonalDetail


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'degree', 'university', 'result', 'year_of_passing', 'specialization', 'description')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'project_for_which_used')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'sr_no', 'organization', 'positions_held', 'from_date', 'to_date', 'duration', 'key_responsibilities')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'sr_no', 'authors', 'publication_type', 'title', 'journal', 'year', 'publisher', 'indexing', 'impact_factor',
        'doi')


@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'patent_title', 'inventors', 'country', 'application_number', 'publication_date', 'status')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description', 'granting_agency', 'amount', 'start_date', 'end_date', 'status')


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'date_awarded', 'description')


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = (
        'title_of_paper', 'title_of_conference', 'type', 'date_of_conference', 'organizing_institute', 'authors',
        'location_of_conference', 'link_of_conference')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date', 'summary', 'isbn_issn', 'link')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'url')


@admin.register(AreaOfInterest)
class AreaOfInterestAdmin(admin.ModelAdmin):
    list_display = ('interest', 'projects_done_in_this_area')


@admin.register(ResearchPublicationSummary)
class ResearchPublicationSummaryAdmin(admin.ModelAdmin):
    list_display = ('publication_type', 'total', 'indexing', 'status')


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'date', 'organizer')


@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'date', 'organizer')


@admin.register(STTP)
class STTPAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'date', 'organizer')


@admin.register(DissertationGuided)
class DissertationGuidedAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'title', 'level', 'year', 'status')


@admin.register(PersonalDetail)
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'photo', 'biography', 'professional_background', 'interests_hobbies')

# Uncommenting these lines is not necessary since you have already registered the models with the admin site
# admin.site.register(Education)
# admin.site.register(Skill)
# admin.site.register(Experience)
# admin.site.register(Publication)
# admin.site.register(Patent)
# admin.site.register(Project)
# admin.site.register(Award)
# admin.site.register(Conference)
# admin.site.register(Book)
# admin.site.register(SocialLink)
# admin.site.register(AreaOfInterest)
# admin.site.register(ResearchPublicationSummary)
# admin.site.register(Workshop)
# admin.site.register(Seminar)
# admin.site.register(STTP)
# admin.site.register(DissertationGuided)
