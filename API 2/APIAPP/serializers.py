from rest_framework import serializers
from .models import Faculty,Subject,Student

class Facultyserializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields='__all__'

class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'
        
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'  

    