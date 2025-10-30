from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Park, Trail, Place
from .serializers import ParkSer, TrailSer, PlaceSer


class ParkVS(viewsets.ModelViewSet): queryset=Park.objects.all(); serializer_class=ParkSer
class TrailVS(viewsets.ModelViewSet): queryset=Trail.objects.all(); serializer_class=TrailSer
class PlaceVS(viewsets.ModelViewSet): queryset=Place.objects.all(); serializer_class=PlaceSer


@api_view(["GET"])
def nearest_place(request):
lat=float(request.GET.get("lat")); lng=float(request.GET.get("lng"))
p=Point(lng,lat,srid=4326)
q=Place.objects.annotate(d=Distance("geom",p)).order_by("d").first()
return Response(PlaceSer(q).data if q else {})


@api_view(["GET"])
def within_radius(request):
lat=float(request.GET.get("lat")); lng=float(request.GET.get("lng")); r=float(request.GET.get("r",500))
p=Point(lng,lat,srid=4326)
qs=Place.objects.filter(geom__distance_lte=(p, D(m=r)))
return Response(PlaceSer(qs, many=True).data)


@api_view(["GET"])
def trail_buffer_intersections(request):
trail_id=int(request.GET.get("trail_id")); buf=float(request.GET.get("buffer",50))
t=Trail.objects.get(id=trail_id)
qs=Place.objects.filter(geom__within=t.geom.buffer(buf/111320.0)) # meters to degrees approx
return Response(PlaceSer(qs, many=True).data)