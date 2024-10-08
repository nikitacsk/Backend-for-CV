from rest_framework import serializers
from .models import PersonalDetails, Summary, Skills, WorkExperience, Education


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['summary']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['hard_skills', 'soft_skills', 'name_of_language', 'level_of_language', 'certification']


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['position', 'place_of_work', 'onboarding_date', 'offboarding_date', 'additional_information']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['educational_organisation', 'year_of_start', 'year_of_end',
                  'name_of_publication', 'date_of_publication', 'publication_link']


class PersonalDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalDetails
        fields = [
            'id',
            'photos_link', 'full_name', 'date_of_birth', 'gender', 'place_of_residence',
            'relocate', 'names_of_hobby', 'phone_number', 'email', 'social_media'
        ]


class CVDetailsSerializer(serializers.ModelSerializer):
    summary = SummarySerializer(many=False)
    skills = SkillsSerializer(many=False)
    work_experience = WorkExperienceSerializer(many=False)
    education = EducationSerializer(many=False)

    class Meta:
        model = PersonalDetails
        fields = [
            'id',
            'photos_link', 'full_name', 'date_of_birth', 'gender', 'place_of_residence',
            'relocate', 'names_of_hobby', 'phone_number', 'email', 'social_media',
            'summary', 'skills', 'work_experience', 'education'
        ]

    def create(self, validated_data):
        summary_data = validated_data.pop('summary')
        skills_data = validated_data.pop('skills')
        work_experience_data = validated_data.pop('work_experience')
        education_data = validated_data.pop('education')

        person = PersonalDetails.objects.create(**validated_data)

        Summary.objects.create(person=person, **summary_data)

        Skills.objects.create(person=person, **skills_data)

        WorkExperience.objects.create(person=person, **work_experience_data)

        Education.objects.create(person=person, **education_data)

        return person
