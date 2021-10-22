from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=154)
    
    GENDER = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    gender = models.CharField(max_length=50, choices=GENDER)
    number = models.CharField(max_length=50)
    path = models.CharField(max_length=50)

    PATH = (
        ("AWS-DevOps" , "AWS-DevOps"),
        ("Full Stack" , "Full Stack"),
        ("Data Science" , "Data Science"),
            )
      
    
    path = models.CharField(max_length=50, choices=PATH)
    # register_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.full_name} - {self.number}"