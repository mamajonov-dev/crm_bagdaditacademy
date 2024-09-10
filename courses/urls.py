from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', all_courses, name='courses'),
    path('add-course/', add_course, name='add_course'),
    path('delete-course/<str:pk>/', delete_course, name='delete_course'),

    path('groups/', all_groups, name='groups'),
    path('add-group/', add_group, name='add_group'),

    path('group-detail/<str:pk>/', group_deatail, name='group_detail'),
    path('group-delete/<str:pk>/', delete_group, name='delete_group'),
    path('group-finish/<str:pk>/', end_group, name='end_group'),
    path('group-complete/<str:pk>/', complete_group, name='complete_group'),
    path('add-student-group/<str:student_pk>/<str:group_pk>/', add_student_to_group, name='add_student_to_group'),

]
