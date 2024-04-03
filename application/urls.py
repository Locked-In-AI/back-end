from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobApplicationModelViewSet

router = DefaultRouter()
router.register(r'job-application', JobApplicationModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]