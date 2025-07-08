from django.contrib.auth.models import User
from django.db import models

from api.validators import email_validator, only_letters


class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[only_letters])
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='doctor_profile'
    )
    name = models.CharField(max_length=100, validators=[only_letters])
    last_name = models.CharField(max_length=100, validators=[only_letters])
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.last_name} - {self.specialty.name}'


class Patient(models.Model):
    name = models.CharField(max_length=100, validators=[only_letters])
    last_name = models.CharField(max_length=100, validators=[only_letters])
    email = models.EmailField(unique=True, validators=[email_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    reason = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['doctor', 'date', 'time']

    def __str__(self):
        return f'{self.date} {self.time} - {self.doctor} with {self.patient}'
