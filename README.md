# openepi-client-py
A python client for the openepi data

## Weather
### Sync usage
```python
from openepi_client.weather import WeatherClient

# Getting the sunrise and sunset times for a location
sunrise_sunset = WeatherClient.get_sunrise(lat=51.5074, lon=0.1278)

# Getting the weather forecast for a location
forecast = WeatherClient.get_location_forecast(lat=51.5074, lon=0.1278)

# Searching for coordinates for a location
feature_collection = GeocodeClient.geocode(q="Kigali, Rwanda")
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

## Updating the client
```bash
 poetry run datamodel-codegen --url https://api-test.openepi.io/weather/openapi.json --output openepi_client/weather/_weather_types.py --enum-field-as-literal all --output-model-type pydantic_v2.BaseModel
 poetry run datamodel-codegen --url https://api-test.openepi.io/geocoding/openapi.json --output openepi_client/geocoding/_geocoding_types.py --enum-field-as-literal all --output-model-type pydantic_v2.BaseModel
```
