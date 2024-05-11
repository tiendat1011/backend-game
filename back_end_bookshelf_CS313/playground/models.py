from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)
    about_game = models.TextField()
    gameplay = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video = models.TextField()
