from django.db import models
from django.utils.timezone import now
import random
from django.utils import timezone
from django.db import models
from django.utils.timezone import now, timedelta

class TeacherOTP(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return now() > self.created_at + timedelta(minutes=10)

    def __str__(self):
        return f"{self.email} - {self.otp}"



# ----------------- TEACHER MODEL -----------------
class Teacher(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    student_default_pass = models.CharField(max_length=30)

    def __str__(self):
        return self.username


# ----------------- STUDENT MODEL -----------------
class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    class Meta:
        unique_together = ('teacher', 'roll_no')



# ----------------- SUBJECT MODEL -----------------
class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


# ----------------- ATTENDANCE MODEL -----------------
class Attendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)   # Present / Absent

    def __str__(self):
        return f"{self.student.name} - {self.date}"


# ----------------- MARKS MODEL -----------------
class Marks(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}"
