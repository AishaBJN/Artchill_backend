from django.db import models
from django.core.validators import FileExtensionValidator



class Canvas(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateField()

    
    def __str__(self):
        return self.title

class Track(models.Model):
    title =  models.CharField(max_length=50)
    artist = models.CharField(max_length=30)
    path = models.FileField( upload_to='audio_tracks/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])],
        help_text='Upload only MP3 files')
    
    def __str__(self):
        return f"{self.title} by {self.artist}"



# Create your models here.

 