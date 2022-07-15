import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.direction import Direction
from ...models.query_response_body import QueryResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    query: str,
    limit: int = 100,
    time: Union[Unset, None, datetime.datetime] = UNSET,
    direction: Direction = Direction.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = f"{client.base_url}/loki/api/v1/query"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_scope_org_id, Unset):
        headers["X-Scope-OrgID"] = x_scope_org_id

    params: Dict[str, Any] = {}
    params["query"] = query

    params["limit"] = limit

    json_time: Union[Unset, None, str] = UNSET
    if not isinstance(time, Unset):
        json_time = time.isoformat() if time else None

    params["time"] = json_time

    json_direction = direction.value

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
    limit: int = 100,
    time: Union[Unset, None, datetime.datetime] = UNSET,
    direction: Direction = Direction.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Response[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (int):  Default: 100.
        time (Union[Unset, None, datetime.datetime]):
        direction (Direction):  Default: Direction.BACKWARD.
        x_scope_org_id (Union[Unset, str]):

    Returns:
        Response[QueryResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        query=query,
        limit=limit,
        time=time,
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
    limit: int = 100,
    time: Union[Unset, None, datetime.datetime] = UNSET,
    direction: Direction = Direction.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Optional[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (int):  Default: 100.
        time (Union[Unset, None, datetime.datetime]):
        direction (Direction):  Default: Direction.BACKWARD.
        x_scope_org_id (Union[Unset, str]):

    Returns:
        Response[QueryResponseBody]
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
        time=time,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    query: str,
    limit: int = 100,
    time: Union[Unset, None, datetime.datetime] = UNSET,
    direction: Direction = Direction.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Response[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (int):  Default: 100.
        time (Union[Unset, None, datetime.datetime]):
        direction (Direction):  Default: Direction.BACKWARD.
        x_scope_org_id (Union[Unset, str]):

    Returns:
        Response[QueryResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        query=query,
        limit=limit,
        time=time,
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
    limit: int = 100,
    time: Union[Unset, None, datetime.datetime] = UNSET,
    direction: Direction = Direction.BACKWARD,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Optional[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (int):  Default: 100.
        time (Union[Unset, None, datetime.datetime]):
        direction (Direction):  Default: Direction.BACKWARD.
        x_scope_org_id (Union[Unset, str]):

    Returns:
        Response[QueryResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
            time=time,
            direction=direction,
            x_scope_org_id=x_scope_org_id,
        )
    ).parsed
