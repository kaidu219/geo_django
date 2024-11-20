from django.contrib.gis import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.GISModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)