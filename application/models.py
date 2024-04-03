from django.db import models
from core.models import CV
from .choice import ApplicationStatus


class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    cv = models.ForeignKey(CV, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=ApplicationStatus.choices, default=ApplicationStatus.APPLIED)
    job_url = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    website = models.URLField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.job_title} at {self.company_name}'
