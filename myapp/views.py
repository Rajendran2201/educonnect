from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Attendance

def attendance(request):
    students = Student.objects.all()
    attendance_records = Attendance.objects.all().order_by('-date')  # Latest records first
    
    context = {
        'students': students,
        'attendance_records': attendance_records,
    }
    
    return render(request, 'attendance.html', context)

def index(request):
  return render(request, "index.html")

def login(request):
  return render(request, "login.html")

def contact(request):
  return render(request, "contact.html")

def eventbooking(request):
   return render(request, "eventbooking.html")