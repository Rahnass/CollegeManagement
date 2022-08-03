from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=100)
    course_fee=models.IntegerField()

class student(models.Model):
     course=models.ForeignKey(course, on_delete=models.CASCADE,null=True)   
     student_name=models.CharField(max_length=100)
     student_address=models.CharField(max_length=100)
     student_age=models.IntegerField()
     joining_date=models.DateField()

class UserMember(models.Model):
     user_course=models.ForeignKey(course, on_delete=models.CASCADE,null=True)   
     user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)   
     user_address = models.CharField(max_length=100)
     user_gender=models.CharField(max_length=100)
     user_contact=models.IntegerField()
     user_image=models.ImageField(upload_to='images/',blank=True, null=False, default='images/dp.png')     


class stdcrs(models.Model):
     student_name=models.CharField(max_length=100)
     student_address=models.CharField(max_length=100)
     student_age=models.IntegerField()
     joining_date=models.DateField() 
     course_name=models.CharField(max_length=100)
     course_fee=models.IntegerField()    

class teacher(models.Model):      
     first_name=models.CharField(max_length=50)
     last_name=models.CharField(max_length=50)
     user_address = models.CharField(max_length=100)
     user_gender=models.CharField(max_length=100)
     user_contact=models.IntegerField()
     user_image=models.ImageField(upload_to='images/',blank=True, null=False, default='images/dp.png')

     
     
   


  
          