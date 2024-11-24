# TorrentsService

A list of all methods in the `TorrentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_torrent](#create_torrent)                                     | ### Overview Creates a torrent under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [control_torrent](#control_torrent)                                   | ### Overview Controls a torrent. By sending the torrent's ID and the type of operation you want to perform, it will send that request to the torrent client. Operations are either: - **Reannounce** `reannounces the torrent to get new peers` - **Delete** `deletes the torrent from the client and your account permanently` - **Resume** `resumes a paused torrent` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [control_queued_torrent](#control_queued_torrent)                     | ### Overview Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent. Operations are either: - **Delete** `deletes the queued torrent from your account` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [request_download_link](#request_download_link)                       | ### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 1 hour for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [get_torrent_list](#get_torrent_list)                                 | ### Overview Gets the user's torrent list. This gives you the needed information to perform other torrent actions. This information only gets updated every 600 seconds, or when the _Request Update On Torrent_ request is sent to the _relay API_. #### Download States: - "downloading" -\> The torrent is currently downloading. - "uploading" -\> The torrent is currently seeding. - "stalled (no seeds)" -\> The torrent is trying to download, but there are no seeds connected to download from. - "paused" -\> The torrent is paused. - "completed" -\> The torrent is completely downloaded. Do not use this for download completion status. - "cached" -\> The torrent is cached from the server. - "metaDL" -\> The torrent is downloading metadata from the hoard. - "checkingResumeData" -\> The torrent is checking resumable data. All other statuses are basic qBittorrent states. [Check out here for the full list](<https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management>). ### Authorization Requires an API key using the Authorization Bearer Header. |
| [get_torrent_cached_availability](#get_torrent_cached_availability)   | ### Overview Takes in a list of comma separated torrent hashes and checks if the torrent is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                         |
| [search_all_torrents_from_scraper](#search_all_torrents_from_scraper) | ### Overview Uses Meilisearch to search for scraped torrents. This is a basic torrent aggregator system and has no real relation to TorBox. It is simply a tool you can use. It does not have cache information, or anything special like that, and will not have any of that information. This is simply a torrent search, nothing more. You may use this for anything. TorBox uses it in the website to make it easy for users to find torrents without having to go and find them on sketchy websites. ### Authorization None required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [export_torrent_data](#export_torrent_data)                           | ### Overview Exports the magnet or torrent file. Requires a type to be passed. If type is **magnet**, it will return a JSON response with the magnet as a string in the _data_ key. If type is **file**, it will return a bittorrent file as a download. Not compatible with cached downloads. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [get_torrent_info](#get_torrent_info)                                 | ### Overview A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant. ### Authorization None required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [get_queued_torrents](#get_queued_torrents)                           | ### Overview Retrieves all of a user's queued torrents. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## create_torrent

### Overview Creates a torrent under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/createtorrent`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateTorrentRequest](../models/CreateTorrentRequest.md) | ❌       | The request body. |
| api_version  | str                                                       | ✅       |                   |

**Return Type**

`CreateTorrentOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi
from torbox_api.models import CreateTorrentRequest

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

request_body = CreateTorrentRequest(
    file="file",
    magnet="magnet"
)

result = sdk.torrents.create_torrent(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## control_torrent

### Overview Controls a torrent. By sending the torrent's ID and the type of operation you want to perform, it will send that request to the torrent client. Operations are either: - **Reannounce** `reannounces the torrent to get new peers` - **Delete** `deletes the torrent from the client and your account permanently` - **Resume** `resumes a paused torrent` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/controltorrent`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | any  | ❌       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`ControlTorrentOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi
from torbox_api.models import any

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

request_body = ""

result = sdk.torrents.control_torrent(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## control_queued_torrent

### Overview Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent. Operations are either: - **Delete** `deletes the queued torrent from your account` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/controlqueued`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | any  | ❌       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`ControlQueuedTorrentOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi
from torbox_api.models import any

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

request_body = ""

result = sdk.torrents.control_queued_torrent(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## request_download_link

### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 1 hour for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/requestdl`

**Parameters**

| Name         | Type | Required | Description                                                                                      |
| :----------- | :--- | :------- | :----------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                  |
| token        | str  | ❌       | Your API Key                                                                                     |
| torrent_id   | str  | ❌       | The torrent's ID that you want to download                                                       |
| file_id      | str  | ❌       | The files's ID that you want to download                                                         |
| zip_link     | str  | ❌       | If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given. |
| torrent_file | str  | ❌       | If you want a .torrent file to be downloaded. Does not work with the zip_link option. Optional.  |

**Return Type**

`RequestDownloadLinkOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.torrents.request_download_link(
    api_version="api_version",
    token="{{api_key}}",
    torrent_id="{{torrent_id}}",
    file_id="{{torrent_file_id}}",
    zip_link="boolean",
    torrent_file="boolean"
)

print(result)
```

## get_torrent_list

### Overview Gets the user's torrent list. This gives you the needed information to perform other torrent actions. This information only gets updated every 600 seconds, or when the _Request Update On Torrent_ request is sent to the _relay API_. #### Download States: - "downloading" -\> The torrent is currently downloading. - "uploading" -\> The torrent is currently seeding. - "stalled (no seeds)" -\> The torrent is trying to download, but there are no seeds connected to download from. - "paused" -\> The torrent is paused. - "completed" -\> The torrent is completely downloaded. Do not use this for download completion status. - "cached" -\> The torrent is cached from the server. - "metaDL" -\> The torrent is downloading metadata from the hoard. - "checkingResumeData" -\> The torrent is checking resumable data. All other statuses are basic qBittorrent states. [Check out here for the full list](<https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management>). ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/mylist`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                   |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                                                                                                               |
| bypass_cache | str  | ❌       | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. |
| id\_         | str  | ❌       | Determines the torrent requested, will return an object rather than list. Optional.                                                                                                           |
| offset       | str  | ❌       | Determines the offset of items to get from the database. Default is 0. Optional.                                                                                                              |
| limit        | str  | ❌       | Determines the number of items to recieve per request. Default is 1000. Optional.                                                                                                             |

**Return Type**

`GetTorrentListOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.torrents.get_torrent_list(
    api_version="api_version",
    bypass_cache="boolean",
    id_="integer",
    offset="integer",
    limit="integer"
)

print(result)
```

## get_torrent_cached_availability

### Overview Takes in a list of comma separated torrent hashes and checks if the torrent is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/checkcached`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                              |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                          |
| hash        | str  | ❌       | The list of torrent hashes you want to check. Comma seperated.                                                                                           |
| format      | str  | ❌       | Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list. |
| list_files  | str  | ❌       | Allows you to list the files found inside the cached data.                                                                                               |

**Return Type**

`GetTorrentCachedAvailabilityOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.torrents.get_torrent_cached_availability(
    api_version="api_version",
    hash="{{torrent_hash}}",
    format="object",
    list_files="boolean"
)

print(result)
```

## search_all_torrents_from_scraper

### Overview Uses Meilisearch to search for scraped torrents. This is a basic torrent aggregator system and has no real relation to TorBox. It is simply a tool you can use. It does not have cache information, or anything special like that, and will not have any of that information. This is simply a torrent search, nothing more. You may use this for anything. TorBox uses it in the website to make it easy for users to find torrents without having to go and find them on sketchy websites. ### Authorization None required.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/search`

**Parameters**

| Name        | Type | Required | Description                       |
| :---------- | :--- | :------- | :-------------------------------- |
| api_version | str  | ✅       |                                   |
| query       | str  | ❌       | The query you want to search for. |

**Return Type**

`SearchAllTorrentsFromScraperOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.torrents.search_all_torrents_from_scraper(
    api_version="api_version",
    query="{{search_query}}"
)

print(result)
```

## export_torrent_data

### Overview Exports the magnet or torrent file. Requires a type to be passed. If type is **magnet**, it will return a JSON response with the magnet as a string in the _data_ key. If type is **file**, it will return a bittorrent file as a download. Not compatible with cached downloads. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/exportdata`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                                                                             |
| :---------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                                                                                         |
| torrent_id  | str  | ❌       | The torrent's ID.                                                                                                                                                                                                       |
| type\_      | str  | ❌       | Either "magnet" or "file". Tells how the API what to get, and what to respond as. If magnet, it returns a JSON response with the magnet as a string in the data key. If file, it responds with a torrent file download. |

**Return Type**

`ExportTorrentDataOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.torrents.export_torrent_data(
    api_version="api_version",
    torrent_id="int",
    type_="str"
)

print(result)
```

## get_torrent_info

### Overview A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant. ### Authorization None required.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/torrentinfo`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                                                          |
| :---------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                                                                      |
| hash        | str  | ❌       | Hash of the torrent you want to get info for. This is required.                                                                                                                                      |
| timeout     | str  | ❌       | The amount of time you want TorBox to search for the torrent on the Bittorrent network. If the number of seeders is low or even zero, this value may be helpful to move up. Default is 10. Optional. |

**Return Type**

`GetTorrentInfoOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.torrents.get_torrent_info(
    api_version="api_version",
    hash="string",
    timeout="integer"
)

print(result)
```

## get_queued_torrents

### Overview Retrieves all of a user's queued torrents. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/getqueued`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.torrents.get_queued_torrents(api_version="api_version")

print(result)
```
