# Generated by Django 5.1.1 on 2024-10-09 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_university_education_educational_organisation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='additional_information',
        ),
    ]
