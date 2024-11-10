from django.db import models
from django.contrib.postgres.fields import ArrayField


class PersonalDetails(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    photos_link = models.URLField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=False)
    date_of_birth = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False)
    place_of_residence = models.CharField(max_length=255, blank=True, null=True)
    relocate = models.BooleanField(blank=False, default=False)
    names_of_hobby = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, default=list)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=False, unique=True, default='<EMAIL>')
    summary = models.TextField(blank=False, default="No summary")
    hard_skills = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    soft_skills = ArrayField(models.CharField(max_length=255), blank=True, default=list)

    def __str__(self):
        return self.full_name


class SocialMedia(models.Model):
    name_of_social_media = models.CharField(max_length=255)
    url = models.URLField()
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE, related_name='social_media')

    def __str__(self):
        return self.name_of_social_media


class Language(models.Model):
    name_of_language = models.CharField(max_length=255)
    level_of_language = models.CharField(max_length=255)
    certification = models.URLField(blank=True, null=True)
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE, related_name="language")

    def __str__(self):
        return f"Language for {self.person.full_name}"


class WorkExperience(models.Model):
    position = models.CharField(max_length=255, blank=True, null=True)
    place_of_work = models.CharField(max_length=255, blank=True, null=True)
    onboarding_date = models.CharField(max_length=100, blank=True, null=True)
    offboarding_date = models.CharField(max_length=100, blank=True, null=True, default="-")
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE, related_name="work_experience")

    def __str__(self):
        return f"Work Experience for {self.person.full_name}"


class Education(models.Model):
    educational_organisation = models.CharField(max_length=255, blank=True, null=True)
    year_of_start = models.IntegerField(blank=True, null=True, default='-')
    year_of_end = models.IntegerField(blank=True, null=True, default='-')
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE, related_name="education")

    def __str__(self):
        return f"Education for {self.person.full_name}"


class Publication(models.Model):
    name_of_publication = models.CharField(max_length=255, blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    publication_link = models.URLField(blank=True, null=True)
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE, related_name="publication")

    def __str__(self):
        return f"{self.person.full_name}s publication"

