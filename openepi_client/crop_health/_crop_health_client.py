from pydantic import BaseModel, Field, computed_field, model_validator, FilePath
from httpx import AsyncClient, Client

from openepi_client import openepi_settings
from openepi_client.crop_health._crop_health_types import (
    SingleHLTPredictionResponse,
    MultiHLTPredictionResponse,
    BinaryPredictionResponse,
)


class PredictionRequest(BaseModel):
    image_path: FilePath | None = Field(
        default=None, description="The full filepath of the image"
    )

    _prediction_endpoint: str = (
        f"{openepi_settings.api_root_url}/crop-health/predictions"
    )

    @model_validator(mode="after")
    def check_mutually_exclusive(self) -> "PredictionRequest":
        if not (self.image_path is not None):
            raise ValueError("Specify image path")
        return self

    @computed_field
    @property
    def _params(self) -> bytes:
        return open(self.image_path, "rb").read()


class BinaryHealthPredictionRequest(PredictionRequest):
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


class SingleHLTHealthPredictionRequest(PredictionRequest):
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


class MultiHLTHealthPredictionRequest(PredictionRequest):
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
    def get_binary_health_prediction(
        image_path: str | None = None,
    ) -> BinaryPredictionResponse:
        return BinaryHealthPredictionRequest(image_path=image_path).get_sync()

    @staticmethod
    def get_singleHLT_health_prediction(
        image_path: str | None = None,
    ) -> SingleHLTPredictionResponse:
        return SingleHLTHealthPredictionRequest(image_path=image_path).get_sync()

    @staticmethod
    def get_multiHLT_health_prediction(
        image_path: str | None = None,
    ) -> MultiHLTPredictionResponse:
        return MultiHLTHealthPredictionRequest(image_path=image_path).get_sync()


class AsyncCropHealthClient:
    @staticmethod
    async def get_binary_health_prediction(
        image_path: str | None = None,
    ) -> BinaryPredictionResponse:
        return await BinaryHealthPredictionRequest(image_path=image_path).get_async()

    @staticmethod
    async def get_singleHLT_health_prediction(
        image_path: str | None = None,
    ) -> SingleHLTPredictionResponse:
        return await SingleHLTHealthPredictionRequest(image_path=image_path).get_async()

    @staticmethod
    async def get_multiHLT_health_prediction(
        image_path: str | None = None,
    ) -> MultiHLTPredictionResponse:
        return await MultiHLTHealthPredictionRequest(image_path=image_path).get_async()
