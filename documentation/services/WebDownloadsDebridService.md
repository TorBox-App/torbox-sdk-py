# WebDownloadsDebridService

A list of all methods in the `WebDownloadsDebridService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :---------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_web_download](#create_web_download)                                   | ### Overview Creates a web download under your account. Simply send a link to any file on the internet. Once it has been checked, it will begin downloading assuming your account has available active download slots, and they aren't too large. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [control_web_download](#control_web_download)                                 | ### Overview Controls a web download. By sending the web download's ID and the type of operation you want to perform, it will send that request to the debrid client. Operations are either: - **Delete** `deletes the download from the client and your account permanently` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [request_download_link2](#request_download_link2)                             | ### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 1 hour for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_web_download_list](#get_web_download_list)                               | ### Overview Gets the user's web download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live web downloads. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [get_web_download_cached_availability](#get_web_download_cached_availability) | ### Overview Takes in a list of comma separated usenet hashes and checks if the web download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. To get the hash of a web download, pass the link through an md5 hash algo and it will return the proper hash for it. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [get_hoster_list](#get_hoster_list)                                           | ### Overview A dynamic list of hosters that TorBox is capable of downloading through its paid service. - Name - a clean name for display use, the well known name of the service, should be recognizable to users. - Domains - an array of known domains that the hoster uses. While each may serve a different purpose it is still included. - URL - the main url of the service. This should take you to the home page or a service page of the hoster. - Icon - a square image, usually a favicon or logo, that represents the service, should be recognizable as the hoster's icon. - Status - whether this hoster can be used on TorBox or not at the current time. It is usually a good idea to check this value before submitting a download to TorBox's servers for download. - Type - values are either "hoster" or "stream". Both do the same thing, but is good to differentiate services used for different things. - Note - a string value (or null) that may give helpful information about the current status or state of a hoster. This can and should be shown to end users. - Daily Link Limit - the number of downloads a user can use per day. As a user submits links, once they hit this number, the API will deny them from adding anymore of this type of link. A zero value means that it is unlimited. - Daily Link Used - the number of downloads a user has already used. This endpoint currently doesn't update this value. - Daily Bandwidth Limit - the value in bytes that a user is allowed to download from this hoster. A zero value means that it is unlimited. This endpoint doesn't currently implement this limit. It is recommended to use the Daily Link Limit instead. - Daily Bandwdith Used - the value in btes that a user has already used to download from this hoster. This endpoint currently doesn't update this value. ### Authorization Requires an API key using the Authorization Bearer Header. |

## create_web_download

### Overview Creates a web download under your account. Simply send a link to any file on the internet. Once it has been checked, it will begin downloading assuming your account has available active download slots, and they aren't too large. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/webdl/createwebdownload`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateWebDownloadRequest](../models/CreateWebDownloadRequest.md) | ❌       | The request body. |
| api_version  | str                                                               | ✅       |                   |

**Return Type**

`CreateWebDownloadOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi
from torbox_api.models import CreateWebDownloadRequest

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

request_body = CreateWebDownloadRequest(
    link="link"
)

result = sdk.web_downloads_debrid.create_web_download(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## control_web_download

### Overview Controls a web download. By sending the web download's ID and the type of operation you want to perform, it will send that request to the debrid client. Operations are either: - **Delete** `deletes the download from the client and your account permanently` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/webdl/controlwebdownload`

**Parameters**

| Name         | Type | Required | Description                                                                              |
| :----------- | :--- | :------- | :--------------------------------------------------------------------------------------- |
| request_body | any  | ❌       | The request body.                                                                        |
| api_version  | str  | ✅       |                                                                                          |
| bypass_cache | str  | ❌       |                                                                                          |
| id\_         | str  | ❌       | Determines the web download requested, will return an object rather than list. Optional. |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi
from torbox_api.models import any

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

request_body = ""

result = sdk.web_downloads_debrid.control_web_download(
    request_body=request_body,
    api_version="api_version",
    bypass_cache="boolean",
    id_="integer"
)

print(result)
```

## request_download_link2

### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 1 hour for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/requestdl`

**Parameters**

| Name         | Type | Required | Description                                                                                      |
| :----------- | :--- | :------- | :----------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                  |
| token        | str  | ❌       | Your API Key                                                                                     |
| web_id       | str  | ❌       | The web download's ID that you want to download                                                  |
| file_id      | str  | ❌       | The files's ID that you want to download                                                         |
| zip_link     | str  | ❌       | If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given. |
| torrent_file | str  | ❌       | If you want a .torrent file to be downloaded. Does not work with the zip_link option. Optional.  |
| user_ip      | str  | ❌       | The user's IP to determine the closest CDN. Optional.                                            |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.web_downloads_debrid.request_download_link2(
    api_version="api_version",
    token="{{api_key}}",
    web_id="{{webdl_id}}",
    file_id="{{usenet_file_id}}",
    zip_link="boolean",
    torrent_file="boolean",
    user_ip="string"
)

print(result)
```

## get_web_download_list

### Overview Gets the user's web download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live web downloads. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/mylist`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                   |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                                                                                                               |
| bypass_cache | str  | ❌       | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. |
| id\_         | str  | ❌       | Determines the torrent requested, will return an object rather than list. Optional.                                                                                                           |
| offset       | str  | ❌       | Determines the offset of items to get from the database. Default is 0. Optional.                                                                                                              |
| limit        | str  | ❌       | Determines the number of items to recieve per request. Default is 1000. Optional.                                                                                                             |

**Return Type**

`GetWebDownloadListOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.web_downloads_debrid.get_web_download_list(
    api_version="api_version",
    bypass_cache="boolean",
    id_="integer",
    offset="integer",
    limit="integer"
)

print(result)
```

## get_web_download_cached_availability

### Overview Takes in a list of comma separated usenet hashes and checks if the web download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. To get the hash of a web download, pass the link through an md5 hash algo and it will return the proper hash for it. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/checkcached`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                              |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                          |
| hash        | str  | ❌       | The list of web hashes you want to check. Comma seperated. To find the hash, md5 the link.                                                               |
| format      | str  | ❌       | Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list. |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.web_downloads_debrid.get_web_download_cached_availability(
    api_version="api_version",
    hash="{{webdl_hash}}",
    format="object"
)

print(result)
```

## get_hoster_list

### Overview A dynamic list of hosters that TorBox is capable of downloading through its paid service. - Name - a clean name for display use, the well known name of the service, should be recognizable to users. - Domains - an array of known domains that the hoster uses. While each may serve a different purpose it is still included. - URL - the main url of the service. This should take you to the home page or a service page of the hoster. - Icon - a square image, usually a favicon or logo, that represents the service, should be recognizable as the hoster's icon. - Status - whether this hoster can be used on TorBox or not at the current time. It is usually a good idea to check this value before submitting a download to TorBox's servers for download. - Type - values are either "hoster" or "stream". Both do the same thing, but is good to differentiate services used for different things. - Note - a string value (or null) that may give helpful information about the current status or state of a hoster. This can and should be shown to end users. - Daily Link Limit - the number of downloads a user can use per day. As a user submits links, once they hit this number, the API will deny them from adding anymore of this type of link. A zero value means that it is unlimited. - Daily Link Used - the number of downloads a user has already used. This endpoint currently doesn't update this value. - Daily Bandwidth Limit - the value in bytes that a user is allowed to download from this hoster. A zero value means that it is unlimited. This endpoint doesn't currently implement this limit. It is recommended to use the Daily Link Limit instead. - Daily Bandwdith Used - the value in btes that a user has already used to download from this hoster. This endpoint currently doesn't update this value. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/hosters`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`GetHosterListOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.web_downloads_debrid.get_hoster_list(api_version="api_version")

print(result)
```
