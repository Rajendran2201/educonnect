from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=50)
    roll_number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_number})"

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.name} - {self.date}: {self.status}"
