from rest_framework_gis.serializers import GeoModelSerializer
from .models import Park, Trail, Place


class ParkSer(GeoModelSerializer):
    class Meta: model=Park; fields="__all__"
class TrailSer(GeoModelSerializer):
    class Meta: model=Trail; fields="__all__"
class PlaceSer(GeoModelSerializer):
    class Meta: model=Place; fields="__all__"