import uuid
from django.db import models

from courses.models import Group
# Create your models here.

class Expenses(models.Model):
    others = models.IntegerField(blank=True, null=True)
    rent = models.IntegerField(blank=True, null=True)
    energy = models.IntegerField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                          unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def salary(self):
        amount = 0
        for i in Group.objects.all():
            amount += i.monthly_amount()
        return amount