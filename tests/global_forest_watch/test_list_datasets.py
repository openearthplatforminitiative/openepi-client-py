from http import HTTPMethod, HTTPStatus

import pytest

from openepi_client.global_forest_watch import GlobalForestWatchClient
from openepi_client.global_forest_watch._list_datasets import LIST_DATASETS_ENDPOINT
from tests.mocking import MockClient


class TestListDatasets:
    mock_response = {
        "data": [
            {
                "created_on": "2023-01-01T00:00:00Z",
                "updated_on": "2023-01-02T00:00:00Z",
                "dataset": "downloadable_dataset",
                "is_downloadable": True,
                "metadata": {
                    "tags": ["tag1", "tag2"],
                },
                "versions": ["1.0", "1.1"],
            },
            {
                "created_on": "2023-01-01T00:00:00Z",
                "updated_on": "2023-01-02T00:00:00Z",
                "dataset": "not_downloadable_dataset",
                "is_downloadable": False,
                "metadata": {
                    "tags": ["tag1", "tag2"],
                },
                "versions": ["1.0", "1.1"],
            },
        ],
        "status": "success",
        "links": {
            "self": LIST_DATASETS_ENDPOINT,
            "first": LIST_DATASETS_ENDPOINT,
            "last": LIST_DATASETS_ENDPOINT,
        },
        "meta": {
            "size": 10,
            "total_items": 2,
            "total_pages": 1,
        },
    }

    def test_list_datasets_no_paging_all(self):
        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=LIST_DATASETS_ENDPOINT,
            status=HTTPStatus.OK,
            response=self.mock_response,
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        response = gfw.list_datasets()
        assert len(response.datasets) == 2

    def test_list_datasets_no_paging_downloadable(self):
        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=LIST_DATASETS_ENDPOINT,
            status=HTTPStatus.OK,
            response=self.mock_response,
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        response = gfw.list_datasets(downloadable=True)
        assert len(response.datasets) == 1
        assert response.datasets[0].dataset == "downloadable_dataset"

    def test_list_datasets_paging_all(self):
        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=f"{LIST_DATASETS_ENDPOINT}?page[number]=1&page[size]=10",
            status=HTTPStatus.OK,
            response=self.mock_response,
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        response = gfw.list_datasets(page=1, page_size=10)
        assert len(response.datasets) == 2
        assert response.page_size == 10
        assert response.total_items == 2
        assert response.total_pages == 1

    def test_list_datasets_paging_downloadable(self):
        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=f"{LIST_DATASETS_ENDPOINT}?page[number]=1&page[size]=10",
            status=HTTPStatus.OK,
            response=self.mock_response,
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        response = gfw.list_datasets(page=1, page_size=10, downloadable=True)
        assert len(response.datasets) == 1
        assert response.datasets[0].dataset == "downloadable_dataset"
        assert response.page_size == 10
        assert response.total_items == 2
        assert response.total_pages == 1

    def test_list_datasets_error(self):
        mock = MockClient()
        mock.add_response(
            method=HTTPMethod.GET,
            url=LIST_DATASETS_ENDPOINT,
            status=HTTPStatus.BAD_REQUEST,
            response={"message": "A mocked error occured"},
        )

        gfw = GlobalForestWatchClient(http_client=mock.client())

        with pytest.raises(ValueError) as exc_info:
            gfw.list_datasets()

        assert "A mocked error occured" in str(exc_info.value)
