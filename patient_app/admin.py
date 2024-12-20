from django.contrib import admin
from patient_app.models import LabReport,Appointment
# Register your models here.
admin.site.register(Appointment)
admin.site.register(LabReport)