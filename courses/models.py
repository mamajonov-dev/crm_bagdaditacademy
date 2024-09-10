import uuid

from django.db import models
from teachers.models import Teacher

class Room(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    CHOISES = (
        ('8:00 - 10:00', '8:00 - 10:00'),
        ('10:00 - 12:00', '10:00 - 12:00'),
        ('12:00 - 14:00', '12:00 - 14:00'),
        ('14:00 - 16:00', '14:00 - 16:00'),
        ('16:00 - 18:00', '16:00 - 18:00'),
    )
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(default=200000, blank=True, null=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    continuity = models.IntegerField(default=1, blank=True, null=True)

    start = models.DateField(auto_created=True, blank=True, null=True)
    finish = models.DateField(auto_created=True, blank=True, null=True)

    room_time = models.CharField(choices=CHOISES, max_length=100,  blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def all_amount(self):
        all_price = self.continuity * len(self.student_set.all()) * self.amount
        return all_price

    def monthly_amount(self):
        m_price = len(self.student_set.all()) * self.amount
        return m_price

    def all_students(self):
        sutdents = len(self.student_set.all())
        return sutdents