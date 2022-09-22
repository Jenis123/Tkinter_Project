from django.db import models


class employee(models.Model):
    no = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20, unique = False)
    lname = models.CharField(max_length=20)
    gender = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.fname
     
class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    phone_no = models.IntegerField()
    password = models.CharField(max_length=8)   

    def __str__(self):
        return self.username

hobbies_choices = (('reading','reading'),('writing','writing'),('music','music'))



class uniq(models.Model):
    uniq_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    phone_no = models.IntegerField()
    gender = models.CharField(max_length=200)

    department = models.CharField(max_length=200)
    

    def __str__(self):
        return self.username