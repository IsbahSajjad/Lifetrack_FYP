# from django.db import models

# # Create your models here.
# class Appointment(models.Model):
#     doctor = models.ForeignKey( on_delete=models.CASCADE)  # Assuming you have a Doctor model
#     date = models.DateField()
#     time = models.TimeField()

#     def __str__(self):
#         return f"{self.doctor} - {self.date} {self.time}"
    
from django.db import models

class Appointment(models.Model):
    doctor_id = models.IntegerField()  # Use IntegerField to store the doctor ID
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Appointment with Doctor ID {self.doctor_id} on {self.date} at {self.time}"
    
class LabReport(models.Model):
    patient_username = models.CharField(max_length=150)  # Assuming you identify patients by username
    report_file = models.FileField(upload_to='lab_reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lab Report for {self.patient_username} on {self.created_at}"


