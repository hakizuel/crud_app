from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField()
    gender = models.CharField(max_length=7)
    grade = models.CharField(max_length=2)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.first_name