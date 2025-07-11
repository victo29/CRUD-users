from fastapi import Request

from typing import Callable

from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

async def request_adapter(request: Request, controller: Callable) -> HttpResponse:
    body = None
    if request.headers.get("content-type", "").startswith("application/json"):
        body = await request.json()

    http_request = HttpRequest(
        body=body,
        headers=dict(request.headers),
        query_params=dict(request.query_params),
        path_params=request.path_params,
        url=str(request.url),
    )

    http_response = controller(http_request)
    return http_response
