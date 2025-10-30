from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Park, Trail, Place


@admin.register(Park)
class ParkAdmin(OSMGeoAdmin):
    list_display=("name",)


@admin.register(Trail)
class TrailAdmin(OSMGeoAdmin):
    list_display=("name",)


@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    list_display=("name","kind")