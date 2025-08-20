from http import HTTPStatus, HTTPMethod
from urllib import response, parse

import httpx
from httpx import Client
from httpx import MockTransport


class MockResponse:
    def __init__(self, status: HTTPStatus, response: dict = None):
        self.status = status
        self.response = response or {}


class MockClient:
    def __init__(self):
        self.responses = {}

    def add_response(
        self, method: HTTPMethod, url: str, status: HTTPStatus, response: dict
    ):
        self.responses[(method, url)] = MockResponse(status, response)

    def client(self) -> Client:
        def transport(request):
            decoded_url = parse.unquote(str(request.url))
            mock = self.responses.get((request.method, decoded_url))
            if mock:
                return httpx.Response(
                    status_code=mock.status,
                    json=mock.response,
                    request=request,
                )
            return httpx.Response(
                status_code=404,
                json={"message": "Not Found"},
                request=request,
            )

        return Client(transport=MockTransport(transport))
