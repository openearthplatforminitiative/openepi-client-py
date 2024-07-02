from pydantic import BaseModel, Field, computed_field, model_validator
from httpx import AsyncClient, Client

from openepi_client import openepi_settings
from openepi_client.crop_health._crop_health_types import (
    SingleHLTPredictionResponse,
    MultiHLTPredictionResponse,
    BinaryPredictionResponse,
)


class PredictionRequest(BaseModel):
    image_data: bytes = Field(..., description="The image data as bytes")

    _prediction_endpoint: str = (
        f"{openepi_settings.api_root_url}/crop-health/predictions"
    )

    @model_validator(mode="after")
    def check_image_data(self) -> "PredictionRequest":
        if not self.image_data:
            raise ValueError("Image data must be provided and non-empty")
        return self

    @computed_field
    @property
    def _params(self) -> bytes:
        return self.image_data


class BinaryPredictionRequest(PredictionRequest):
    def get_sync(self) -> BinaryPredictionResponse:
        with Client() as client:
            response = client.post(
                f"{self._prediction_endpoint}/binary", content=self._params
            )
            return BinaryPredictionResponse(**response.json())

    async def get_async(self) -> BinaryPredictionResponse:
        async with AsyncClient() as async_client:
            response = await async_client.post(
                f"{self._prediction_endpoint}/binary", content=self._params
            )
            return BinaryPredictionResponse(**response.json())


class SingleHLTPredictionRequest(PredictionRequest):
    def get_sync(self) -> SingleHLTPredictionResponse:
        with Client() as client:
            response = client.post(
                f"{self._prediction_endpoint}/single-HLT", content=self._params
            )
            return SingleHLTPredictionResponse(**response.json())

    async def get_async(self) -> SingleHLTPredictionResponse:
        async with AsyncClient() as async_client:
            response = await async_client.post(
                f"{self._prediction_endpoint}/single-HLT", content=self._params
            )
            return SingleHLTPredictionResponse(**response.json())


class MultiHLTPredictionRequest(PredictionRequest):
    def get_sync(self) -> MultiHLTPredictionResponse:
        with Client() as client:
            response = client.post(
                f"{self._prediction_endpoint}/multi-HLT", content=self._params
            )
            return MultiHLTPredictionResponse(**response.json())

    async def get_async(self) -> MultiHLTPredictionResponse:
        async with AsyncClient() as async_client:
            response = await async_client.post(
                f"{self._prediction_endpoint}/multi-HLT", content=self._params
            )
            return MultiHLTPredictionResponse(**response.json())


class CropHealthClient:
    @staticmethod
    def get_binary_prediction(
        image_data: bytes,
    ) -> BinaryPredictionResponse:
        return BinaryPredictionRequest(image_data=image_data).get_sync()

    @staticmethod
    def get_singleHLT_prediction(
        image_data: bytes,
    ) -> SingleHLTPredictionResponse:
        return SingleHLTPredictionRequest(image_data=image_data).get_sync()

    @staticmethod
    def get_multiHLT_prediction(
        image_data: bytes,
    ) -> MultiHLTPredictionResponse:
        return MultiHLTPredictionRequest(image_data=image_data).get_sync()


class AsyncCropHealthClient:
    @staticmethod
    async def get_binary_prediction(
        image_data: bytes,
    ) -> BinaryPredictionResponse:
        return await BinaryPredictionRequest(image_data=image_data).get_async()

    @staticmethod
    async def get_singleHLT_prediction(
        image_data: bytes,
    ) -> SingleHLTPredictionResponse:
        return await SingleHLTPredictionRequest(image_data=image_data).get_async()

    @staticmethod
    async def get_multiHLT_prediction(
        image_data: bytes,
    ) -> MultiHLTPredictionResponse:
        return await MultiHLTPredictionRequest(image_data=image_data).get_async()
