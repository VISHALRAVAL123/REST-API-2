from django.db import models

# Create your models here.
class Faculty(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.PositiveIntegerField()
    subject=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name=models.CharField(max_length=100)
    choch=models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name='subjects')

    def __str__(self):
        return self.name

class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone=models.PositiveIntegerField()
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True,blank=True)
    subjects=models.ManyToManyField(Subject)

    def __str__(self):
        return self.fname+""+self.subject+""+self.faculty
