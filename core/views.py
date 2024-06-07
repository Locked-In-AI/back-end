from django.shortcuts import get_list_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PersonalInfo, Education, Experience, Skill, Project, CV
from .permissions import AdminOrOwnerPermission
from .serializers import PersonalInfoSerializer, EducationSerializer, ExperienceSerializer, SkillSerializer, \
    ProjectSerializer, CVSerializer


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
    permission_classes = (AdminOrOwnerPermission,)

    def get_queryset(self):
        user = self.request.user
        return CV.objects.filter(user=user)


class OptimizeCVViewSet(APIView):
    permission_classes = (AdminOrOwnerPermission,)

    def post(self, request, *args, **kwargs):
        description = request.data.get('description', "")

        if not description:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)
        processed_description = self.optimize_description(description)
        return Response({"processed_description": processed_description}, status=status.HTTP_200_OK)

    def optimize_description(self, description):
        return description.upper()
