import pytest
import os
from pydantic import ValidationError

from openepi_client.crop_health import CropHealthClient, AsyncCropHealthClient


class TestCropHealthClient:
    image_path = os.path.abspath("tests/assets/plant.jpg")
    topk = 5  # number of non-null values returned by the (non binary) models

    def test_sync_get_binary_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_binary_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    def test_sync_get_singleHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_singleHLT_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    def test_sync_get_multiHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_multiHLT_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    @pytest.mark.asyncio
    async def test_async_get_binary_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_binary_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    @pytest.mark.asyncio
    async def test_async_get_singleHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_singleHLT_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    @pytest.mark.asyncio
    async def test_async_get_multiHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_multiHLT_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    def test_empty_image_data(self):
        # Test with empty bytes
        with pytest.raises(ValidationError) as exc_info:
            CropHealthClient.get_binary_prediction(image_data=b"")
        assert "Image data must be provided and non-empty" in str(exc_info.value)

        # Test that None raises Pydantic ValidationError
        with pytest.raises(ValidationError) as exc_info:
            CropHealthClient.get_binary_prediction(image_data=None)
