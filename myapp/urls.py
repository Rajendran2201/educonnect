from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("/login", views.login, name="login"),
  path("/attendance", views.attendance, name="attendance"),
  path("/eventbooking", views.eventbooking, name="eventbooking"),
   path("/contact", views.contact, name="contact"),
]