from rest_framework import viewsets

from api.models import Appointment, Doctor, Patient, Specialty
from api.serializers import (
    AppointmentSerializer,
    DoctorSerializer,
    PatientSerializer,
    SpecialtySerializer,
)


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # def perform_create(self, serializer):
    #     serializer.save()
    #
    # def perform_update(self, serializer):
    #     serializer.save()
