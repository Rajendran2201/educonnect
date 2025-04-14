from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("/login", views.login, name="login"),
  path("/attendance", views.attendance, name="attendance"),
  path("/eventbooking", views.eventbooking, name="eventbooking"),
  path("/contact", views.contact, name="contact"),
  path("/donate", views.donate, name="donate"),
  path("/resources", views.resources, name="resources"),
  path("/events", views.events, name="events"),
  path("/event1", views.event1, name="event1"),
  path("/event2", views.event2, name="event2"),
  path("/event3", views.event3, name="event3"),
  path("/event4", views.event4, name="event4"),
  path("/event5", views.event5, name="event5"),
  path("/event6", views.event6, name="event6"),
  path("/careerguidance", views.careerguidance, name="careerguidance"),
  path("/discussion_login", views.discussion_login, name="discussion_login"),
  path("/discussion_forum", views.discussion_forum, name="discussion_forum"),
]