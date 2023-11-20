from httpx import AsyncClient, Client

from openepi_client import openepi_settings
from openepi_client.geocoding._geocoding_types import FeatureCollection


class GeocodeRequest:
    def __init__(
        self,
        q: str,
        lat: float | None = None,
        lon: float | None = None,
        lang: str | None = None,
        limit: int | None = None,
    ):
        self.params = {
            k: v
            for k, v in {
                "q": q,
                "lon": lon,
                "lat": lat,
                "lang": lang,
                "limit": limit,
            }.items()
            if v is not None
        }
        self.geocode_endpoint = f"{openepi_settings.api_root_url}/geocoding/"

    def get_sync(self) -> FeatureCollection:
        with Client() as client:
            response = client.get(self.geocode_endpoint, params=self.params)
            return FeatureCollection(**response.json())

    async def get_async(self) -> FeatureCollection:
        async with AsyncClient() as async_client:
            response = await async_client.get(self.geocode_endpoint, params=self.params)
            return FeatureCollection(**response.json())


class ReverseGeocodeRequest:
    def __init__(
        self,
        lat: float | None = None,
        lon: float | None = None,
        lang: str | None = None,
        limit: int | None = None,
    ):
        self.params = {
            k: v
            for k, v in {
                "lon": lon,
                "lat": lat,
                "lang": lang,
                "limit": limit,
            }.items()
            if v is not None
        }
        self.reverse_geocode_endpoint = (
            f"{openepi_settings.api_root_url}/geocoding/reverse"
        )

    def get_sync(self) -> FeatureCollection:
        with Client() as client:
            response = client.get(self.reverse_geocode_endpoint, params=self.params)
            return FeatureCollection(**response.json())

    async def get_async(self) -> FeatureCollection:
        async with AsyncClient() as async_client:
            response = await async_client.get(
                self.reverse_geocode_endpoint, params=self.params
            )
            return FeatureCollection(**response.json())


class GeocodeClient:
    @staticmethod
    def geocode(
        q: str,
        lat: float | None = None,
        lon: float | None = None,
        lang: str | None = None,
        limit: int | None = None,
    ) -> FeatureCollection:
        return GeocodeRequest(q, lat, lon, lang, limit).get_sync()

    @staticmethod
    def reverse_geocode(
        lat: float,
        lon: float,
        lang: str | None = None,
        limit: int | None = None,
    ) -> FeatureCollection:
        return ReverseGeocodeRequest(lat, lon, lang, limit).get_sync()


class AsyncGeocodeClient:
    @staticmethod
    async def geocode(
        q: str,
        lat: float | None = None,
        lon: float | None = None,
        lang: str | None = None,
        limit: int | None = None,
    ) -> FeatureCollection:
        return await GeocodeRequest(q, lat, lon, lang, limit).get_async()

    @staticmethod
    async def reverse_geocode(
        lat: float,
        lon: float,
        lang: str | None = None,
        limit: int | None = None,
    ) -> FeatureCollection:
        return await ReverseGeocodeRequest(lat, lon, lang, limit).get_async()
