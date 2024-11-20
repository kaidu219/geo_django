from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Location
from .forms import LocationForm

class LocationView(View):
    def get(self, request, *args, **kwargs):
    
        locations = Location.objects.all()
        form = LocationForm()  
        return render(request, 'locations/location_list.html', {
            'locations': locations,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        print(1)
       
        method = request.POST.get('_method', '').upper()
        if method == 'DELETE':
            print(2)
            location_id = request.POST.get('id')
            location = get_object_or_404(Location, pk=location_id)
            location.delete()
            return redirect('location_list')  

       
        form = LocationForm(request.POST)
        if form.is_valid():
            print(3)
            form.save()  
            return redirect('location_list') 

        locations = Location.objects.all()
        return render(request, 'locations/location_list.html', {
            'form': form,
            'locations': locations,
        })
