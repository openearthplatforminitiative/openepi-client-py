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
from openepi_client.global_forest_watch._get_geostore import GET_GEOSTORE_ENDPOINT
from tests.mocking import MockClient


class TestGetGeostore:
    coordinates = [
        [
            (103.19732666015625, 0.5537709801264608),
            (103.24882507324219, 0.5647567848663363),
            (103.21277618408203, 0.5932511181408705),
            (103.19732666015625, 0.5537709801264608),
        ]
    ]

    def test_get_geostore(self):
        geostore_id = "geostore_id"

        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=f"{GET_GEOSTORE_ENDPOINT}/{geostore_id}",
            status=HTTPStatus.OK,
            response={
                "data": {
                    "type": "geoStore",
                    "id": geostore_id,
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
        retrieved_geostore = gfw.get_geostore(geostore_id)

        assert (
            retrieved_geostore.attributes.geojson.features[0].geometry.coordinates
            == self.coordinates
        )
