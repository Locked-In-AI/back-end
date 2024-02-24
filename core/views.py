from rest_framework import viewsets
from .models import PersonalInfo, Education, Experience, Skill, Project, CV
from .serializers import PersonalInfoSerializer, EducationSerializer, ExperienceSerializer, SkillSerializer, \
    ProjectSerializer, CVSerializer


class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
