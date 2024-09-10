from django.urls import path
from .views import *

urlpatterns = [
    path('', all_teachers, name='all_teachers'),
    path('teacher-profile/<str:pk>/', teacher_profile, name='teacher_profile'),
    path('edit-teacher-profile/<str:pk>/', edit_teacher, name='edit_teacher'),
    path('add-teacher/', add_teacher, name='add_teacher'),

]