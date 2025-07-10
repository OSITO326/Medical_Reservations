from collections import defaultdict
from datetime import date
from django.http import request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def appointment_schedule_view(request):
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return Response({'detail': 'Not linked to a doctor profile.'}, status=403)

    appointments = Appointment.objects.filter(
        doctor=doctor, date__gte=date.today()
    ).order_by('date', 'time')

    schedule = defaultdict(list)
    for app in appointments:
        schedule[app.date].append({'time': app.time, 'patient_name': app.patient.name})

    data = [{'date': d, 'appointments': a} for d, a in schedule.items()]
    return Response(data)
