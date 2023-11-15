from httpx import AsyncClient, Client
from datetime import datetime
from openepi_client.weather._weather_types import METJSONSunrise, METJSONForecast
from openepi_client import openepi_settings


class SunriseRequest:
    def __init__(
        self, lat: float, lon: float, date: datetime | None = datetime.today()
    ):
        self.params = {"lat": lat, "lon": lon, "date": date.strftime("%Y-%m-%d")}
        self.sunrise_endpoint = f"{openepi_settings.api_root_url}/weather/sunrise"

    def get_sync(self) -> METJSONSunrise:
        with Client() as client:
            response = client.get(self.sunrise_endpoint, params=self.params)
            return METJSONSunrise(**response.json())

    async def get_async(self) -> METJSONSunrise:
        async with AsyncClient() as async_client:
            response = await async_client.get(self.sunrise_endpoint, params=self.params)
            return METJSONSunrise(**response.json())


class LocationForecastRequest:
    def __init__(self, lat: float, lon: float, altitude: int):
        self.params = {"lat": lat, "lon": lon, "altitude": altitude}
        self.location_forecast_endpoint = (
            f"{openepi_settings.api_root_url}/weather/locationforecast"
        )

    def get_sync(self) -> METJSONForecast:
        with Client() as client:
            response = client.get(self.location_forecast_endpoint, params=self.params)
            return METJSONForecast(**response.json())

    async def get_async(self) -> METJSONForecast:
        async with AsyncClient() as async_client:
            response = await async_client.get(
                self.location_forecast_endpoint, params=self.params
            )
            return METJSONForecast(**response.json())


class WeatherClient:
    @staticmethod
    def get_sunrise(
        lat: float,
        lon: float,
        date: datetime | None = datetime.today(),
    ) -> METJSONSunrise:
        return SunriseRequest(lat, lon, date).get_sync()

    @staticmethod
    def get_location_forecast(
        lat: float, lon: float, altitude: int | None = 0
    ) -> METJSONForecast:
        return LocationForecastRequest(lat, lon, altitude).get_sync()


class AsyncWeatherClient:
    @staticmethod
    async def get_sunrise(
        lat: float,
        lon: float,
        date: datetime | None = datetime.today(),
    ) -> METJSONSunrise:
        return await SunriseRequest(lat, lon, date).get_async()

    @staticmethod
    async def get_location_forecast(
        lat: float, lon: float, altitude: int | None = 0
    ) -> METJSONForecast:
        return await LocationForecastRequest(lat, lon, altitude).get_async()
