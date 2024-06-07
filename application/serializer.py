from rest_framework import serializers
from .models import JobApplication
from core.serializers import CVSerializer


class JobApplicationSerializer(serializers.ModelSerializer):
    cv = CVSerializer(required=False)

    class Meta:
        model = JobApplication
        fields = (
            'company_name', 'job_title', 'cv', 'status', 'job_url', 'email', 'phone', 'website', 'notes', 'created_at',
            'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, attrs):
        cv = attrs.get('cv', None)
        request_user = self.context['request'].user
        if cv and cv.user != request_user:
            raise serializers.ValidationError("The CV is not owned by the requesting user.")
        return attrs
