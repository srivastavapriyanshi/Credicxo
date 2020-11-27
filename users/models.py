from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=100)
    pic = models.ImageField(upload_to='Student/media/uploads',null=True,blank=True)
    roll_no = models.CharField(max_length=10,null=True,blank=True)
    age=models.PositiveIntegerField()
    std = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    contact = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    school_name = models.CharField(max_length=250,null=True,blank=True)
    father_name = models.CharField(max_length=50,null=True,blank=True)
    mother_name = models.CharField(max_length=50,null=True,blank=True)
    bus_facility = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.name+"-----"+self.std

    
