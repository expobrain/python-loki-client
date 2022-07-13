import asyncio
from functools import wraps

import click

from grafana_loki_client import Client
from grafana_loki_client.api.query import get_loki_api_v1_query


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.command()
@click.argument("url")
@coro
async def main(url: str) -> None:
    # Create client
    client = Client(base_url=url)

    # ----------------------------------------------------------------
    # Query
    # ----------------------------------------------------------------

    # Query
    query = query = '{app="test"}'
    query_response = await get_loki_api_v1_query.asyncio(client=client, query=query)
    assert query_response

    print(query_response)


if __name__ == "__main__":
    main()
