from geojson_pydantic import Polygon
from http import HTTPStatus, HTTPMethod
from openepi_client.global_forest_watch import (
    GlobalForestWatchClient,
    GFWDataset,
    GFWPagedDatasetResponse,
    GFWVersion,
    GFWRasterField,
    GFWQueryResponse,
    GFWAsset,
    GFWAssetType,
    GFWAccountInfo,
    GFWApiKey,
)

from openepi_client.global_forest_watch._create_apikey import (
    TOKEN_ENDPOINT,
    API_KEY_ENDPOINT,
)

from tests.mocking import MockClient


class TestCreateAccount:
    def test_create_account_ok(self):
        name: str = "Test Testingbuddy"
        email: str = "test@testingbuddy.com"

        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.POST,
            url="https://data-api.globalforestwatch.org/auth/sign-up",
            status=HTTPStatus.OK,
            response={
                "data": {
                    "id": "12345",
                    "name": name,
                    "email": email,
                    "createdAt": "2023-10-01T00:00:00Z",
                }
            },
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        account_info: GFWAccountInfo = gfw.create_account(name, email)

        assert account_info.name == name
        assert account_info.email == email

    def test_create_account_error(self):
        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.POST,
            url="https://data-api.globalforestwatch.org/auth/sign-up",
            status=HTTPStatus.BAD_REQUEST,
            response={"message": "Invalid email address"},
        )
        gfw = GlobalForestWatchClient(http_client=mock.client())
        try:
            gfw.create_account(name="Test Testingbuddy", email="invalid-email")
        except ValueError as e:
            assert str(e) == "Failed to create account: Invalid email address"
        else:
            assert False, "Expected ValueError was not raised"
