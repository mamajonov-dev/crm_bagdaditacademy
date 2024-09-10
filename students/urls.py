from django.urls import path
from .views import *

urlpatterns = [
    path('', all_students, name='all_students'),
    path('student-profile/<str:pk>/', student_profile, name='student_profile'),
    path('delete-student/<str:pk>/', delete_student, name='delete_student'),
    path('edit-student/<str:pk>/', editStudent, name='edit_student'),

    path('add-student/', add_student, name='add_student'),
    path('payments/', students_payments, name='payments'),
    path('payment-for-student/<str:pk>/', pay_for_student, name='pay_for_student'),
    path('student-certificate/<str:pk>/' ,generate_certificate, name='student_certificate')
]