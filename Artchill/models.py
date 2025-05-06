from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import base64


class Canvas(models.Model):
    title = models.CharField(max_length=50, default="Untitled")
    create_at = models.DateField(auto_now_add=True)
    image_data = models.TextField(default="")

    
    def __str__(self):
        return self.title

class Track(models.Model):
    title =  models.CharField(max_length=50)
    artist = models.CharField(max_length=30)
    path = models.FileField(max_length=200)
    
    def __str__(self):
        return f"{self.title} by {self.artist}"

class Notes(models.Model):
    content = models.TextField(max_length=500,blank=False)








# Create your models here.

 