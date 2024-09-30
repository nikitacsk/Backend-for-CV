from django.db import models


class PersonalDetails(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=255, verbose_name="Full Name", blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="Gender", blank=False)
    date_of_birth = models.CharField(max_length=100, verbose_name="Date of Birth", blank=False)
    place_of_residence = models.CharField(max_length=255, verbose_name="Place of Residence", blank=True, null=True)
    relocate = models.BooleanField(verbose_name="Relocate", blank=False)
    names_of_hobby = models.CharField(max_length=255, verbose_name="Names of Hobby", blank=True, null=True)
    summary = models.TextField(verbose_name="Summary", blank=False)
    hard_skills = models.TextField(verbose_name="Hard Skills", blank=False)

    def __str__(self):
        return self.full_name


class Contacts(models.Model):
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number", blank=True, null=True)
    social_media = models.CharField(max_length=255, verbose_name="Social Media", blank=True, null=True)
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE,
                               verbose_name="Person", related_name="contacts")

    def __str__(self):
        return f"Contact for: {self.person.full_name} - {self.email or 'No Email'}"


class Education(models.Model):
    university = models.CharField(max_length=255, verbose_name="University", blank=True, null=True)
    courses = models.TextField(verbose_name="Courses", blank=True, null=True)
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE,
                               verbose_name="Person", related_name="education")

    def __str__(self):
        return self.university or self.courses or "No education"


class Publication(models.Model):
    title_of_publication = models.CharField(max_length=255, verbose_name="Title of Publication", blank=False)
    date = models.CharField(max_length=100, verbose_name="Date", blank=True, null=True)
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE,
                               verbose_name="Person", related_name="publications")

    def __str__(self):
        return self.title_of_publication


class ForeignLanguages(models.Model):
    language_name = models.CharField(max_length=255, verbose_name="Language Name", blank=False)
    level = models.CharField(max_length=100, verbose_name="Level", blank=False)
    certificate = models.CharField(max_length=255, verbose_name="Certificate", blank=True, null=True)
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE,
                               verbose_name="Person", related_name="foreign_languages")

    def __str__(self):
        return f"{self.language_name} - {self.level}"


class WorkExperience(models.Model):
    position = models.CharField(max_length=255, verbose_name="Position", blank=False)
    place_of_work = models.CharField(max_length=255, verbose_name="Place of Work", blank=False)
    onboarding_date = models.CharField(max_length=100, verbose_name="Onboarding Date", blank=False)
    offboarding_date = models.CharField(max_length=100, verbose_name="Offboarding Date", blank=True, default="-")
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE,
                               verbose_name="Person", related_name="work_experience")

    def __str__(self):
        return f"{self.position} at {self.place_of_work}"
