# GeneralService

A list of all methods in the `GeneralService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_up_status](#get_up_status)                     | ### Overview Simply gets if the TorBox API is available for use or not. Also might include information about downtimes. ### Authorization None needed.                                                                                                                                                                                                                                                                                                                                                                                                 |
| [get_stats](#get_stats)                             | ### Overview Simply gets general stats about the TorBox service. ### Authorization None needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [get_changelogs_rss_feed](#get_changelogs_rss_feed) | ### Overview Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for people who want updates on the TorBox changelog. Includes all the necessary items to make this compatible with RSS feed viewers for notifications, and proper HTML viewing. ### Authorization None needed.                                                                                                                                                                                       |
| [get_changelogs_json](#get_changelogs_json)         | ### Overview Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for developers who want to integrate the changelog into their apps for their users to see. Includes content in HTML and markdown for developers to easily render the text in a fancy yet simple way. ### Authorization None needed.                                                                                                                                                                  |
| [get_speedtest_files](#get_speedtest_files)         | ### Overview Gets CDN speedtest files. This can be used for speedtesting TorBox for users or other usages, such as checking download speeds for verification. Provides all necessary data such as region, server name, and even coordinates. Uses the requesting IP to determine if the server is the closest to the user. You also have the ability to choose between long tests or short tests via the "test_length" parameter. You may also force the region selection by passing the "region" as a specific region. ### Authorization None needed. |

## get_up_status

### Overview Simply gets if the TorBox API is available for use or not. Also might include information about downtimes. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/`

**Return Type**

`GetUpStatusOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.general.get_up_status()

print(result)
```

## get_stats

### Overview Simply gets general stats about the TorBox service. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/stats`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`GetStatsOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.general.get_stats(api_version="api_version")

print(result)
```

## get_changelogs_rss_feed

### Overview Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for people who want updates on the TorBox changelog. Includes all the necessary items to make this compatible with RSS feed viewers for notifications, and proper HTML viewing. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/changelogs/rss`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.general.get_changelogs_rss_feed(api_version="api_version")

print(result)
```

## get_changelogs_json

### Overview Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for developers who want to integrate the changelog into their apps for their users to see. Includes content in HTML and markdown for developers to easily render the text in a fancy yet simple way. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/changelogs/json`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`GetChangelogsJsonOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.general.get_changelogs_json(api_version="api_version")

print(result)
```

## get_speedtest_files

### Overview Gets CDN speedtest files. This can be used for speedtesting TorBox for users or other usages, such as checking download speeds for verification. Provides all necessary data such as region, server name, and even coordinates. Uses the requesting IP to determine if the server is the closest to the user. You also have the ability to choose between long tests or short tests via the "test_length" parameter. You may also force the region selection by passing the "region" as a specific region. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/speedtest`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                                                        |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                                                                    |
| test_length | str  | ❌       | Determines the size of the file used for the speedtest. May be "long" or "short". Optional.                                                                                                        |
| region      | str  | ❌       | Determines what cdns are returned. May be any region that TorBox is located in. To get this value, send a request without this value to determine all of the available regions that are available. |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.general.get_speedtest_files(
    api_version="api_version",
    test_length="string",
    region="string"
)

print(result)
```
