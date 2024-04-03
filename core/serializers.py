from rest_framework import serializers
from .models import PersonalInfo, Education, Experience, Skill, Project, CV


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('degree', 'school_name', 'start_year', 'end_year', 'description')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('job_title', 'company_name', 'start_year', 'end_year', 'description')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('skill_name', 'skill_level')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name', 'description', 'start_year', 'end_year')


class CVSerializer(serializers.ModelSerializer):
    personal_info = PersonalInfoSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    education = EducationSerializer(many=True, required=False)
    experience = ExperienceSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        # TODO: fix this
        education_data = validated_data.pop('education')
        experience_data = validated_data.pop('experience')
        skill_data = validated_data.pop('skill')
        project_data = validated_data.pop('project')

        instance.education.set(Education.objects.filter(id__in=[item['id'] for item in education_data]))
        instance.experience.set(Experience.objects.filter(id__in=[item['id'] for item in experience_data]))
        instance.skill.set(Skill.objects.filter(id__in=[item['id'] for item in skill_data]))
        instance.project.set(Project.objects.filter(id__in=[item['id'] for item in project_data]))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


    class Meta:
        model = CV
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user

        if not user.is_authenticated:
            raise serializers.ValidationError("Authentication is required to create a CV.")

        personal_info_data = validated_data.pop('personal_info', None)
        personal_info_instance = self._create_personal_info(personal_info_data)

        cv_instance = CV.objects.create(
            personal_info=personal_info_instance,
            user=user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', '')
        )

        self._create_related_objects(cv_instance, 'education', Education, validated_data)
        self._create_related_objects(cv_instance, 'experience', Experience, validated_data)
        self._create_related_objects(cv_instance, 'skills', Skill, validated_data)
        self._create_related_objects(cv_instance, 'projects', Project, validated_data)

        return cv_instance

    def _create_personal_info(self, personal_info_data):
        if personal_info_data:
            return PersonalInfo.objects.create(**personal_info_data)
        return None

    def _create_related_objects(self, cv_instance, field_name, model_class, validated_data):
        related_data = validated_data.pop(field_name, [])
        related_objects = [model_class(cv=cv_instance, **data) for data in related_data]
        model_class.objects.bulk_create(related_objects)
