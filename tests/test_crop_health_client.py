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

        # Assert that all values (2) are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        # The number of topk values is greater than 2 (the number
        # of classes in the binary model), so we can guarantee that
        # the sum of all values is 1.0
        assert sum(v for _, v in health if v is not None) == pytest.approx(
            1.0, rel=1e-1
        )

    def test_sync_get_singleHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_singleHLT_prediction(image_data)

        # Assert that only the topk values are non-null
        assert sum(v is not None for _, v in health) == self.topk

        # Assert that the sum of all values is greater than topk * 1.0 / number of classes
        # This is the only guarantee we can make about the output of the model
        # We cannot guarantee that the topk values sum to 1.0
        num_classes = sum(1 for _ in health)
        assert (
            sum(v for _, v in health if v is not None) >= self.topk * 1.0 / num_classes
        )

    def test_sync_get_multiHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_multiHLT_prediction(image_data)

        # Assert that only the topk values are non-null
        assert sum(v is not None for _, v in health) == self.topk

        # Assert that the sum of all values is greater than topk * 1.0 / number of classes
        # This is the only guarantee we can make about the output of the model
        # We cannot guarantee that the topk values sum to 1.0
        num_classes = sum(1 for _ in health)
        assert (
            sum(v for _, v in health if v is not None) >= self.topk * 1.0 / num_classes
        )

    @pytest.mark.asyncio
    async def test_async_get_binary_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_binary_prediction(image_data)

        # Assert that all values (2) are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        # The number of topk values is greater than 2 (the number
        # of classes in the binary model), so we can guarantee that
        # the sum of all values is 1.0
        assert sum(v for _, v in health if v is not None) == pytest.approx(
            1.0, rel=1e-1
        )

    @pytest.mark.asyncio
    async def test_async_get_singleHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_singleHLT_prediction(image_data)

        # Assert that only the topk values are non-null
        assert sum(v is not None for _, v in health) == self.topk

        # Assert that the sum of all values is greater than topk * 1.0 / number of classes
        # This is the only guarantee we can make about the output of the model
        # We cannot guarantee that the topk values sum to 1.0
        num_classes = sum(1 for _ in health)
        assert (
            sum(v for _, v in health if v is not None) >= self.topk * 1.0 / num_classes
        )

    @pytest.mark.asyncio
    async def test_async_get_multiHLT_health(self):
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_multiHLT_prediction(image_data)

        # Assert that only the topk values are non-null
        assert sum(v is not None for _, v in health) == self.topk

        # Assert that the sum of all values is greater than topk * 1.0 / number of classes
        # This is the only guarantee we can make about the output of the model
        # We cannot guarantee that the topk values sum to 1.0
        num_classes = sum(1 for _ in health)
        assert (
            sum(v for _, v in health if v is not None) >= self.topk * 1.0 / num_classes
        )

    def test_empty_image_data(self):
        # Test with empty bytes
        with pytest.raises(ValidationError) as exc_info:
            CropHealthClient.get_binary_prediction(image_data=b"")
        assert "Image data must be provided and non-empty" in str(exc_info.value)

        # Test that None raises Pydantic ValidationError
        with pytest.raises(ValidationError) as exc_info:
            CropHealthClient.get_binary_prediction(image_data=None)
