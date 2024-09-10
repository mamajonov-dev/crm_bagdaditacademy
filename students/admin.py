from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', ]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'group', 'month', 'complete']
@admin.register(StudentCertificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['student', 'image']


