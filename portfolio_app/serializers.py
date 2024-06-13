from rest_framework import serializers
from .models import (
    Education, Skill, Experience, Publication, Patent, Project, Award, Conference, Book, SocialLink,
    AreaOfInterest, ResearchPublicationSummary, Workshop, Seminar, STTP, DissertationGuided, PersonalDetail
)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['sr_no', 'degree', 'university', 'result', 'year_of_passing', 'specialization', 'description']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'level', 'project_for_which_used']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['sr_no', 'organization', 'positions_held', 'from_date', 'to_date', 'duration', 'key_responsibilities']


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['sr_no', 'authors', 'publication_type', 'title', 'journal', 'year', 'publisher', 'indexing',
                  'impact_factor', 'doi']


class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = ['sr_no', 'patent_title', 'inventors', 'country', 'application_number', 'publication_date', 'status']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'granting_agency', 'amount', 'start_date', 'end_date', 'status']


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['title', 'organization', 'date_awarded', 'description']


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ['title_of_paper', 'title_of_conference', 'type', 'date_of_conference', 'organizing_institute',
                  'authors', 'location_of_conference', 'link_of_conference']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'publication_date', 'summary', 'isbn_issn', 'link']


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['platform_name', 'url']


class AreaOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaOfInterest
        fields = ['interest', 'projects_done_in_this_area']


class ResearchPublicationSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPublicationSummary
        fields = ['publication_type', 'total', 'indexing', 'status']


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ['title', 'venue', 'date', 'organizer']


class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields = ['title', 'venue', 'date', 'organizer']


class STTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = STTP
        fields = ['title', 'venue', 'date', 'organizer']


class DissertationGuidedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DissertationGuided
        fields = ['student_name', 'title', 'level', 'year', 'status']


class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        fields = '__all__'
