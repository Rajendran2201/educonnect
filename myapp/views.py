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

def discussion_login(request):
   return render(request, "discussion_login.html")

def discussion_forum(request):
   return render(request, "discussion_forum.html")

def donate(request):
   return render(request, "donate.html")

def resources(request):
   return render(request, "resources.html")

def events(request):
   return render(request, "events.html")


def event1(request):
   return render(request, "event1.html")

def event2(request):
   return render(request, "event2.html")

def event3(request):
   return render(request, "event3.html")

def event4(request):
   return render(request, "event4.html")

def event5(request):
   return render(request, "event5.html")

def event6(request):
   return render(request, "event6.html")

def careerguidance(request):
   return render(request, "careerguidance.html")