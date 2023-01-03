from django.db import models

# Create your models here.



# Create your models here.
class student_data(models.Model): #model is the parents class
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.name




class employee_data(models.Model): #model is the parents class
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    salary=models.IntegerField()
    H_education=models.CharField(max_length=60)

    def __str__(self):
        return self.name

class student(models.Model):
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)
    address = models.CharField(max_length=200)


