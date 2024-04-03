from rest_framework import serializers
from .models import JobApplication
from core.serializers import CVSerializer



class JobApplicationSerializer(serializers.Serializer):
    cv = CVSerializer(required=False)

    class Meta:
        model = JobApplication
        fields = (
            'company_name', 'job_title', 'cv', 'status', 'job_url', 'email', 'phone', 'website', 'notes', 'created_at',
            'updated_at')
        read_only_fields = ('created_at', 'updated_at')
