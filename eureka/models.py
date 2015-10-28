from django.db import models

# Create your models here.

# Constants
IMG_WIDTH = 200
IMG_HEIGHT = 200

class Project(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=150)
    created_date = models.DateField(auto_now_add=True)
    img = models.ImageField(height_field=IMG_HEIGHT, width_field=IMG_WIDTH)

class Student(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()


# class Team(models.Model):
#
