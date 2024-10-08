import pytest
from unittest.mock import patch, AsyncMock

from openepi_client import GeoLocation
from openepi_client.geocoding import (
    GeocodeClient,
    AsyncGeocodeClient,
    FeatureCollection,
)


class TestGeocodeClient:
    @patch("openepi_client.geocoding.GeocodeClient.geocode")
    def test_sync_geocode(self, mock_geocode):
        mock_geocode.return_value = MockFeatureCollection()
        features: FeatureCollection = GeocodeClient.geocode(q="Kigali, Rwanda")
        assert features.features[0].properties.countrycode == "RW"

    @pytest.mark.asyncio
    @patch(
        "openepi_client.geocoding.AsyncGeocodeClient.geocode", new_callable=AsyncMock
    )
    async def test_async_geocode(self, mock_geocode):
        mock_geocode.return_value = MockFeatureCollection()
        features: FeatureCollection = await AsyncGeocodeClient.geocode(
            q="Kigali, Rwanda"
        )
        assert features.features[0].properties.countrycode == "RW"

    @patch("openepi_client.geocoding.GeocodeClient.reverse_geocode")
    def test_sync_reverse_geocode(self, mock_reverse_geocode):
        mock_reverse_geocode.return_value = MockFeatureCollection()
        features: FeatureCollection = GeocodeClient.reverse_geocode(
            geolocation=GeoLocation(lat=60.0, lon=10.0)
        )
        assert len(features.features) > 0

    @pytest.mark.asyncio
    @patch(
        "openepi_client.geocoding.AsyncGeocodeClient.reverse_geocode",
        new_callable=AsyncMock,
    )
    async def test_async_reverse_geocode(self, mock_reverse_geocode):
        mock_reverse_geocode.return_value = MockFeatureCollection()
        features: FeatureCollection = await AsyncGeocodeClient.reverse_geocode(
            geolocation=GeoLocation(lat=60.0, lon=10.0)
        )
        assert len(features.features) > 0


class MockFeatureCollection:
    class Features:
        class Properties:
            countrycode = "RW"

        properties = Properties()

    features = [Features()]
