from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import JobApplication
from .serializer import JobApplicationSerializer


class JobApplicationModelViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]
