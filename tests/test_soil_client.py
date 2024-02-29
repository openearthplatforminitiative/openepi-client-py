import pytest

from openepi_client.soil import (
    SoilClient,
    AsyncSoilClient,
    SoilTypeSummaryJSON,
    SoilTypeJSON,
    SoilPropertyJSON,
    SoilTypes,
    SoilPropertiesCodes,
    SoilDepthLabels,
)
from openepi_client import GeoLocation, BoundingBox


class TestSoilClient:
    LAT: float = 60.10
    LON: float = 9.58

    MIN_LON: float = 9.58
    MAX_LON: float = 9.6
    MIN_LAT: float = 60.10
    MAX_LAT: float = 60.12

    def test_sync_type(self):
        soil_type: SoilTypeJSON = SoilClient.get_soil_type(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert soil_type.properties.most_probable_soil_type == SoilTypes("Podzols")

    def test_sync_type_top_1(self):
        soil_type: SoilTypeJSON = SoilClient.get_soil_type(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON), top_k=1
        )
        assert soil_type.properties.probabilities[0].soil_type == SoilTypes("Podzols")
        assert soil_type.properties.probabilities[0].probability > 0

    @pytest.mark.asyncio
    async def test_async_type(self):
        soil_type: SoilTypeJSON = await AsyncSoilClient.get_soil_type(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON)
        )
        assert soil_type.properties.most_probable_soil_type == SoilTypes("Podzols")

    @pytest.mark.asyncio
    async def test_async_type_top_1(self):
        soil_type: SoilTypeJSON = await AsyncSoilClient.get_soil_type(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON), top_k=1
        )
        assert soil_type.properties.probabilities[0].soil_type == SoilTypes("Podzols")
        assert soil_type.properties.probabilities[0].probability > 0

    def test_sync_type_summary(self):
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
    async def test_async_type_summary(self):
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

    def test_sync_property(self):
        properties = ["clay", "silt"]
        depths = ["0-5cm"]
        values = ["mean", "Q0.05"]
        soil_property: SoilPropertyJSON = SoilClient.get_soil_property(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON),
            depths=depths,
            properties=properties,
            values=values,
        )
        assert soil_property.properties.layers[0].code == SoilPropertiesCodes(
            "clay"
        ) or SoilPropertiesCodes("silt")
        assert soil_property.properties.layers[0].depths[0].label == SoilDepthLabels(
            "0-5cm"
        )
        assert soil_property.properties.layers[0].depths[0].values.mean >= 0
        assert soil_property.properties.layers[0].depths[0].values.Q0_05 >= 0

        assert soil_property.properties.layers[1].code == SoilPropertiesCodes(
            "clay"
        ) or SoilPropertiesCodes("silt")
        assert soil_property.properties.layers[1].depths[0].label == SoilDepthLabels(
            "0-5cm"
        )
        assert soil_property.properties.layers[1].depths[0].values.mean >= 0
        assert soil_property.properties.layers[1].depths[0].values.Q0_05 >= 0

    @pytest.mark.asyncio
    async def test_async_property(self):
        properties = ["clay", "silt"]
        depths = ["0-5cm"]
        values = ["mean", "Q0.05"]
        soil_property: SoilPropertyJSON = await AsyncSoilClient.get_soil_property(
            geolocation=GeoLocation(lat=self.LAT, lon=self.LON),
            depths=depths,
            properties=properties,
            values=values,
        )
        assert soil_property.properties.layers[0].code == SoilPropertiesCodes(
            "clay"
        ) or SoilPropertiesCodes("silt")
        assert soil_property.properties.layers[0].depths[0].label == SoilDepthLabels(
            "0-5cm"
        )
        assert soil_property.properties.layers[0].depths[0].values.mean >= 0
        assert soil_property.properties.layers[0].depths[0].values.Q0_05 >= 0

        assert soil_property.properties.layers[1].code == SoilPropertiesCodes(
            "clay"
        ) or SoilPropertiesCodes("silt")
        assert soil_property.properties.layers[1].depths[0].label == SoilDepthLabels(
            "0-5cm"
        )
        assert soil_property.properties.layers[1].depths[0].values.mean >= 0
        assert soil_property.properties.layers[1].depths[0].values.Q0_05 >= 0
