from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Summary, Skills, WorkExperience, Education, PersonalDetails
from .serializers import SummarySerializer, SkillsSerializer, WorkExperienceSerializer, EducationSerializer, \
                        CVDetailsSerializer, PersonalDetailsSerializer


class PersonalDetailUpdateView(viewsets.ModelViewSet):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer


class SummaryDetailUpdateView(generics.GenericAPIView):
    serializer_class = SummarySerializer

    def get_object(self, person_id):
        try:
            return Summary.objects.get(person__id=person_id)
        except Summary.DoesNotExist:
            return None

    def get(self, request, person_id):
        summary = self.get_object(person_id)
        if summary is not None:
            serializer = self.serializer_class(summary)
            return Response(serializer.data)
        return Response({"error": "Summary not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, person_id):
        summary = self.get_object(person_id)
        if summary is not None:
            serializer = self.serializer_class(summary, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Summary not found."}, status=status.HTTP_404_NOT_FOUND)


class SkillsDetailUpdateView(generics.GenericAPIView):
    serializer_class = SkillsSerializer

    def get_object(self, person_id):
        try:
            return Skills.objects.get(person__id=person_id)
        except Skills.DoesNotExist:
            return None

    def get(self, request, person_id):
        skills = self.get_object(person_id)
        if skills is not None:
            serializer = self.serializer_class(skills)
            return Response(serializer.data)
        return Response({"error": "Skills not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, person_id):
        skills = self.get_object(person_id)
        if skills is not None:
            serializer = self.serializer_class(skills, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Skills not found."}, status=status.HTTP_404_NOT_FOUND)


class WorkExperienceDetailUpdateView(generics.GenericAPIView):
    serializer_class = WorkExperienceSerializer

    def get_object(self, person_id):
        try:
            return WorkExperience.objects.get(person__id=person_id)
        except WorkExperience.DoesNotExist:
            return None

    def get(self, request, person_id):
        work_experience = self.get_object(person_id)
        if work_experience is not None:
            serializer = self.serializer_class(work_experience)
            return Response(serializer.data)
        return Response({"error": "Work Experience not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, person_id):
        work_experience = self.get_object(person_id)
        if work_experience is not None:
            serializer = self.serializer_class(work_experience, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Work Experience not found."}, status=status.HTTP_404_NOT_FOUND)


class EducationDetailUpdateView(generics.GenericAPIView):
    serializer_class = EducationSerializer

    def get_object(self, person_id):
        try:
            return Education.objects.get(person__id=person_id)
        except Education.DoesNotExist:
            return None

    def get(self, request, person_id):
        education = self.get_object(person_id)
        if education is not None:
            serializer = self.serializer_class(education)
            return Response(serializer.data)
        return Response({"error": "Education not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, person_id):
        education = self.get_object(person_id)
        if education is not None:
            serializer = self.serializer_class(education, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Education not found."}, status=status.HTTP_404_NOT_FOUND)


class CVDetailsViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetails.objects.all()
    serializer_class = CVDetailsSerializer
