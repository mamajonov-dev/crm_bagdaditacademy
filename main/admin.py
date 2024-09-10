from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('salary', 'month')