from datetime import date, timedelta
import pytest
from unittest.mock import patch, AsyncMock

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

    @patch("openepi_client.flood.FloodClient.get_threshold")
    def test_sync_threshold_geolocation(self, mock_get_threshold):
        mock_get_threshold.return_value = MockThresholdResponseModel()
        threshold: ThresholdResponseModel = FloodClient.get_threshold(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert threshold.queried_location.features[0].properties.threshold_2y > 0.0

    @patch("openepi_client.flood.FloodClient.get_threshold")
    def test_sync_threshold_bounding_box(self, mock_get_threshold):
        mock_get_threshold.return_value = MockThresholdResponseModel()
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
    @patch(
        "openepi_client.flood.AsyncFloodClient.get_threshold", new_callable=AsyncMock
    )
    async def test_async_threshold_geolocation(self, mock_get_threshold):
        mock_get_threshold.return_value = MockThresholdResponseModel()
        threshold: ThresholdResponseModel = await AsyncFloodClient.get_threshold(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert threshold.queried_location.features[0].properties.threshold_2y > 0.0

    @pytest.mark.asyncio
    @patch(
        "openepi_client.flood.AsyncFloodClient.get_threshold", new_callable=AsyncMock
    )
    async def test_async_threshold_bounding_box(self, mock_get_threshold):
        mock_get_threshold.return_value = MockThresholdResponseModel()
        threshold: ThresholdResponseModel = await AsyncFloodClient.get_threshold(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert threshold.queried_location.features[0].properties.threshold_2y > 0.0

    @patch("openepi_client.flood.FloodClient.get_summary")
    def test_sync_summary_geolocation(self, mock_get_summary):
        mock_get_summary.return_value = MockSummaryResponseModel()
        summary: SummaryResponseModel = FloodClient.get_summary(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert summary

    @patch("openepi_client.flood.FloodClient.get_summary")
    def test_sync_summary_neighbors(self, mock_get_summary):
        mock_get_summary.return_value = MockSummaryResponseModel()
        summary: SummaryResponseModel = FloodClient.get_summary(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON),
            include_neighbors=True,
        )
        assert summary

    @patch("openepi_client.flood.FloodClient.get_summary")
    def test_sync_summary_bounding_box(self, mock_get_summary):
        mock_get_summary.return_value = MockSummaryResponseModel()
        summary: SummaryResponseModel = FloodClient.get_summary(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert summary


class MockThresholdResponseModel:
    class QueriedLocation:
        class Features:
            class Properties:
                threshold_2y = 1.0

            properties = Properties()

        features = [Features()]

    queried_location = QueriedLocation()


class MockSummaryResponseModel:
    pass
