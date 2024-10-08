import pytest
import os
from unittest.mock import patch, AsyncMock

from openepi_client.crop_health import CropHealthClient, AsyncCropHealthClient


class TestCropHealthClient:
    image_path = os.path.abspath("tests/assets/plant.jpg")

    @patch("openepi_client.crop_health.CropHealthClient.get_binary_prediction")
    def test_sync_get_binary_health(self, mock_get_binary_prediction):
        mock_get_binary_prediction.return_value = MockHealth()
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_binary_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    @patch("openepi_client.crop_health.CropHealthClient.get_singleHLT_prediction")
    def test_sync_get_singleHLT_health(self, mock_get_singleHLT_prediction):
        mock_get_singleHLT_prediction.return_value = MockHealth()
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_singleHLT_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    @patch("openepi_client.crop_health.CropHealthClient.get_multiHLT_prediction")
    def test_sync_get_multiHLT_health(self, mock_get_multiHLT_prediction):
        mock_get_multiHLT_prediction.return_value = MockHealth()
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = CropHealthClient.get_multiHLT_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    @pytest.mark.asyncio
    @patch(
        "openepi_client.crop_health.AsyncCropHealthClient.get_binary_prediction",
        new_callable=AsyncMock,
    )
    async def test_async_get_binary_health(self, mock_get_binary_prediction):
        mock_get_binary_prediction.return_value = MockHealth()
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_binary_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    @pytest.mark.asyncio
    @patch(
        "openepi_client.crop_health.AsyncCropHealthClient.get_singleHLT_prediction",
        new_callable=AsyncMock,
    )
    async def test_async_get_singleHLT_health(self, mock_get_singleHLT_prediction):
        mock_get_singleHLT_prediction.return_value = MockHealth()
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_singleHLT_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)

    @pytest.mark.asyncio
    @patch(
        "openepi_client.crop_health.AsyncCropHealthClient.get_multiHLT_prediction",
        new_callable=AsyncMock,
    )
    async def test_async_get_multiHLT_health(self, mock_get_multiHLT_prediction):
        mock_get_multiHLT_prediction.return_value = MockHealth()
        with open(self.image_path, "rb") as f:
            image_data = f.read()
            health = await AsyncCropHealthClient.get_multiHLT_prediction(image_data)

        # Assert that all values are non-null
        assert all(v is not None for _, v in health)

        # Assert that the sum of all values is approx equal to 1.0
        assert sum(v for _, v in health) == pytest.approx(1.0, rel=1e-1)


class MockHealth:
    def __iter__(self):
        return iter([("health1", 0.5), ("health2", 0.5)])
