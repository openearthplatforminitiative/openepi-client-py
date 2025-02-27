import pytest
from unittest.mock import patch, AsyncMock


from openepi_client.agriculture import (
    AgricultureClient,
    AsyncAgricultureClient,
    PeakTimingEnum,
    IntensityEnum,
)
from openepi_client import GeoLocation
from openepi_client.agriculture._agriculture_types import Summary


class TestAgricultureClient:
    LAT: float = -1.9441
    LON: float = 30.0619

    @patch("openepi_client.agriculture.AgricultureClient.get_summary")
    def test_sync_get_summary(self, mock_get_summary):
        mock_get_summary.return_value = MockSummary()
        summary: Summary = AgricultureClient.get_summary(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        print(summary)
        assert summary.deforestation.daterange_tot_treeloss == 123.456
        assert summary.soil.most_probable_soil_type == "Somesoil"
        assert summary.weather.air_temperature == 123.456
        assert summary.flood.peak_step == 10

    @pytest.mark.asyncio
    @patch(
        "openepi_client.agriculture.AsyncAgricultureClient.get_summary",
        new_callable=AsyncMock,
    )
    async def test_async_get_summary(self, mock_get_summary):
        mock_get_summary.return_value = MockSummary()
        summary: Summary = await AsyncAgricultureClient.get_summary(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert summary.deforestation.daterange_tot_treeloss == 123.456
        assert summary.soil.most_probable_soil_type == "Somesoil"
        assert summary.weather.air_temperature == 123.456
        assert summary.flood.peak_step == 10


class MockSummary:
    class Deforestation:
        daterange_tot_treeloss = 123.456

    class SoilType:
        most_probable_soil_type = "Somesoil"

    class Weather:
        air_temperature = 123.456
        cloud_area_fraction = 123.456
        error = "Some error"
        precipitation_amount = 123.456
        relative_humidity = 123.456
        wind_from_direction = 123.456
        wind_speed = 123.456
        wind_speed_of_gust = 123.456

    class Flood:
        error = "Some error"
        intensity = "P"
        issued_on = "some date"
        peak_day = "some date"
        peak_step = 10
        peak_timing = "BB"

    deforestation = Deforestation()
    soil = SoilType()
    weather = Weather()
    flood = Flood()
