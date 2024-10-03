from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalDetailsViewSet

router = DefaultRouter()
router.register(r'personal-details', PersonalDetailsViewSet, basename='personal-details')

urlpatterns = [
    path('', include(router.urls)),
]
