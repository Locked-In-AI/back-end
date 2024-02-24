from django.db import models
from django.conf import settings


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class CV(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE, related_name='cv')


class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    description = models.TextField()


class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    description = models.TextField()


class Skill(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=50)


class Project(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)