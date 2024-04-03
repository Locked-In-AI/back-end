from core.models import CV
from django.contrib import admin
from .models import JobApplication


class JobApplicationAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "cv":
            kwargs["queryset"] = CV.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(JobApplication, JobApplicationAdmin)
