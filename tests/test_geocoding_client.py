import pytest

from openepi_client.geocoding import (
    GeocodeClient,
    AsyncGeocodeClient,
    FeatureCollection,
)


class TestGeocodeClient:
    def test_sync_geocode(self):
        features: FeatureCollection = GeocodeClient.geocode(q="Kigali, Rwanda")
        assert features.features[0].properties.countrycode == "RW"

    @pytest.mark.asyncio
    async def test_async_geocode(self):
        features: FeatureCollection = await AsyncGeocodeClient.geocode(
            q="Kigali, Rwanda"
        )
        assert features.features[0].properties.countrycode == "RW"

    def test_sync_reverse_geocode(self):
        features: FeatureCollection = GeocodeClient.reverse_geocode(lat=60.0, lon=10.0)
        assert len(features.features) > 0

    @pytest.mark.asyncio
    async def test_async_reverse_geocode(self):
        features: FeatureCollection = await AsyncGeocodeClient.reverse_geocode(
            lat=60.0, lon=10.0
        )
        assert len(features.features) > 0
