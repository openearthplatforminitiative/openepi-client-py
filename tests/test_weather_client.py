import pytest
from unittest.mock import patch, AsyncMock

from openepi_client import GeoLocation
from openepi_client.weather import (
    WeatherClient,
    AsyncWeatherClient,
    METJSONSunrise,
    METJSONForecast,
)


class TestWeatherClient:
    @patch("openepi_client.weather.WeatherClient.get_sunrise")
    def test_sync_sunrise(self, mock_get_sunrise):
        mock_get_sunrise.return_value = MockMETJSONSunrise()
        the_weather: METJSONSunrise = WeatherClient.get_sunrise(
            geolocation=GeoLocation(lat=60.0, lon=10.0)
        )
        assert the_weather.copyright == "MET Norway"

    @pytest.mark.asyncio
    @patch(
        "openepi_client.weather.AsyncWeatherClient.get_sunrise", new_callable=AsyncMock
    )
    async def test_async_sunrise(self, mock_get_sunrise):
        mock_get_sunrise.return_value = MockMETJSONSunrise()
        the_weather: METJSONSunrise = await AsyncWeatherClient.get_sunrise(
            geolocation=GeoLocation(lat=60.0, lon=10.0)
        )
        assert the_weather.copyright == "MET Norway"

    @patch("openepi_client.weather.WeatherClient.get_location_forecast")
    def test_sync_weatherforecast(self, mock_get_location_forecast):
        mock_get_location_forecast.return_value = MockMETJSONForecast()
        the_weather: METJSONForecast = WeatherClient.get_location_forecast(
            geolocation=GeoLocation(lat=60.0, lon=10.0, alt=0)
        )
        assert the_weather.geometry.coordinates == [10.0, 60.0, 0.0]

    @pytest.mark.asyncio
    @patch(
        "openepi_client.weather.AsyncWeatherClient.get_location_forecast",
        new_callable=AsyncMock,
    )
    async def test_async_weatherforecast(self, mock_get_location_forecast):
        mock_get_location_forecast.return_value = MockMETJSONForecast()
        the_weather: METJSONForecast = await AsyncWeatherClient.get_location_forecast(
            geolocation=GeoLocation(lat=60.0, lon=10.0, alt=0)
        )
        assert the_weather.geometry.coordinates == [10.0, 60.0, 0.0]


class MockMETJSONSunrise:
    copyright = "MET Norway"


class MockMETJSONForecast:
    class Geometry:
        coordinates = [10.0, 60.0, 0.0]

    geometry = Geometry()
