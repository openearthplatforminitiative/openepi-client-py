from httpx import AsyncClient, Client
from pydantic import BaseModel, Field, model_validator, computed_field

from openepi_client import GeoLocation, openepi_settings
from openepi_client.agriculture._agriculture_types import Summary


class SummaryRequest(BaseModel):
    """
    Request model for agriculture data.

    Parameters
    ----------
    geolocation: GeoLocation
        The geolocation to query for

    Attributes
    ----------
    _agriculture_entpoint : str
        The API endpoint for sunrise requests.

    Methods
    -------
    _params()
        Generates the query parameters for the API request.
    get_sync()
        Synchronously retrieves the agriculture data.
    get_async()
        Asynchronously retrieves the agriculture data.
    """

    geolocation: GeoLocation = Field(..., description="The geolocation to query for")
    _agriculture_endpoint = f"{openepi_settings.api_root_url}/agriculture/summary"

    @computed_field
    @property
    def _params(self) -> dict:
        """
        Generates the query parameters for the API request.

        Returns
        -------
        dict
            The query parameters for the API request.
        """
        return {
            "lat": self.geolocation.lat,
            "lon": self.geolocation.lon,
        }

    def get_sync(self) -> Summary:
        """
        Synchronously retrieves agriculture Summary data.

        Returns
        -------
        Summary
            A summary of deforestation, flood, soil and
            weather data.
        """
        with Client() as client:
            response = client.get(self._agriculture_endpoint, params=self._params)
            return Summary(**response.json())

    async def get_async(self) -> Summary:
        """
        Asynchronously retrieves agriculture Summary data.

        Returns
        -------
        Summary
            A summary of deforestation, flood, soil and
            weather data.
        """
        async with AsyncClient() as async_client:
            response = await async_client.get(
                self._agriculture_endpoint, params=self._params
            )
            return Summary(**response.json())


class AgricultureClient:
    """
    Synchronous client for agriculture-related API requests.

    Methods
    -------
    get_summary(
        geolocation: GeoLocation | None = None,
    )
        Synchronously retrieves agriculture Summary data.
    """

    @staticmethod
    def get_summary(
        geolocation: GeoLocation | None = None,
    ) -> Summary:
        """
        Gets agriculture summary.


        Parameters
        ----------
        geolocation : GeoLocation, optional
            The geolocation to query for.

        Returns
        -------
        Summary
            A summary of deforestation, flood, soil and
            weather data.
        """
        return SummaryRequest(geolocation=geolocation).get_sync()


class AsyncAgricultureClient:
    """
    Asynchronous client for agriculture-related API requests.

    Methods
    ------
    """

    @staticmethod
    async def get_summary(
        geolocation: GeoLocation | None = None,
    ) -> Summary:
        """
        Gets agriculture summary.

        Parameters
        ----------
        geolocation : GeoLocation, optional
            The geolocation to query for.

        Returns
        -------
        Summary
            A summary of deforestation, flood, soil and
            weather data.
        """
        return await SummaryRequest(geolocation=geolocation).get_async()
