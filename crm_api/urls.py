from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('api-student', StudentView)
router.register('api-teacher', TeacherView)
router.register('api-group', GroupView)

urlpatterns = [
    path('', include(router.urls)),
]
