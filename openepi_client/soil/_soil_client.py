from httpx import AsyncClient, Client
import httpx
from pydantic import BaseModel, Field, computed_field
from openepi_client import openepi_settings, BoundingBox, GeoLocation

from openepi_client.soil._soil_types import (
    SoilTypeSummaryJSON,
    SoilTypeJSON,
    SoilPropertyJSON,
)


class SoilTypeRequest(BaseModel):
    geolocation: GeoLocation = Field(description="The geolocation to query for")
    top_k: int = Field(
        0,
        description=(
            "The number of most probable soil types that will "
            "be returned, sorted by probability in descending order"
        ),
    )

    _soil_type_endpoint: str = f"{openepi_settings.api_root_url}/soil/type"

    @computed_field
    @property
    def _params(self) -> dict:
        return {
            "lat": self.geolocation.lat,
            "lon": self.geolocation.lon,
            "top_k": self.top_k,
        }

    def get_sync(self) -> SoilTypeJSON:
        with Client() as client:
            response = client.get(
                self._soil_type_endpoint,
                params=self._params,
                timeout=httpx.Timeout(None),
            )
            return SoilTypeJSON(**response.json())

    async def get_async(self) -> SoilTypeJSON:
        async with AsyncClient() as async_client:
            response = await async_client.get(
                self._soil_type_endpoint,
                params=self._params,
                timeout=httpx.Timeout(None),
            )
            return SoilTypeJSON(**response.json())


class SoilTypeSummaryRequest(BaseModel):
    bounding_box: BoundingBox = Field(description="The bounding box to query for")

    _soil_type_summary_endpoint: str = (
        f"{openepi_settings.api_root_url}/soil/type/summary"
    )

    @computed_field
    @property
    def _params(self) -> dict:
        return {
            "min_lat": self.bounding_box.min_lat,
            "max_lat": self.bounding_box.max_lat,
            "min_lon": self.bounding_box.min_lon,
            "max_lon": self.bounding_box.max_lon,
        }

    def get_sync(self) -> SoilTypeSummaryJSON:
        with Client() as client:
            response = client.get(
                self._soil_type_summary_endpoint,
                params=self._params,
                timeout=httpx.Timeout(None),
            )
            return SoilTypeSummaryJSON(**response.json())

    async def get_async(self) -> SoilTypeSummaryJSON:
        async with AsyncClient() as async_client:
            response = await async_client.get(
                self._soil_type_summary_endpoint,
                params=self._params,
                timeout=httpx.Timeout(None),
            )
            return SoilTypeSummaryJSON(**response.json())


class SoilPropertyRequest(BaseModel):
    geolocation: GeoLocation = Field(description="The geolocation to query for")
    depths: list[str] = Field(
        ["0-5cm", "0-30cm", "5-15cm", "15-30cm", "30-60cm", "60-100cm", "100-200cm"],
        description="List of depths to query for",
    )
    properties: list[str] = Field(
        [
            "bdod",
            "cec",
            "cfvo",
            "clay",
            "nitrogen",
            "ocd",
            "ocs",
            "phh2o",
            "sand",
            "silt",
            "soc",
        ],
        description="List of properties to query for",
    )
    values: list[str] = Field(
        ["mean", "Q0.05", "Q0.5", "Q0.95", "uncertainty"],
        description="List of values to query for",
    )

    _soil_propery_endpoint: str = f"{openepi_settings.api_root_url}/soil/property"

    @computed_field
    @property
    def _params(self) -> dict:
        return {
            "lat": self.geolocation.lat,
            "lon": self.geolocation.lon,
            "depths": self.depths,
            "properties": self.properties,
            "values": self.values,
        }

    def get_sync(self) -> SoilPropertyJSON:
        with Client() as client:
            response = client.get(
                self._soil_propery_endpoint,
                params=self._params,
                timeout=httpx.Timeout(None),
            )
            return SoilPropertyJSON(**response.json())

    async def get_async(self) -> SoilPropertyJSON:
        async with AsyncClient() as async_client:
            response = await async_client.get(
                self._soil_propery_endpoint,
                params=self._params,
                timeout=httpx.Timeout(None),
            )
            return SoilPropertyJSON(**response.json())


class SoilClient:
    @staticmethod
    def get_soil_type(
        geolocation: GeoLocation,
        top_k: int = 0,
    ) -> SoilTypeJSON:
        return SoilTypeRequest(geolocation=geolocation, top_k=top_k).get_sync()

    @staticmethod
    def get_soil_property(
        geolocation: GeoLocation,
        depths: list[str] = [
            "0-5cm",
            "0-30cm",
            "5-15cm",
            "15-30cm",
            "30-60cm",
            "60-100cm",
            "100-200cm",
        ],
        properties: list[str] = [
            "bdod",
            "cec",
            "cfvo",
            "clay",
            "nitrogen",
            "ocd",
            "ocs",
            "phh2o",
            "sand",
            "silt",
            "soc",
        ],
        values: list[str] = ["mean", "Q0.05", "Q0.5", "Q0.95", "uncertainty"],
    ) -> SoilPropertyJSON:
        return SoilPropertyRequest(
            geolocation=geolocation, depths=depths, properties=properties, values=values
        ).get_sync()

    @staticmethod
    def get_soil_type_summary(
        bounding_box: BoundingBox,
    ) -> SoilTypeSummaryJSON:
        return SoilTypeSummaryRequest(bounding_box=bounding_box).get_sync()


class AsyncSoilClient:
    @staticmethod
    async def get_soil_type(
        geolocation: GeoLocation,
        top_k: int = 0,
    ) -> SoilTypeJSON:
        return await SoilTypeRequest(geolocation=geolocation, top_k=top_k).get_async()

    @staticmethod
    async def get_soil_property(
        geolocation: GeoLocation,
        depths: list[str] = [
            "0-5cm",
            "0-30cm",
            "5-15cm",
            "15-30cm",
            "30-60cm",
            "60-100cm",
            "100-200cm",
        ],
        properties: list[str] = [
            "bdod",
            "cec",
            "cfvo",
            "clay",
            "nitrogen",
            "ocd",
            "ocs",
            "phh2o",
            "sand",
            "silt",
            "soc",
        ],
        values: list[str] = ["mean", "Q0.05", "Q0.5", "Q0.95", "uncertainty"],
    ) -> SoilPropertyJSON:
        return await SoilPropertyRequest(
            geolocation=geolocation, depths=depths, properties=properties, values=values
        ).get_async()

    @staticmethod
    async def get_soil_type_summary(
        bounding_box: BoundingBox,
    ) -> SoilTypeSummaryJSON:
        return await SoilTypeSummaryRequest(bounding_box=bounding_box).get_async()
