# portfolio_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EducationViewSet, SkillViewSet, ExperienceViewSet, PublicationViewSet,
    PatentViewSet, ProjectViewSet, AwardViewSet, ConferenceViewSet, BookViewSet,
    SocialLinkViewSet, AreaOfInterestViewSet, ResearchPublicationSummaryViewSet,
    WorkshopViewSet, SeminarViewSet, STTPViewSet, DissertationGuidedViewSet, PersonalDetailViewSet
)

router = DefaultRouter()
router.register(r'educations', EducationViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'patents', PatentViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'conferences', ConferenceViewSet)
router.register(r'books', BookViewSet)
router.register(r'sociallinks', SocialLinkViewSet)
router.register(r'areasofinterest', AreaOfInterestViewSet)
router.register(r'researchpublicationsummaries', ResearchPublicationSummaryViewSet)
router.register(r'workshops', WorkshopViewSet)
router.register(r'seminars', SeminarViewSet)
router.register(r'sttps', STTPViewSet)
router.register(r'dissertationsguided', DissertationGuidedViewSet)
router.register(r'personaldetails', PersonalDetailViewSet)  # New endpoint

urlpatterns = [
    path('', include(router.urls)),
]
