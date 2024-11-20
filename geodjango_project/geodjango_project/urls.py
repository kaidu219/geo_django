from django.contrib import admin
from django.urls import path

from locations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LocationView.as_view(), name='location_list'),
]
