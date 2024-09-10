import uuid

from django.db import models
from courses.models import Course, Group, Room

class Student(models.Model):
    CHOISES = (
        ('8:00 - 10:00', '8:00 - 10:00'),
        ('10:00 - 12:00', '10:00 - 12:00'),
        ('12:00 - 14:00', '12:00 - 14:00'),
        ('14:00 - 16:00', '14:00 - 16:00'),
        ('16:00 - 18:00', '16:00 - 18:00'),
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    student_time = models.CharField(max_length=200, choices=CHOISES, blank=True, null=True)

    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(default=998, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    finish = models.BooleanField(default=False, blank=True, null=True)
    # sertifcateid = models.IntegerField(default=True, auto_created=True, editable=False, blank=True, null=True)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=True, null=True)
    month = models.CharField(max_length=100, blank=True, null=True)
    sale = models.IntegerField(default=0, blank=True, null=True)
    payment_check = models.ImageField(upload_to='payment_cheks/', blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True)

    complete = models.BooleanField(default=False, blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.name

    class Meta:
        ordering = ['month']


class StudentCertificate(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    # sertifcateid = models.IntegerField(auto_created=True, editable=False, primary_key=True, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    # def __str__(self):
    #     return self.student.name