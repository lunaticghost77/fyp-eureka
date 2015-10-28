from django.db import models

# Create your models here.
from django.utils import timezone

# Constants
IMG_WIDTH = 200
IMG_HEIGHT = 200

class Project(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=150)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    #img = models.ImageField(height_field=IMG_HEIGHT, width_field=IMG_WIDTH)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Student(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()


# class Team(models.Model):
#
