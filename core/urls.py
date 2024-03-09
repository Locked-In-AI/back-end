from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (CVViewSet,
                    OptimizeCVViewSet)

router = DefaultRouter()
router.register(r'cv', CVViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('optimize/', OptimizeCVViewSet.as_view(), name='optimize-cv'),
]
