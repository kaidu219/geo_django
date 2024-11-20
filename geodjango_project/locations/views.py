from django.shortcuts import render
from .models import WorldBorder
from django.contrib.gis.geos import Point

def home(request):

    point = Point(37.6173, 55.7558)  # Москва
 
    WorldBorder.objects.create(
        name="Test Point",
        location=point
    )

    points = WorldBorder.objects.all()
    return render(request, 'locations/home.html', {'points': points})