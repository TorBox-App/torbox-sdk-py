# RssFeedsService

A list of all methods in the `RssFeedsService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [add_rss_feed](#add_rss_feed)         | ### Overview ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                          |
| [control_rss_feed](#control_rss_feed) | ### Overview Controls an RSS Feed. By sending the RSS feed's ID and the type of operation you want to perform, it will perform said action on the RSS feed checker. Operations are either: - **Update** `forces an update on the rss feed` - **Delete** `deletes the rss feed from your account permanently` - **Pause** `pauses checking the rss feed on the scan interval` - **Resume** `resumes a paused rss feed` ### Authorization Requires an API key using the Authorization Bearer Header. |
| [modify_rss_feed](#modify_rss_feed)   | ### Overview ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                          |

## add_rss_feed

### Overview ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/rss/addrss`

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

result = sdk.rss_feeds.add_rss_feed(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## control_rss_feed

### Overview Controls an RSS Feed. By sending the RSS feed's ID and the type of operation you want to perform, it will perform said action on the RSS feed checker. Operations are either: - **Update** `forces an update on the rss feed` - **Delete** `deletes the rss feed from your account permanently` - **Pause** `pauses checking the rss feed on the scan interval` - **Resume** `resumes a paused rss feed` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/rss/controlrss`

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

result = sdk.rss_feeds.control_rss_feed(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## modify_rss_feed

### Overview ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/rss/modifyrss`

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

result = sdk.rss_feeds.modify_rss_feed(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```
