from django.contrib import admin
from .models import PersonalInfo, Education, Experience, Skill, Project, CV


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline, SkillInline, ProjectInline]
    list_display = [field.name for field in CV._meta.fields]
