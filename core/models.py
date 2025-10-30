from django.contrib.gis.db import models


class Park(models.Model):
    name = models.CharField(max_length=120)
    geom = models.PolygonField(srid=4326)
    def __str__(self): return self.name


class Trail(models.Model):
    name = models.CharField(max_length=120)
    geom = models.LineStringField(srid=4326)
    def __str__(self): return self.name


class Place(models.Model):
    KIND_CHOICES = [("water","Water"),("toilet","Toilet"),("cafe","Cafe")]
    name = models.CharField(max_length=120)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    geom = models.PointField(srid=4326)
    def __str__(self): return self.name