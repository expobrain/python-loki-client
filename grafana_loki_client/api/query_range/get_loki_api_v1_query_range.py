from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_loki_api_v1_query_range_direction import (
    GetLokiApiV1QueryRangeDirection,
)
from ...models.query_response_body import QueryResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    query: str,
    limit: Union[Unset, None, int] = 100,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    step: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, float] = UNSET,
    direction: Union[
        Unset, None, GetLokiApiV1QueryRangeDirection
    ] = GetLokiApiV1QueryRangeDirection.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = f"{client.base_url}/loki/api/v1/query_range"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_scope_org_id, Unset):
        headers["X-Scope-OrgID"] = x_scope_org_id

    params: Dict[str, Any] = {}
    params["query"] = query

    params["limit"] = limit

    params["start"] = start

    params["end"] = end

    params["step"] = step

    params["interval"] = interval

    json_direction: Union[Unset, None, str] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value if direction else None

    params["direction"] = json_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[QueryResponseBody]:
    if response.status_code == 200:
        response_200 = QueryResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[QueryResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    query: str,
    limit: Union[Unset, None, int] = 100,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    step: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, float] = UNSET,
    direction: Union[
        Unset, None, GetLokiApiV1QueryRangeDirection
    ] = GetLokiApiV1QueryRangeDirection.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Response[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (Union[Unset, None, int]):  Default: 100.
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):
        step (Union[Unset, None, str]):
        interval (Union[Unset, None, float]):
        direction (Union[Unset, None, GetLokiApiV1QueryRangeDirection]):  Default:
            GetLokiApiV1QueryRangeDirection.BACKWARD.
        x_scope_org_id (Union[Unset, str]):

    Returns:
        Response[QueryResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        query=query,
        limit=limit,
        start=start,
        end=end,
        step=step,
        interval=interval,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    query: str,
    limit: Union[Unset, None, int] = 100,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    step: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, float] = UNSET,
    direction: Union[
        Unset, None, GetLokiApiV1QueryRangeDirection
    ] = GetLokiApiV1QueryRangeDirection.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Optional[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (Union[Unset, None, int]):  Default: 100.
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):
        step (Union[Unset, None, str]):
        interval (Union[Unset, None, float]):
        direction (Union[Unset, None, GetLokiApiV1QueryRangeDirection]):  Default:
            GetLokiApiV1QueryRangeDirection.BACKWARD.
        x_scope_org_id (Union[Unset, str]):

    Returns:
        Response[QueryResponseBody]
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
        start=start,
        end=end,
        step=step,
        interval=interval,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    query: str,
    limit: Union[Unset, None, int] = 100,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    step: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, float] = UNSET,
    direction: Union[
        Unset, None, GetLokiApiV1QueryRangeDirection
    ] = GetLokiApiV1QueryRangeDirection.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Response[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (Union[Unset, None, int]):  Default: 100.
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):
        step (Union[Unset, None, str]):
        interval (Union[Unset, None, float]):
        direction (Union[Unset, None, GetLokiApiV1QueryRangeDirection]):  Default:
            GetLokiApiV1QueryRangeDirection.BACKWARD.
        x_scope_org_id (Union[Unset, str]):

    Returns:
        Response[QueryResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        query=query,
        limit=limit,
        start=start,
        end=end,
        step=step,
        interval=interval,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    query: str,
    limit: Union[Unset, None, int] = 100,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    step: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, float] = UNSET,
    direction: Union[
        Unset, None, GetLokiApiV1QueryRangeDirection
    ] = GetLokiApiV1QueryRangeDirection.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Optional[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (Union[Unset, None, int]):  Default: 100.
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):
        step (Union[Unset, None, str]):
        interval (Union[Unset, None, float]):
        direction (Union[Unset, None, GetLokiApiV1QueryRangeDirection]):  Default:
            GetLokiApiV1QueryRangeDirection.BACKWARD.
        x_scope_org_id (Union[Unset, str]):

    Returns:
        Response[QueryResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
            start=start,
            end=end,
            step=step,
            interval=interval,
            direction=direction,
            x_scope_org_id=x_scope_org_id,
        )
    ).parsed
