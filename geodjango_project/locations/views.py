from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.gis.geos import Point
from django.views import View
from .models import Location, Search_city
from .forms import LocationForm

import requests

class LocationView(View):
    def get(self, request, *args, **kwargs):
    
        locations = Location.objects.all()
        search_history = Search_city.objects.all().order_by('-created_at')[:10]
        form = LocationForm()  
        return render(request, 'locations/location_list.html', {
            'locations': locations,
            'city': search_history,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        print(1)
        form = LocationForm(request.POST) 
        method = request.POST.get('_method', '').upper()

        api_key = '252ef48e318843c085c18b7257be4641'  # Ваш ключ от OpenCage API
        query = request.POST.get('search_query')

        if query:
            url = f'https://api.opencagedata.com/geocode/v1/json?q={query}&key={api_key}'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if data['results']:
                    result = data['results'][0]
                    city_name = result['formatted']
                    lat = result['geometry']['lat']
                    lng = result['geometry']['lng']

                    # Сохраняем найденный город в базу данных
                    point = Point(lng, lat)
                    Search_city.objects.create(city_name=city_name, point=point, search_query=query)

                    # Перерисовываем карту с новой точкой
                    request.session['search_result'] = {
                        'name': city_name,
                        'lat': lat,
                        'lng': lng,
                    }
                else:
                    request.session['search_error'] = 'Город не найден.'
            else:
                request.session['search_error'] = 'Ошибка подключения к API.'

            return redirect('location_list')

        if method == 'DELETE':
            print(2)
            location_id = request.POST.get('id')
            location = get_object_or_404(Location, pk=location_id)
            location.delete()
            return redirect('location_list')  

        if form.is_valid():
            print(3)
            # Получаем данные широты и долготы из формы
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')

            try:
                # Преобразуем данные в float
                latitude = float(latitude)
                longitude = float(longitude)

                # Создаём объект Point
                point = Point(longitude, latitude)

                # Сохраняем объект формы с полем point
                location = form.save(commit=False)
                location.point = point
                location.save()

                return redirect('location_list') 

            except ValueError:
                form.add_error(None, "Invalid latitude or longitude")  # Добавляем ошибку в форму

        locations = Location.objects.all()
        return render(request, 'locations/location_list.html', {
            'form': form,
            'locations': locations,
        })