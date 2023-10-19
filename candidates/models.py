from django.db import models
from django.db.models import CheckConstraint, Q
from django.db.models.functions import Length

models.TextField.register_lookup(Length)
#manojbaddela-cbu-candidates-students-profile Models

class Skill(models.Model):
    skill = models.TextField(max_length=255, unique=True)

    def __str__(self):
        return self.skill

class Candidate(models.Model):
    #  Gender Input
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("NA", "Prefer Not To Say")
    )
    #  Resume Status
    RESUME_STATUS = (
        ("PENDING", "In Queue"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed")
    )

    full_name = models.TextField(max_length=255)
    aadhaar_id = models.TextField(max_length=16)
    dob = models.DateField()
    state = models.TextField(max_length=255)
    pin_code = models.TextField(max_length=10)
    gender = models.CharField(max_length=6, choices=GENDER)
    email = models.EmailField(max_length=254)
    primary_phone = models.TextField(max_length=15)
    other_phone = models.TextField(max_length=15, null=True)
    address = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    experience = models.IntegerField()
    resume_status = models.CharField(max_length=10, choices=RESUME_STATUS, default='PENDING')
    resume_path = models.TextField(null=True)
    #skills = models.ManyToManyField(Skill)

    # TODO: Add missing check constraints
    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(aadhaar_id__length=16),
                name='aadhaar_id_length'
            )
        ]

    def __str__(self):
        return self.full_name


class Specialization(models.Model):
    SPECIALIZATION = (
        ("Artificial Intelligence", "Artificial Intelligence"),
        ("Computer-Human Interface", "Computer-Human Interface"),
        ("Game Design", "Game Design"),
        ("Networks and Security", "Networks and Security"),
        ("Computer Graphics", "Computer Graphics"),
        ("Data Science", "Data Science"),
        ("Others", "Others")
    )

    specialization = models.TextField(max_length=255, choices=SPECIALIZATION, unique=True)

    def __str__(self):
        return self.specialization


class Institute(models.Model):
    INSTITUTE = (
        ("Institute 1", "Institute 1"),
        ("Institute 2", "Institute 2"),
        ("Institute 3", "Institute 3"),
        ("Institute 4", "Institute 4"),
        ("Institute 5", "Institute 5"),
        ("Institute 6", "Institute 6")
    )

    institute = models.TextField(max_length=255, choices=INSTITUTE, unique=True)

    def __str__(self):
        return self.institute


class Education(models.Model):
    candidate = models.ForeignKey(Candidate, null=True, on_delete=models.SET_NULL)
    specialization = models.ForeignKey(Specialization, null=True, on_delete=models.SET_NULL)
    institute = models.ForeignKey(Institute, null=True, on_delete=models.SET_NULL)
    board = models.TextField(max_length=255)
    level = models.TextField(max_length=16)
    year_of_passing = models.DateField()


# class CandidateSkills(models.Model):
#     candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
