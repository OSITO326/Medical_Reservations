from django.contrib import admin

from api.models import Appointment, Doctor, Patient, Specialty

admin.site.register(Specialty)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
