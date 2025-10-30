from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkVS, TrailVS, PlaceVS, nearest_place, within_radius, trail_buffer_intersections


r=DefaultRouter()
r.register("parks", ParkVS)
r.register("trails", TrailVS)
r.register("places", PlaceVS)


urlpatterns = [
path("", include(r.urls)),
path("nearest/", nearest_place),
path("within/", within_radius),
path("intersections/", trail_buffer_intersections),
]