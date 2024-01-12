import pytest

from openepi_client.deforestation import DeforestationClient, AsyncDeforestationClient
from openepi_client import GeoLocation, BoundingBox


class TestDeforestationClient:
    LAT: float = -1.9441
    LON: float = 30.0619

    MIN_LON: float = 28.850951
    MIN_LAT: float = 30.909622
    MAX_LON: float = -2.840114
    MAX_LAT: float = -1.041395

    def test_sync_get_basin_geolocation(self):
        basin = DeforestationClient.get_basin(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert basin.features[0].properties.start_year == 2001

    def test_sync_get_basin_bounding_box(self):
        basin = DeforestationClient.get_basin(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                min_lon=self.MIN_LON,
                max_lat=self.MAX_LAT,
                max_lon=self.MAX_LON,
            )
        )
        assert basin.features[0].properties.start_year == 2001

    @pytest.mark.asyncio
    async def test_async_get_basin_geolocation(self):
        basin = await AsyncDeforestationClient.get_basin(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert basin.features[0].properties.start_year == 2001

    @pytest.mark.asyncio
    async def test_async_get_basin_bounding_box(self):
        basin = await AsyncDeforestationClient.get_basin(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                min_lon=self.MIN_LON,
                max_lat=self.MAX_LAT,
                max_lon=self.MAX_LON,
            )
        )
        assert basin.features[0].properties.start_year == 2001
