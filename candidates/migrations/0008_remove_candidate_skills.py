# Generated by Django 5.0.dev20230916185426 on 2023-09-23 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0007_alter_education_candidate_alter_education_institute_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='skills',
        ),
    ]
