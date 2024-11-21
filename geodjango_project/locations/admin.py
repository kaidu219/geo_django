from django.contrib.gis import admin
from .models import Location, Search_city

@admin.register(Location)
class LocationAdmin(admin.GISModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Search_city)
class LocationAdmin(admin.GISModelAdmin):
    list_display = ('city_name', 'created_at')
    search_fields = ('city_name',)