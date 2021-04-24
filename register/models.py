from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GenderChoices = (
    ('male', 'Male'),
    ('female', 'Female'),
)
YesNoChoices = (
    ("no", "No"),
    ('yes', 'Yes'),
)


class patient(models.Model):
    patient_name = models.CharField(max_length=256)
    Age = models.IntegerField()
    Gender = models.CharField(choices=GenderChoices, max_length=10)
    had_asthma_attack_in_the_last_year = models.CharField(
        choices=YesNoChoices, max_length=10)
    smoked_at_least_100_cigarettes_in_life = models.CharField(
        choices=YesNoChoices, max_length=10)
    spirometry_measure = models.CharField(max_length=100)
    blood_eosinophilis_count = models.CharField(max_length=200)

    def __str__(self):
        return str(self.patient_name)
