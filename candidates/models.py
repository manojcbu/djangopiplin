from django.db import models
from django.db.models import CheckConstraint, Q
from django.db.models.functions import Length

models.TextField.register_lookup(Length)

# Choices for Gender Input
GENDER = (
    ("M", "Male"),
    ("F", "Female"),
    ("NA", "Prefer Not To Say")
)

RESUME_STATUS = (
    ("PENDING", "In Queue"),
    ("SUCCESS", "Success"),
    ("FAILED", "Failed")
)


class Candidate(models.Model):
    full_name = models.TextField(max_length=255)
    aadhaar_id = models.TextField(max_length=16)
    dob = models.DateField()
    state = models.TextField(max_length=255)
    pin_code = models.TextField(max_length=10)
    gender = models.CharField(max_length=3, choices=GENDER)
    email = models.EmailField(max_length=254)
    primary_phone = models.TextField(max_length=15)
    other_phone = models.TextField(max_length=15)
    address = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    experience = models.IntegerField()
    resume_status = models.CharField(max_length=10, choices=RESUME_STATUS)
    resume_path = models.TextField()

    # TODO: Add missing check constraints
    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(aadhaar_id__length=16),
                name='aadhaar_id_length'
            )
        ]


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
