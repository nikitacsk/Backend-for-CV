from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CVDetailsViewSet, PersonalDetailsViewSet, SummaryViewSet, SkillsViewSet, WorkExperienceViewSet, \
                    EducationViewSet

router = DefaultRouter()
router.register(r'cv-details', CVDetailsViewSet, basename='cv-details')
router.register(r'personal-details', PersonalDetailsViewSet, basename='personal-details')


urlpatterns = [
    path('', include(router.urls)),
    path('summary/<int:person_id>/', SummaryViewSet.as_view({'get': 'get', 'put': 'put'})),
    path('skills/<int:person_id>/', SkillsViewSet.as_view({'get': 'get', 'put': 'put'})),
    path('work-experience/<int:person_id>/', WorkExperienceViewSet.as_view({'get': 'get', 'put': 'put'})),
    path('education/<int:person_id>/', EducationViewSet.as_view({'get': 'get', 'put': 'put'})),
]
