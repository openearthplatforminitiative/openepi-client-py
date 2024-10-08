import pytest
from unittest.mock import patch, AsyncMock

from openepi_client.soil import (
    SoilClient,
    AsyncSoilClient,
    SoilTypeSummaryJSON,
    SoilTypeJSON,
    SoilTypes,
)
from openepi_client import GeoLocation, BoundingBox


class TestSoilClient:
    LAT: float = 60.10
    LON: float = 9.58

    MIN_LON: float = 9.58
    MAX_LON: float = 9.6
    MIN_LAT: float = 60.10
    MAX_LAT: float = 60.12

    @patch("openepi_client.soil.SoilClient.get_soil_type")
    def test_sync_type(self, mock_get_soil_type):
        mock_get_soil_type.return_value = MockSoilTypeJSON()
        soil_type: SoilTypeJSON = SoilClient.get_soil_type(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert soil_type.properties.most_probable_soil_type == SoilTypes("Podzols")

    @patch("openepi_client.soil.SoilClient.get_soil_type")
    def test_sync_type_top_1(self, mock_get_soil_type):
        mock_get_soil_type.return_value = MockSoilTypeJSON()
        soil_type: SoilTypeJSON = SoilClient.get_soil_type(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON), top_k=1
        )
        assert soil_type.properties.probabilities[0].soil_type == SoilTypes("Podzols")
        assert soil_type.properties.probabilities[0].probability > 0

    @pytest.mark.asyncio
    @patch("openepi_client.soil.AsyncSoilClient.get_soil_type", new_callable=AsyncMock)
    async def test_async_type(self, mock_get_soil_type):
        mock_get_soil_type.return_value = MockSoilTypeJSON()
        soil_type: SoilTypeJSON = await AsyncSoilClient.get_soil_type(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert soil_type.properties.most_probable_soil_type == SoilTypes("Podzols")

    @pytest.mark.asyncio
    @patch("openepi_client.soil.AsyncSoilClient.get_soil_type", new_callable=AsyncMock)
    async def test_async_type_top_1(self, mock_get_soil_type):
        mock_get_soil_type.return_value = MockSoilTypeJSON()
        soil_type: SoilTypeJSON = await AsyncSoilClient.get_soil_type(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON), top_k=1
        )
        assert soil_type.properties.probabilities[0].soil_type == SoilTypes("Podzols")
        assert soil_type.properties.probabilities[0].probability > 0

    @patch("openepi_client.soil.SoilClient.get_soil_type_summary")
    def test_sync_type_summary(self, mock_get_soil_type_summary):
        mock_get_soil_type_summary.return_value = MockSoilTypeSummaryJSON()
        soil_type_summary: SoilTypeSummaryJSON = SoilClient.get_soil_type_summary(
            bounding_box=BoundingBox(
                min_lat=self.MIN_LAT,
                max_lat=self.MAX_LAT,
                min_lon=self.MIN_LON,
                max_lon=self.MAX_LON,
            )
        )
        assert soil_type_summary.properties.summaries[0].soil_type == SoilTypes(
            "Podzols"
        )
        assert soil_type_summary.properties.summaries[0].count > 0

    @pytest.mark.asyncio
    @patch(
        "openepi_client.soil.AsyncSoilClient.get_soil_type_summary",
        new_callable=AsyncMock,
    )
    async def test_async_type_summary(self, mock_get_soil_type_summary):
        mock_get_soil_type_summary.return_value = MockSoilTypeSummaryJSON()
        soil_type_summary: SoilTypeSummaryJSON = (
            await AsyncSoilClient.get_soil_type_summary(
                bounding_box=BoundingBox(
                    min_lat=self.MIN_LAT,
                    max_lat=self.MAX_LAT,
                    min_lon=self.MIN_LON,
                    max_lon=self.MAX_LON,
                )
            )
        )
        assert soil_type_summary.properties.summaries[0].soil_type == SoilTypes(
            "Podzols"
        )
        assert soil_type_summary.properties.summaries[0].count > 0


class MockSoilTypeJSON:
    class Properties:
        most_probable_soil_type = SoilTypes("Podzols")

        class Probabilities:
            soil_type = SoilTypes("Podzols")
            probability = 0.9

        probabilities = [Probabilities()]

    properties = Properties()


class MockSoilTypeSummaryJSON:
    class Properties:
        class Summaries:
            soil_type = SoilTypes("Podzols")
            count = 10

        summaries = [Summaries()]

    properties = Properties()
