from django.db import models


class ApplicationStatus(models.TextChoices):
    APPLIED = 'applied'
    REJECTED = 'rejected'
    INTERVIEW = 'interview'
    OFFER = 'offer'
    GHOSTED = 'ghosted'
