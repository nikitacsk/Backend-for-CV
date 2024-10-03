from django.db import models


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
    names_of_hobby = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=False, unique=True, default='<EMAIL>')
    social_media = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name


class Summary(models.Model):
    summary = models.TextField(verbose_name="Summary", blank=False)
    person = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE, related_name="summary")

    def __str__(self):
        return f"Summary for {self.person.full_name}"


class Skills(models.Model):
    hard_skills = models.CharField(max_length=255)
    soft_skills = models.CharField(max_length=255)
    name_of_language = models.CharField(max_length=255)
    level_of_language = models.CharField(max_length=255)
    certification = models.URLField(blank=True, null=True)
    person = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return f"Skills for {self.person.full_name}"


class WorkExperience(models.Model):
    position = models.CharField(max_length=255, blank=True, null=True)
    place_of_work = models.CharField(max_length=255, blank=True, null=True)
    onboarding_date = models.CharField(max_length=100, blank=True, null=True)
    offboarding_date = models.CharField(max_length=100, blank=True, null=True, default="-")
    additional_information = models.CharField(max_length=255, blank=True, null=True)
    person = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE, related_name="work_experience")

    def __str__(self):
        return f"Work Experience for {self.person.full_name}"


class Education(models.Model):
    university = models.CharField(max_length=255, blank=True, null=True)
    year_of_start = models.IntegerField(blank=True, null=True)
    year_of_end = models.IntegerField(blank=True, null=True)
    name_of_publication = models.CharField(max_length=255, blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    publication_link = models.URLField(blank=True, null=True)
    person = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE, related_name="education")

    def __str__(self):
        return f"Education for {self.person.full_name}"
