from django.contrib import admin
from .models import *


@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = ('name',)
