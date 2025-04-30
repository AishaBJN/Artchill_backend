from django.db import models


class Canva(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateField()

    
    def __str__(self):
        return self.title





# Create your models here.

 