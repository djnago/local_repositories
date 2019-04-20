from django.db import models
from multiselectfield import MultiSelectField

class RegistrationData(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)

    GENDER_CHOICES=(
        ('F','Female'),
        ('M','Male')
    )
    gender = models.CharField(max_length=10, choices= GENDER_CHOICES)

    LOCATION_CHOICES=(
        ('Hyd','Hyderabad'),
        ('Bang','Bangalore'),
        ('Chen','Chennai'),
        ('Mum','Mumbai')
    )
    locations = MultiSelectField(max_length=20, choices=LOCATION_CHOICES)

from django.db import models
class Feedbackdata(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    time = models.DateTimeField()
    feedback = models.CharField(max_length=500)


class StudentData(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=30)

    Shift_Choices=(
        ('Morning','Morning'),
        ('Afternoon','Afternoon'),
        ('Evening','Evening')
    )
    shift = MultiSelectField(max_length=100, choices=Shift_Choices)

    Course_Choices = (
        ('Python','Python'),
        ('Django','Django'),
        ('MySQL','MySQL'),
        ('Oracle','Oracle'),
        ('MSBI','MSBI'),
        ('REST API','REST API')
    )
    course = MultiSelectField(max_length=400, choices=Course_Choices)

    Faculty_Choices = (
        ('Nani','Nani'),
        ('Sai','Sai'),
        ('Raju','Raju'),
        ('Satya','Satya'),
        ('Rajesh','Rajesh')
    )
    faculty = MultiSelectField(max_length=500, choices=Faculty_Choices)

    Branch_Choices=(
        ('Branch-1','Branch-1'),
        ('Branch-2','Branch-2'),
        ('Branch-3','Branch-3'),
    )
    brance = MultiSelectField(max_length=500, choices=Branch_Choices)