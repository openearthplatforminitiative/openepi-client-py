from httpx import Client
from pydantic import Field
from geojson_pydantic.geometries import Geometry

from openepi_client import openepi_settings, BaseModel
from ._gfw_types import GFWAdminGeostore


CREATE_GEOSTORE_ENDPOINT: str = f"{openepi_settings.gfw_api_url}/geostore"


class CreateGeostoreRequest(BaseModel):
    geometry: Geometry = Field(..., description="The geometry to create a geostore for")
    http_client: Client = Field(..., description="HTTP client for making requests")

    def post_sync(self) -> GFWAdminGeostore:
        with self.http_client as client:
            response = client.post(
                url=CREATE_GEOSTORE_ENDPOINT,
                json={"geojson": self.geometry.model_dump(exclude={"bbox"})},
                headers={"x-api-key": openepi_settings.gfw_api_key},
            )

            json = response.json()
            if response.status_code != 201:
                raise ValueError(
                    f"Failed to create geoStore: {json.get('message', 'Unknown error')}"
                )

            response = GFWAdminGeostore(**json.get("data", {}))
            response.status = json.get("status", "unknown")
            return response
