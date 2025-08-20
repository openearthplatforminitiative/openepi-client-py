from http import HTTPMethod, HTTPStatus

import pytest

from openepi_client.global_forest_watch._get_dataset import GET_DATASET_ENDPOINT

from openepi_client.global_forest_watch import GlobalForestWatchClient
from tests.mocking import MockClient


class TestGetDataset:
    def test_get_dataset_ok(self):
        dataset_id = "test_dataset_id"

        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=f"{GET_DATASET_ENDPOINT}/{dataset_id}",
            status=HTTPStatus.OK,
            response={
                "data": {
                    "created_on": "2023-01-01T00:00:00Z",
                    "updated_on": "2023-01-02T00:00:00Z",
                    "dataset": "downloadable_dataset",
                    "is_downloadable": True,
                    "metadata": {
                        "tags": ["tag1", "tag2"],
                    },
                    "versions": ["1.0", "1.1"],
                },
                "status": "success",
            },
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        response = gfw.get_dataset(dataset_id=dataset_id)
        assert response.dataset == "downloadable_dataset"

    def test_get_dataset_not_found(self):
        dataset_id = "non_existent_dataset_id"

        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=f"{GET_DATASET_ENDPOINT}/{dataset_id}",
            status=HTTPStatus.NOT_FOUND,
            response={
                "message": "Dataset not found",
            },
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        response = gfw.get_dataset(dataset_id=dataset_id)
        assert response is None

    def test_get_dataset_error(self):
        dataset_id = "test_dataset_id"

        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=f"{GET_DATASET_ENDPOINT}/{dataset_id}",
            status=HTTPStatus.INTERNAL_SERVER_ERROR,
            response={
                "message": "A mock error message",
            },
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        with pytest.raises(ValueError) as exc_info:
            gfw.get_dataset(dataset_id=dataset_id)

        assert "A mock error message" in str(exc_info.value)
