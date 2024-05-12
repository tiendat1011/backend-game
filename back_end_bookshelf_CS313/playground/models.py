from django.db import models
from datetime import datetime


class CustomDateField(models.DateField):
    def to_python(self, value):
        if isinstance(value, datetime):
            return value
        if value:
            return datetime.strptime(value, '%B %d, %Y').date()
        return None


class GameDetail(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=200, null=True)
    image = models.URLField()
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    genres = models.CharField(max_length=200)
    operating_systems = models.CharField(max_length=100)
    date_released = CustomDateField()

    def __str__(self):
        return self.name
    

class GameInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    about_game = models.TextField()
    gameplay = models.TextField(null=True)
    price = models.FloatField(null=True)
    video = models.URLField()

    def __str__(self):
        return self.name
    
    
