# python-loki-client

> WARNING: This is a beta release of the loki-client, the client is incomplete.

![main build status](https://github.com/expobrain/python-loki-client/actions/workflows/main.yml/badge.svg?branch=main)

A client library for accessing Grafana Loki APIs.

## Installation

To install the client:

```shell
pip install python-loki-client
```

## Implemented endpoints

This client is still incomplete and implements only the following endpoints:

- `GET /loki/api/v1/query`
- `GET /loki/api/v1/query_range`

## Usage

First, create a client:

```python
from grafana_loki_client import Client

client = Client(base_url="https://loki.grafana.com")
```

Now call your endpoint and use your models:

```python
from grafana_loki_client.models import MyDataModel
from grafana_loki_client.api.my_tag import get_my_data_model
from grafana_loki_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from grafana_loki_client.models import MyDataModel
from grafana_loki_client.api.my_tag import get_my_data_model
from grafana_loki_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = Client(
    base_url="https://internal_loki.grafana.com",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = Client(
    base_url="https://internal_loki.grafana.com", verify_ssl=False
)
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:

   1. `sync`: Blocking request that returns parsed data (if successful) or `None`
   1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
   1. `asyncio`: Like `sync` but the async instead of blocking
   1. `asyncio_detailed`: Like `sync_detailed` by async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `grafana_loki_client.api.default`

## Generate code

This client is automatically generated from the OpenAPI 3.x specs manually defined in `grafana_loki_openapi.yaml`.

APIs are manually declared in the YAML file by reading the Grafana [Loki API's documentation](https://grafana.com/docs/loki/latest/api/).

A code generator tool will use the OpenAPI document to generates a sync/async client.

To generare an updated copy of the client:

```shell
poetry install
poetry run make generate
```
