from openepi_client import GeoLocation
from openepi_client.weather import WeatherClient


class TestIntegrationWeather:
    def test_weather_integration(self):
        client = WeatherClient()
        response = client.get_location_forecast(
            geolocation=GeoLocation(lat=60.0, lon=10.0)
        )
        assert response is not None
