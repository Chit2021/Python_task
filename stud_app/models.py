from django.db import models

# Create your models here.

class Student_Info(models.Model):
    
    Student_Name = models.CharField(max_length=40)
    Student_School = models.CharField(max_length=40)
    Student_RollNo = models.IntegerField()
    Student_Std = models.IntegerField()
    Location = models.CharField(max_length=30)

    def __str__(self):
        return self.Student_Name

