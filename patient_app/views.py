from django.shortcuts import render
from form import Login_Page
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Appointment   #Import your Appointment model
from django.views.decorators.http import require_POST
from .models import LabReport

def landing_page(request):
    return render(request, 'index.html')

def usertype(request):
    return render(request, 'select_usertype.html')


def patient_login(request):
    form=Login_Page()
    if request.method=="POST":
        form=Login_Page(request.POST)
        if form.is_valid():
            print("validation succesfull....")
            print("Username:",form.cleaned_data['Username'])
            print("Password:",form.cleaned_data['Password'])
    return render(request,'patient_dashboard.html',{'form':form}) 

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def login(request):
    form=Login_Page()
    if request.method=="POST":
        form=Login_Page(request.POST)
        if form.is_valid():
            print("validation succesfull....")
            print("Username:",form.cleaned_data['Username'])
            print("Password:",form.cleaned_data['Password'])
    return render(request,'login.html',{'form':form}) 














# Create your views here.
def homepage(request):
    return render(request,"homepage.html")


def up_appointment(request):
    # Hardcoded doctor list (You can modify it as needed)
    doctors = [
        {'id': 1, 'name': 'Dr. James Carter - Cardiologist'},
        {'id': 2, 'name': 'Dr. Kelly Jarner - Dermatologist'},
        {'id': 3, 'name': 'Dr. Mike Wise - Therapist'},
    ]

    # upcoming_appointments = Appointment.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'appointments.html', {'doctors': doctors})
    # Render the home page with upcoming appointments if needed
   # upcoming_appointments = Appointment.objects.filter(date__gte=date.today()).order_by('date')
    # return render(request, 'appointments.html')

@require_POST
def book_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        
        # Create and save the appointment (assuming your Appointment model has these fields)
        appointment = Appointment(doctor_id=doctor_id, date=date, time=time)
        appointment.save()
        
        # Redirect to home page or show a success message
        return redirect('up_appointment')  # Replace 'home' with the URL name of your home view

    return HttpResponse("Invalid request", status=400)


def lab_reports_view(request):
    # Assuming the patient's username is stored in the session or passed in some way
    patient_username = request.session.get('patient_username')  # Adjust according to your logic
    
    if patient_username:
        reports = LabReport.objects.filter(patient_username=patient_username)
    else:
        reports = []
    
    return render(request, 'lab_reports.html', {'reports': reports})
