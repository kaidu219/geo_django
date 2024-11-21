from django import forms
from .models import Location
from django.contrib.gis.geos import Point


class LocationForm(forms.ModelForm):
    latitude = forms.FloatField(
        min_value=-90,
        max_value=90,
        required=False, 
        help_text="Введите широту (от -90 до 90)"
    )
    longitude = forms.FloatField(
        min_value=-180,
        max_value=180,
        required=False, 
        help_text="Введите долготу (от -180 до 180)"
    )

    class Meta:
        model = Location
        fields = ['name', 'description', 'latitude', 'longitude']


    def clean(self):
        cleaned_data = super().clean()
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')

        if (latitude is not None and longitude is None) or (latitude is None and longitude is not None):
            raise forms.ValidationError("Необходимо указать и широту, и долготу.")

        return cleaned_data
    

    def save(self, commit=True):
        instance = super().save(commit=False)
        latitude = self.cleaned_data.get('latitude')
        longitude = self.cleaned_data.get('longitude')

        # Если широта и долгота указаны, создаём объект Point
        if latitude is not None and longitude is not None:
            instance.point = Point(longitude, latitude)

        if commit:
            instance.save()
        return instance