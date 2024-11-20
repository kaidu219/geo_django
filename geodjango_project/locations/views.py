from django.views.generic import ListView
from .models import Location

class LocationListView(ListView):
    model = Location
    template_name = 'locations/location_list.html'
    context_object_name = 'locations'