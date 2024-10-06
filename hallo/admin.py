from django.contrib import admin
from .models import Restaurant
from leaflet.admin import LeafletGeoAdmin

admin.site.register(Restaurant,LeafletGeoAdmin)