from rest_framework import serializers

from api.models import Appointment, Doctor, Patient, Specialty


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        if Appointment.objects.filter(
            doctor=data['doctor'], date=data['date'], time=data['time']
        ).exists():
            raise serializers.ValidationError('This appointment slot is already taken.')
        return data
