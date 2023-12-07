import pytest

from openepi_client import GeoLocation
from openepi_client.weather import (
    WeatherClient,
    AsyncWeatherClient,
    METJSONSunrise,
    METJSONForecast,
)


class TestWeatherClient:
    def test_sync_sunrise(self):
        the_weather: METJSONSunrise = WeatherClient.get_sunrise(
            geolocation=GeoLocation(lat=60.0, lon=10.0)
        )
        assert the_weather.copyright == "MET Norway"

    @pytest.mark.asyncio
    async def test_async_sunrise(self):
        the_weather: METJSONSunrise = await AsyncWeatherClient.get_sunrise(
            geolocation=GeoLocation(lat=60.0, lon=10.0)
        )
        assert the_weather.copyright == "MET Norway"

    def test_sync_weatherforecast(self):
        the_weather: METJSONForecast = WeatherClient.get_location_forecast(
            geolocation=GeoLocation(lat=60.0, lon=10.0, alt=0)
        )
        assert the_weather.geometry.coordinates == [10.0, 60.0, 0.0]

    @pytest.mark.asyncio
    async def test_async_weatherforecast(self):
        the_weather: METJSONForecast = await AsyncWeatherClient.get_location_forecast(
            geolocation=GeoLocation(lat=60.0, lon=10.0, alt=0)
        )
        assert the_weather.geometry.coordinates == [10.0, 60.0, 0.0]
