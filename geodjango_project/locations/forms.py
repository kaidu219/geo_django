from django import forms
from .models import Location
from django.contrib.gis.geos import Point

class LocationForm(forms.ModelForm):
    latitude = forms.FloatField(
        min_value=-90,
        max_value=90,
        help_text="Введите широту (от -90 до 90)"
    )
    longitude = forms.FloatField(
        min_value=-180,
        max_value=180,
        help_text="Введите долготу (от -180 до 180)"
    )

    class Meta:
        model = Location
        fields = ['name', 'description', 'latitude', 'longitude']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.point = Point(
            float(self.cleaned_data['longitude']),
            float(self.cleaned_data['latitude'])
        )
        if commit:
            instance.save()
        return instance