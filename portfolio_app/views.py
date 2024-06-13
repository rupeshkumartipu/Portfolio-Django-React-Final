from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Education, Skill, Experience, Publication, Patent, Project, Award, Conference, Book, SocialLink, \
    AreaOfInterest, ResearchPublicationSummary, Workshop, Seminar, STTP, DissertationGuided, PersonalDetail
from .serializers import EducationSerializer, SkillSerializer, ExperienceSerializer, PublicationSerializer, \
    PatentSerializer, ProjectSerializer, AwardSerializer, ConferenceSerializer, BookSerializer, SocialLinkSerializer, \
    AreaOfInterestSerializer, ResearchPublicationSummarySerializer, WorkshopSerializer, SeminarSerializer, \
    STTPSerializer, DissertationGuidedSerializer, PersonalDetailSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', None)
        if query is not None:
            results = self.queryset.filter(
                degree__icontains=query
            )
        else:
            results = self.queryset.none()
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = [IsAuthenticated]


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    # permission_classes = [IsAuthenticated]


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    # permission_classes = [IsAuthenticated]


class PatentViewSet(viewsets.ModelViewSet):
    queryset = Patent.objects.all()
    serializer_class = PatentSerializer
    # permission_classes = [IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    # permission_classes = [IsAuthenticated]


class ConferenceViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    # permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]


class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    # permission_classes = [IsAuthenticated]


class AreaOfInterestViewSet(viewsets.ModelViewSet):
    queryset = AreaOfInterest.objects.all()
    serializer_class = AreaOfInterestSerializer
    # permission_classes = [IsAuthenticated]


class ResearchPublicationSummaryViewSet(viewsets.ModelViewSet):
    queryset = ResearchPublicationSummary.objects.all()
    serializer_class = ResearchPublicationSummarySerializer
    # permission_classes = [IsAuthenticated]


class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    # permission_classes = [IsAuthenticated]


class SeminarViewSet(viewsets.ModelViewSet):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer
    # permission_classes = [IsAuthenticated]


class STTPViewSet(viewsets.ModelViewSet):
    queryset = STTP.objects.all()
    serializer_class = STTPSerializer
    # permission_classes = [IsAuthenticated]


class DissertationGuidedViewSet(viewsets.ModelViewSet):
    queryset = DissertationGuided.objects.all()
    serializer_class = DissertationGuidedSerializer
    # permission_classes = [IsAuthenticated]


class PersonalDetailViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetail.objects.all()
    serializer_class = PersonalDetailSerializer
    # permission_classes = [IsAuthenticated]
