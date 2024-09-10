
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework import filters
from .serializers import *
from .models import *



class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

