# openepi-client-py
A python client for the openepi data

## Sync usage
```python
from openepi_client.weather import WeatherClient

# Getting the sunrise and sunset times for a location
sunrise_sunset = WeatherClient.get_sunrise(lat=51.5074, lon=0.1278)

# Getting the weather forecast for a location
forecast = WeatherClient.get_location_forecast(lat=51.5074, lon=0.1278)
```

## Async usage
```python
from openepi_client.weather import AsyncWeatherClient

# Getting the sunrise and sunset times for a location
sunrise_sunset = await AsyncWeatherClient.get_sunrise(lat=51.5074, lon=0.1278)

# Getting the weather forecast for a location
forecast = await AsyncWeatherClient.get_location_forecast(lat=51.5074, lon=0.1278)
```

## Updating the client
### Weather
To update the weather data, run the following command:
```bash
 poetry run datamodel-codegen --url https://api-test.openepi.io/weather/openapi.json --output openepi_client/weather/weather_types.py --enum-field-as-literal all --output-model-type pydantic_v2.BaseModel
```
