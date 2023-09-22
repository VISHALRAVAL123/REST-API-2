from django.shortcuts import render
from rest_framework import generics
from .models import Faculty,Subject,Student
from .serializers import Facultyserializer,Subjectserializer,Studentserializer
# Create your views here.
class FacultyList(generics.ListCreateAPIView):
    queryset=Faculty.objects.all()
    serializer_class=Facultyserializer

class FacultyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Faculty.objects.all()
    serializer_class=Facultyserializer

class SubjectList(generics.ListCreateAPIView):
    queryset=Subject.objects.all()
    serializer_class=Subjectserializer

class SubjectDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Subject.objects.all()
    serializer_class=Subjectserializer

class StudentList(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer