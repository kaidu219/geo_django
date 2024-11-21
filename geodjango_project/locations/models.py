from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    point = models.PointField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Search_city(models.Model):
    city_name = models.CharField(max_length=100)
    point = models.PointField()
    point = models.PointField()
    search_query = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name