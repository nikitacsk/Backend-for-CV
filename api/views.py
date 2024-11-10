from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PersonalDetails
from .serializers import CVDetailsSerializer, PersonalDetailsSerializer, SummarySerializer, SkillsSerializer, \
                        WorkSerializer, EducationAndPublicationSerializer


class CVDetailsViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetails.objects.all()
    serializer_class = CVDetailsSerializer


class PersonalDetailsViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer


class SummaryViewSet(viewsets.ViewSet):
    serializer_class = SummarySerializer

    def get_object(self, person_id):
        try:
            return PersonalDetails.objects.get(id=person_id)
        except PersonalDetails.DoesNotExist:
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


class SkillsViewSet(viewsets.ViewSet):
    serializer_class = SkillsSerializer

    def get_object(self, person_id):
        try:
            return PersonalDetails.objects.get(id=person_id)
        except PersonalDetails.DoesNotExist:
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


class WorkExperienceViewSet(viewsets.ViewSet):
    serializer_class = WorkSerializer

    def get_object(self, person_id):
        try:
            return PersonalDetails.objects.get(id=person_id)
        except PersonalDetails.DoesNotExist:
            return None

    def get(self, request, person_id):
        work_experience = self.get_object(person_id)
        if work_experience is not None:
            serializer = self.serializer_class(work_experience)
            return Response(serializer.data)
        return Response({"error": "Work experience not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, person_id):
        work_experience = self.get_object(person_id)
        if work_experience is not None:
            serializer = self.serializer_class(work_experience, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Work experience not found."}, status=status.HTTP_404_NOT_FOUND)


class EducationViewSet(viewsets.ViewSet):
    serializer_class = EducationAndPublicationSerializer

    def get_object(self, person_id):
        try:
            return PersonalDetails.objects.get(id=person_id)
        except PersonalDetails.DoesNotExist:
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
