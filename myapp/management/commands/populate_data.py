import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from myapp.models import Student, Attendance

class Command(BaseCommand):
    help = "Populate the database with 25 Tamil student names and attendance records"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating students and attendance records...")

        # Tamil student names (in English)
        tamil_student_names = [
            "Arun", "Chandra", "Krishna", "Murugan", "Kesavan", "Nandini", "Anitha", "Siva",
            "Ragu", "Pavithra", "Deepa", "Logesh", "Ranjani", "Gautham", "Sujitha", "Mohan", "Vinoth",
            "Ramya", "Manikandan", "Naresh", "Priya", "Chandran", "Jayalakshmi", "Durga", "Ganesh"
        ]
        classes = ["Grade 6", "Grade 7", "Grade 8"]

        # Create 25 students
        students = []
        for i in range(1, 26):
            student = Student.objects.create(
                name=random.choice(tamil_student_names),
                class_name=random.choice(classes),
                roll_number=i
            )
            students.append(student)

        # Generate attendance for the past 3 months
        today = datetime.today()
        for student in students:
            for days_ago in range(90):  # Last 3 months
                date = today - timedelta(days=days_ago)
                status = random.choice(["Present", "Absent"])
                Attendance.objects.create(student=student, date=date, status=status)

        self.stdout.write(self.style.SUCCESS("Successfully populated 25 Tamil students and attendance records!"))
