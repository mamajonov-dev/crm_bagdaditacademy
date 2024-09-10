import uuid

from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def oylik(self):
        groups = self.group_set.all()
        all_students = 0
        summa = 0
        for group in groups:
            all_students += group.all_students()
            for student in group.student_set.filter(finish=False):
                summa += group.amount * 1
        summa = summa / 2
        return summa

    def all_summa(self):
        groups = self.group_set.all()
        all_students = 0
        summa = 0
        for group in groups:
            all_students += group.all_students()
            for student in group.student_set.filter(finish=False):
                summa += group.amount * 1
        return summa


    def teacher_students(self):
        groups = self.group_set.all()
        all_students = 0
        summa = 0
        for group in groups:
            all_students += group.all_students()
            for student in group.student_set.filter(finish=False):
                summa += group.amount * 1
        return  all_students

