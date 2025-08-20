import pytest
from unittest.mock import patch
from http import HTTPStatus, HTTPMethod

from geojson_pydantic import Polygon
from geojson_pydantic.features import Feature
from geojson_pydantic.features import FeatureCollection

from openepi_client.global_forest_watch import (
    GlobalForestWatchClient,
    GFWAdminGeostore,
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

    def test_create_geostore_with_geometry_ok(self):
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
            api_key="test_api_key",
            http_client=mock.client(),
        )
        created_geostore = gfw.create_geostore(
            geojson=Polygon(
                type="Polygon",
                coordinates=self.coordinates,
            )
        )

        assert (
            created_geostore.attributes.geojson.features[0].geometry.coordinates
            == self.coordinates
        )

    def test_create_geostore_error(self):
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

        gfw = GlobalForestWatchClient(api_key="test_api_key", http_client=mock.client())
        with pytest.raises(ValueError) as exc_info:
            gfw.create_geostore(
                geojson=Polygon(
                    type="Polygon",
                    coordinates=self.coordinates,
                )
            )

        assert "Invalid geometry" in str(exc_info.value)
