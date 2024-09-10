from django.contrib import admin
from .models import *


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ('name','image')
