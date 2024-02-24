from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalInfoViewSet, EducationViewSet, ExperienceViewSet, SkillViewSet, ProjectViewSet, CVViewSet

router = DefaultRouter()
router.register(r'personalinfo', PersonalInfoViewSet)
router.register(r'education', EducationViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'cv', CVViewSet)

urlpatterns = [
    path('', include(router.urls)),
]