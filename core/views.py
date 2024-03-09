from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import AdminOrOwnerPermission

from .models import PersonalInfo, Education, Experience, Skill, Project, CV
from .serializers import PersonalInfoSerializer, EducationSerializer, ExperienceSerializer, SkillSerializer, \
    ProjectSerializer, CVSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.models import User


class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = (AdminOrOwnerPermission,)


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (AdminOrOwnerPermission,)


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (AdminOrOwnerPermission,)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (AdminOrOwnerPermission,)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AdminOrOwnerPermission,)


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    #permission_classes = (AdminOrOwnerPermission,)

    def get_queryset(self):
        return get_list_or_404(CV, user=self.request.user) if self.request.user else None


class OptimizeCVViewSet(APIView):

    def post(self, request, *args, **kwargs):
        description = request.data.get('description', "")

        if not description:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)
