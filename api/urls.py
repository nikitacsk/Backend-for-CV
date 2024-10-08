from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CVDetailsViewSet, SummaryDetailUpdateView, SkillsDetailUpdateView, WorkExperienceDetailUpdateView, \
                    EducationDetailUpdateView, PersonalDetailUpdateView


router = DefaultRouter()
router.register(r'cv-details', CVDetailsViewSet, basename='cv-details')
router.register(r'personal-details', PersonalDetailUpdateView, basename='personal-details')

urlpatterns = [
    path('', include(router.urls)),
    path('summary/<int:person_id>/', SummaryDetailUpdateView.as_view(), name='summary-detail-update'),
    path('skills/<int:person_id>/', SkillsDetailUpdateView.as_view(), name='skills-detail-update'),
    path('work-experience/<int:person_id>/', WorkExperienceDetailUpdateView.as_view(),
         name='work-experience-detail-update'),
    path('education/<int:person_id>/', EducationDetailUpdateView.as_view(), name='education-detail-update'),
]
