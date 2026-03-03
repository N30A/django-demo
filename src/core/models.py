from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image_name = models.CharField(max_length=100, default="no_hero.png")

    def __str__(self):
        return self.name