from django.contrib.gis.db import models

class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField()

    def __str__(self):
        return self.name
    
class WorldBorder1(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField()

    def __str__(self):
        return self.name