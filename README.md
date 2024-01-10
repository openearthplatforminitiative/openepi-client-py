# openepi-client-py
A python client for accessing data from OpenEPI.

## Table of Contents
- [Weather Data](#weather)
  - [Sync usage](#sync-usage)
  - [Async usage](#async-usage)
- [Geocoding](#geocoding)
  - [Sync usage](#sync-usage-1)
  - [Async usage](#async-usage-1)
- [Flood predictions](#flood)
  - [Sync usage](#sync-usage-2)
  - [Async usage](#async-usage-2)

## Weather
### Sync usage
```python
from openepi_client import GeoLocation
from openepi_client.weather import WeatherClient

# Getting the sunrise and sunset times for a location
sunrise_sunset = WeatherClient.get_sunrise(geolocation=GeoLocation(lat=51.5074, lon=0.1278))

# Getting the weather forecast for a location
forecast = WeatherClient.get_location_forecast(geolocation=GeoLocation(lat=51.5074, lon=0.1278))
```

### Async usage
```python
from openepi_client.weather import AsyncWeatherClient

# Getting the sunrise and sunset times for a location
sunrise_sunset = await AsyncWeatherClient.get_sunrise(lat=51.5074, lon=0.1278)

# Getting the weather forecast for a location
forecast = await AsyncWeatherClient.get_location_forecast(lat=51.5074, lon=0.1278)

# Searching for coordinates for a location
feature_collection = await AsyncGeocodeClient.geocode(q="Kigali, Rwanda")
```

## Geocoding
### Sync usage
```python
from openepi_client.geocoding import GeocodeClient

# Searching for the coordinates to a named place
feature_collection = GeocodeClient.geocode(q="Kigali, Rwanda")

# Geocode with priority to a lat and lon
feature_collection = GeocodeClient.geocode(q="Kigali, Rwanda", lat=51.5074, lon=0.1278)

# Reverse geocode
feature_collection = GeocodeClient.reverse_geocode(lat=51.5074, lon=0.1278)
```

### Async usage
```python
from openepi_client.geocoding import AsyncGeocodeClient

# Searching for coordinates for a location
feature_collection = await AsyncGeocodeClient.geocode(q="Kigali, Rwanda")

# Geocode with priority to a lat and lon
feature_collection = await AsyncGeocodeClient.geocode(q="Kigali, Rwanda", lat=51.5074, lon=0.1278)

# Reverse geocode
feature_collection = await AsyncGeocodeClient.reverse_geocode(lat=51.5074, lon=0.1278)
```

## Flood
### Sync usage
```python
from openepi_client import GeoLocation, BoundingBox
from openepi_client.flood import FloodClient

# Get the return period thresholds for a given geolocation
thresholds = FloodClient.get_threshold(geolocation=GeoLocation(lat=51.5074, lon=0.1278))

# Get the return period thresholds for a given bounding box
thresholds = FloodClient.get_threshold(bounding_box=BoundingBox(min_lat=4.764412, min_lon=22.0, max_lat=5.015732, max_lon=23.05))

# Get a summary flood forecast for a given coordinate
summary = FloodClient.get_summary(geolocation=GeoLocation(lat=51.5074, lon=0.1278))

# Get a summary flood forecast for a given bounding box
summary = FloodClient.get_summary(bounding_box=BoundingBox(min_lat=4.764412, min_lon=22.0, max_lat=5.015732, max_lon=23.05))

# Get a detailed flood forecast for a given coordinate
detailed = FloodClient.get_detailed(geolocation=GeoLocation(lat=51.5074, lon=0.1278))

# Get a detailed flood forecast for a given bounding box
detailed = FloodClient.get_detailed(bounding_box=BoundingBox(min_lat=4.764412, min_lon=22.0, max_lat=5.015732, max_lon=23.05))
```


### Async usage
```python
from openepi_client import GeoLocation, BoundingBox
from openepi_client.flood import AsyncFloodClient

# Get the return period thresholds for a given geolocation
thresholds = await AsyncFloodClient.get_threshold(geolocation=GeoLocation(lat=51.5074, lon=0.1278))

# Get the return period thresholds for a given bounding box
thresholds = await AsyncFloodClient.get_threshold(bounding_box=BoundingBox(min_lat=4.764412, min_lon=22.0, max_lat=5.015732, max_lon=23.05))

# Get a summary flood forecast for a given coordinate
summary = await AsyncFloodClient.get_summary(geolocation=GeoLocation(lat=51.5074, lon=0.1278))

# Get a summary flood forecast for a given bounding box
summary = await AsyncFloodClient.get_summary(bounding_box=BoundingBox(min_lat=4.764412, min_lon=22.0, max_lat=5.015732, max_lon=23.05))

# Get a detailed flood forecast for a given coordinate
detailed = await AsyncFloodClient.get_detailed(geolocation=GeoLocation(lat=51.5074, lon=0.1278))

# Get a detailed flood forecast for a given bounding box
detailed = await AsyncFloodClient.get_detailed(bounding_box=BoundingBox(min_lat=4.764412, min_lon=22.0, max_lat=5.015732, max_lon=23.05))
```


## Updating the client
The following commands are used to update the client types. The commands are run from the root of the project.
```bash
 poetry run datamodel-codegen --url https://api-test.openepi.io/weather/openapi.json --output openepi_client/weather/_weather_types.py --enum-field-as-literal all --output-model-type pydantic_v2.BaseModel
 poetry run datamodel-codegen --url https://api-test.openepi.io/geocoding/openapi.json --output openepi_client/geocoding/_geocoding_types.py --enum-field-as-literal all --output-model-type pydantic_v2.BaseModel
 poetry run datamodel-codegen --url https://api-test.openepi.io/flood/openapi.json --output openepi_client/flood/_flood_types.py --enum-field-as-literal all --output-model-type pydantic_v2.BaseModel
```
