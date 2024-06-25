from datetime import date, timedelta
import pytest

from openepi_client.flood import (
    FloodClient,
    AsyncFloodClient,
    ThresholdResponseModel,
    SummaryResponseModel,
)
from openepi_client import GeoLocation, BoundingBox


class TestFloodClient:
    LAT: float = 5.175
    LON: float = 37.625

    MIN_LON: float = 22.0
    MAX_LON: float = 23.05
    MIN_LAT: float = 4.764412
    MAX_LAT: float = 5.015732

    def test_sync_threshold_geolocation(self):
        threshold: ThresholdResponseModel = FloodClient.get_threshold(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert threshold.queried_location.features[0].properties.threshold_2y > 0.0

    def test_sync_threshold_bounding_box(self):
        threshold: ThresholdResponseModel = FloodClient.get_threshold(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert threshold.queried_location.features[0].properties.threshold_2y > 0.0

    @pytest.mark.asyncio
    async def test_async_threshold_geolocation(self):
        threshold: ThresholdResponseModel = await AsyncFloodClient.get_threshold(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert threshold.queried_location.features[0].properties.threshold_2y > 0.0

    @pytest.mark.asyncio
    async def test_async_threshold_bounding_box(self):
        threshold: ThresholdResponseModel = await AsyncFloodClient.get_threshold(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert threshold.queried_location.features[0].properties.threshold_2y > 0.0

    def test_sync_summary_geolocation(self):
        summary: SummaryResponseModel = FloodClient.get_summary(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert summary

    def test_sync_summary_neighbors(self):
        summary: SummaryResponseModel = FloodClient.get_summary(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON),
            include_neighbors=True,
        )
        assert summary

    def test_sync_summary_bounding_box(self):
        summary: SummaryResponseModel = FloodClient.get_summary(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert summary

    @pytest.mark.asyncio
    async def test_async_summary_geolocation(self):
        summary = await AsyncFloodClient.get_summary(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert summary

    @pytest.mark.asyncio
    async def test_async_summary_neighbors(self):
        summary = await AsyncFloodClient.get_summary(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON, include_neighbors=True)
        )
        assert summary

    @pytest.mark.asyncio
    async def test_async_summary_bounding_box(self):
        summary = await AsyncFloodClient.get_summary(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert summary

    def test_sync_detailed_geolocation(self):
        detailed = FloodClient.get_detailed(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert detailed

    def test_sync_detailed_date(self):
        start_date = date.today()
        end_date = start_date + timedelta(days=4)
        detailed = FloodClient.get_detailed(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON),
            start_date=start_date,
            end_date=end_date,
        )
        assert detailed

    def test_sync_detailed_neighbors(self):
        detailed = FloodClient.get_detailed(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON),
            include_neighbors=True,
        )
        assert detailed

    def test_sync_detailed_bounding_box(self):
        detailed = FloodClient.get_detailed(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert detailed

    @pytest.mark.asyncio
    async def test_async_detailed(self):
        detailed = await AsyncFloodClient.get_detailed(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert detailed

    @pytest.mark.asyncio
    async def test_async_detailed_bounding_box(self):
        detailed = await AsyncFloodClient.get_detailed(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert detailed
