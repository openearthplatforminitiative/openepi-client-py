import pytest
from unittest.mock import patch
from http import HTTPStatus, HTTPMethod

from geojson_pydantic import Polygon

from openepi_client.global_forest_watch import (
    GlobalForestWatchClient,
)
from openepi_client.global_forest_watch._create_geostore import CREATE_GEOSTORE_ENDPOINT
from tests.mocking import MockClient


class TestCreateGeostore:
    coordinates = [
        [
            (103.19732666015625, 0.5537709801264608),
            (103.24882507324219, 0.5647567848663363),
            (103.21277618408203, 0.5932511181408705),
            (103.19732666015625, 0.5537709801264608),
        ]
    ]

    @patch("openepi_client.global_forest_watch._create_geostore.openepi_settings")
    def test_create_geostore_ok(self, openepi_settings_mock):
        openepi_settings_mock.gfw_api_key = "test_api_key"

        email = "test@testbuddy.com"
        password = "12345678"
        mock = MockClient()

        mock.add_response(
            method=HTTPMethod.POST,
            url=CREATE_GEOSTORE_ENDPOINT,
            status=HTTPStatus.CREATED,
            response={
                "data": {
                    "type": "geoStore",
                    "id": "geostore_id",
                    "attributes": {
                        "geojson": {
                            "type": "FeatureCollection",
                            "features": [
                                {
                                    "type": "Feature",
                                    "geometry": {
                                        "type": "Polygon",
                                        "coordinates": self.coordinates,
                                    },
                                    "properties": {},
                                }
                            ],
                        },
                    },
                },
                "status": "success",
            },
        )

        gfw = GlobalForestWatchClient(
            email=email, password=password, http_client=mock.client()
        )
        created_geostore = gfw.create_geostore(
            geometry=Polygon(
                type="Polygon",
                coordinates=self.coordinates,
            )
        )

        assert (
            created_geostore.attributes.geojson.features[0].geometry.coordinates
            == self.coordinates
        )

    @patch("openepi_client.global_forest_watch._create_geostore.openepi_settings")
    def test_create_geostore_error(self, openepi_settings_mock):
        openepi_settings_mock.gfw_api_key = "test_api_key"

        email = "test@testbuddy.com"
        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.POST,
            url=CREATE_GEOSTORE_ENDPOINT,
            status=HTTPStatus.BAD_REQUEST,
            response={
                "message": "Invalid geometry",
                "status": "error",
            },
        )

        gfw = GlobalForestWatchClient(email=email, http_client=mock.client())
        with pytest.raises(ValueError) as exc_info:
            gfw.create_geostore(
                geometry=Polygon(
                    type="Polygon",
                    coordinates=self.coordinates,
                )
            )

        assert "Invalid geometry" in str(exc_info.value)
