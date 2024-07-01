import pytest
import os

from openepi_client.crop_health import CropHealthClient, AsyncCropHealthClient


class TestCropHealthClient:
    image_path = os.path.abspath("tests/assets/plant.jpg")

    def test_sync_get_binary_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_binary_health_prediction(image_data)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health if v is not None) == pytest.approx(
            1.0, rel=1e-1
        )

    def test_sync_get_singleHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_singleHLT_health_prediction(image_data)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health if v is not None) == pytest.approx(
            1.0, rel=1e-1
        )

    def test_sync_get_multiHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_multiHLT_health_prediction(image_data)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health if v is not None) == pytest.approx(
            1.0, rel=1e-1
        )

    @pytest.mark.asyncio
    async def test_async_get_binary_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_binary_health_prediction(
                image_data
            )
        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health if v is not None) == pytest.approx(
            1.0, rel=1e-1
        )

    @pytest.mark.asyncio
    async def test_async_get_singleHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_singleHLT_health_prediction(
                image_data
            )
        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health if v is not None) == pytest.approx(
            1.0, rel=1e-1
        )

    @pytest.mark.asyncio
    async def test_async_get_multiHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_multiHLT_health_prediction(
                image_data
            )
        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health if v is not None) == pytest.approx(
            1.0, rel=1e-1
        )
