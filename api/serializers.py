from rest_framework import serializers
from .models import PersonalDetails, SocialMedia, Language, WorkExperience, Education, Publication


class SocialMediaWithIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'name_of_social_media', 'url']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['name_of_social_media', 'url']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name_of_language', 'level_of_language', 'certification']


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['position', 'place_of_work', 'onboarding_date', 'offboarding_date']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['educational_organisation', 'year_of_start', 'year_of_end']


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['name_of_publication', 'date_of_publication', 'publication_link']


class CVDetailsSerializer(serializers.ModelSerializer):
    social_media = SocialMediaSerializer(many=True, required=False)
    language = LanguageSerializer(many=True, required=False)
    work_experience = WorkExperienceSerializer(many=True, required=False)
    education = EducationSerializer(many=True, required=False)
    publication = PublicationSerializer(many=True, required=False)

    class Meta:
        model = PersonalDetails
        fields = [
            'id', 'photos_link', 'full_name', 'date_of_birth', 'gender', 'place_of_residence',
            'relocate', 'names_of_hobby', 'phone_number', 'email', 'summary', 'hard_skills',
            'soft_skills', 'social_media', 'language', 'work_experience', 'education', 'publication'
        ]

    def create(self, validated_data):
        social_media_data = validated_data.pop('social_media', [])
        language_data = validated_data.pop('language', [])
        work_experience_data = validated_data.pop('work_experience', [])
        education_data = validated_data.pop('education', [])
        publication_data = validated_data.pop('publication', [])

        person = PersonalDetails.objects.create(**validated_data)

        for social_media in social_media_data:
            SocialMedia.objects.create(person=person, **social_media)

        for language in language_data:
            Language.objects.create(person=person, **language)

        for work_experience in work_experience_data:
            WorkExperience.objects.create(person=person, **work_experience)

        for education in education_data:
            Education.objects.create(person=person, **education)

        for publication in publication_data:
            Publication.objects.create(person=person, **publication)

        return person

    def update(self, instance, validated_data):
        social_media_data = validated_data.pop('social_media', [])
        language_data = validated_data.pop('language', [])
        work_experience_data = validated_data.pop('work_experience', [])
        education_data = validated_data.pop('education', [])
        publication_data = validated_data.pop('publication', [])

        instance.photos_link = validated_data.get('photos_link', instance.photos_link)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.place_of_residence = validated_data.get('place_of_residence', instance.place_of_residence)
        instance.relocate = validated_data.get('relocate', instance.relocate)
        instance.names_of_hobby = validated_data.get('names_of_hobby', instance.names_of_hobby)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.hard_skills = validated_data.get('hard_skills', instance.hard_skills)
        instance.soft_skills = validated_data.get('soft_skills', instance.soft_skills)
        instance.save()

        instance.social_media.all().delete()
        instance.language.all().delete()
        instance.work_experience.all().delete()
        instance.education.all().delete()
        instance.publication.all().delete()

        for social_media in social_media_data:
            SocialMedia.objects.create(person=instance, **social_media)

        for language in language_data:
            Language.objects.create(person=instance, **language)

        for work in work_experience_data:
            WorkExperience.objects.create(person=instance, **work)

        for edu in education_data:
            Education.objects.create(person=instance, **edu)

        for pub in publication_data:
            Publication.objects.create(person=instance, **pub)

        return instance


class PersonalDetailsSerializer(serializers.ModelSerializer):
    social_media = SocialMediaSerializer(many=True, required=False)

    class Meta:
        model = PersonalDetails
        fields = [
            'id', 'photos_link', 'full_name', 'date_of_birth', 'gender', 'place_of_residence',
            'relocate', 'names_of_hobby', 'phone_number', 'email', 'social_media'
        ]

    def create(self, validated_data):
        social_media_data = validated_data.pop('social_media', [])

        person = PersonalDetails.objects.create(**validated_data)

        for social_media in social_media_data:
            SocialMedia.objects.create(person=person, **social_media)

        return person

    def update(self, instance, validated_data):
        social_media_data = validated_data.pop('social_media', [])

        instance.photos_link = validated_data.get('photos_link', instance.photos_link)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.place_of_residence = validated_data.get('place_of_residence', instance.place_of_residence)
        instance.relocate = validated_data.get('relocate', instance.relocate)
        instance.names_of_hobby = validated_data.get('names_of_hobby', instance.names_of_hobby)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        instance.social_media.all().delete()

        for social_media in social_media_data:
            SocialMedia.objects.create(person=instance, **social_media)

        return instance


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = ['photos_link', 'summary']


class SkillsSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True, required=False)

    class Meta:
        model = PersonalDetails
        fields = ['hard_skills', 'soft_skills', 'language']

    def update(self, instance, validated_data):
        language_data = validated_data.pop('language', [])

        instance.hard_skills = validated_data.get('hard_skills', instance.hard_skills)
        instance.soft_skills = validated_data.get('soft_skills', instance.soft_skills)
        instance.save()

        instance.language.all().delete()

        for language in language_data:
            Language.objects.create(person=instance, **language)

        return instance


class WorkSerializer(serializers.ModelSerializer):
    work_experience = WorkExperienceSerializer(many=True, required=False)

    class Meta:
        model = PersonalDetails
        fields = ['work_experience']

    def update(self, instance, validated_data):
        work_experience_data = validated_data.pop('work_experience', [])

        instance.work_experience.all().delete()

        for work_experience in work_experience_data:
            WorkExperience.objects.create(person=instance, **work_experience)

        return instance


class EducationAndPublicationSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=True, required=False)
    publication = PublicationSerializer(many=True, required=False)

    class Meta:
        model = PersonalDetails
        fields = ['education', 'publication']

    def update(self, instance, validated_data):
        education_data = validated_data.pop('education', [])
        publication_data = validated_data.pop('publication', [])

        instance.education.all().delete()
        instance.publication.all().delete()

        for education in education_data:
            Education.objects.create(person=instance, **education)

        for publication in publication_data:
            Publication.objects.create(person=instance, **publication)

        return instance
