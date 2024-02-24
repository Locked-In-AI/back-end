from rest_framework import serializers
from .models import PersonalInfo, Education, Experience, Skill, Project, CV


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CVSerializer(serializers.ModelSerializer):
    personal_info = PersonalInfoSerializer()
    education = EducationSerializer(many=True, required=False)
    experience = ExperienceSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)

    class Meta:
        model = CV
        fields = '__all__'

    def create(self, validated_data):
        personal_info_data = validated_data.pop('personal_info', None)
        personal_info = PersonalInfoSerializer.create(PersonalInfoSerializer(),
                                                      validated_data=personal_info_data) if personal_info_data else None

        education_data = validated_data.pop('education', None)
        education = [EducationSerializer.create(EducationSerializer(), validated_data=edu) for edu in
                     education_data] if education_data else None

        experience_data = validated_data.pop('experience', None)
        experience = [ExperienceSerializer.create(ExperienceSerializer(), validated_data=exp) for exp in
                      experience_data] if experience_data else None

        skills_data = validated_data.pop('skills', None)
        skills = [SkillSerializer.create(SkillSerializer(), validated_data=skill) for skill in
                  skills_data] if skills_data else None

        projects_data = validated_data.pop('projects', None)
        projects = [ProjectSerializer.create(ProjectSerializer(), validated_data=project) for project in
                    projects_data] if projects_data else None

        cv = CV.objects.create(personal_info=personal_info, **validated_data)
        if education:
            cv.education.set(education)
        if experience:
            cv.experience.set(experience)
        if skills:
            cv.skills.set(skills)
        if projects:
            cv.projects.set(projects)
        return cv
