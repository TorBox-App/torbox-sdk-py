# QueuedService

A list of all methods in the `QueuedService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_queued_downloads](#get_queued_downloads)         | ### Overview Retrieves all of a user's queued downloads by type. If you want to get all 3 types, "torrent", "usenet" and "webdl" then you will need to run this request 3 times, each with the different type. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                   |
| [control_queued_downloads](#control_queued_downloads) | ### Overview Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent. Operations are either: - **Delete** `deletes the queued download from your account` - **Start** `starts a queued download, cannot be used with the "all" parameter` ### Authorization Requires an API key using the Authorization Bearer Header. |

## get_queued_downloads

### Overview Retrieves all of a user's queued downloads by type. If you want to get all 3 types, "torrent", "usenet" and "webdl" then you will need to run this request 3 times, each with the different type. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/queued/getqueued`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                   |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                                                                                                               |
| bypass_cache | str  | ❌       | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. |
| id\_         | str  | ❌       | Determines the queued download requested, will return an object rather than list. Optional.                                                                                                   |
| offset       | str  | ❌       | Determines the offset of items to get from the database. Default is 0. Optional.                                                                                                              |
| limit        | str  | ❌       | Determines the number of items to recieve per request. Default is 1000. Optional.                                                                                                             |
| type\_       | str  | ❌       | The type of the queued download you want to retrieve. Can be "torrent", "usenet" or "webdl". Optional. Default is "torrent".                                                                  |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.queued.get_queued_downloads(
    api_version="api_version",
    bypass_cache="boolean",
    id_="integer",
    offset="integer",
    limit="integer",
    type_="string"
)

print(result)
```

## control_queued_downloads

### Overview Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent. Operations are either: - **Delete** `deletes the queued download from your account` - **Start** `starts a queued download, cannot be used with the "all" parameter` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/queued/controlqueued`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | any  | ❌       | The request body. |
| api_version  | str  | ✅       |                   |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi
from torbox_api.models import any

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

request_body = ""

result = sdk.queued.control_queued_downloads(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```
