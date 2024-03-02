from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalInfoViewSet, EducationViewSet, ExperienceViewSet, SkillViewSet, ProjectViewSet, CVViewSet, \
    UserCVViewSet

router = DefaultRouter()
router.register(r'cv', CVViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('user-cv/<str:username>/', UserCVViewSet.as_view({'get': 'list'}), name='user-cv-list'),
]