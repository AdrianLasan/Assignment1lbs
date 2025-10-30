# Parks & Amenities Finder (Minimal LBS)


A minimal Django + PostGIS + Leaflet app meeting A1 rubric.


## Features
- Spatial models: Park(Polygon), Trail(Line), Place(Point)
- CRUD via REST (DRF/DRF‑GIS) + Django admin
- Spatial queries: nearest, within radius, trail-buffer intersections
- Responsive Bootstrap UI, Leaflet map with OSM tiles
- Local deployment; optional Docker (bonus)


## Setup (Local Postgres/PostGIS)
1. Create DB & enable PostGIS
```sql
CREATE DATABASE lbs;
CREATE USER lbs WITH PASSWORD 'lbs';
GRANT ALL PRIVILEGES ON DATABASE lbs TO lbs;
\c lbs
CREATE EXTENSION postgis;