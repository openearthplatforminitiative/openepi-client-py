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


class TestCreateApiKey:
    def test_create_api_key_ok(self):
        email = "test@testbuddy.com"
        password = "12345678"
        domains = ["example.com"]
        alias = "test_alias"
        organization = "test_org"
        api_key_value = "1234567890abcdef"

        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.POST,
            url=TOKEN_ENDPOINT,
            status=HTTPStatus.OK,
            response={
                "data": {"access_token": "test_access_token", "token_type": "Bearer"}
            },
        )

        mock.add_response(
            method=HTTPMethod.POST,
            url=API_KEY_ENDPOINT,
            status=HTTPStatus.CREATED,
            response={
                "data": {
                    "created_on": "2025-10-01T00:00:00Z",
                    "updated_on": "2025-10-01T00:00:00Z",
                    "alias": alias,
                    "user_id": "api_key_id",
                    "api_key": api_key_value,
                    "organization": organization,
                    "email": email,
                    "domains": domains,
                    "expires_on": "2025-11-01T00:00:00Z",
                }
            },
        )

        gfw = GlobalForestWatchClient(
            email=email, password=password, http_client=mock.client()
        )
        api_key: GFWApiKey = gfw.create_api_key(alias, organization, domains)

        assert api_key.alias == alias
        assert api_key.organization == organization
        assert api_key.email == email
        assert api_key.domains == domains
        assert api_key.api_key == api_key_value

    def test_create_api_key_token_error(self):
        email = "test@testbuddy.com"
        password = "12345678"
        domains = ["example.com"]
        alias = "test_alias"
        organization = "test_org"
        api_key_value = "1234567890abcdef"

        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.POST,
            url=TOKEN_ENDPOINT,
            status=HTTPStatus.UNAUTHORIZED,
            response={"message": "Authentication failed"},
        )

        gfw = GlobalForestWatchClient(
            email=email, password=password, http_client=mock.client()
        )
        try:
            api_key: GFWApiKey = gfw.create_api_key(alias, organization, domains)
        except ValueError as e:
            assert str(e) == "Failed to get access token: Authentication failed"
        else:
            assert False, "Expected ValueError was not raised"
