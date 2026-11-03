# MainApiSdk Python SDK 1.0.0<a id="mainapisdk-python-sdk-100"></a>

Welcome to the MainApiSdk SDK documentation. This guide will help you get started with integrating and using the MainApiSdk SDK in your project.

## Versions<a id="versions"></a>

- SDK version: `1.0.0`

## About the API<a id="about-the-api"></a>

### Full documentation for TorBox<a id="full-documentation-for-torbox"></a>

Current API Base: `https://api.torbox.app`

Current API Version: `v1`

You can find more API docs here: [http://api.torbox.app/docs](http://api.torbox.app/docs) (they aren't as great as these, but is in a format most people would be familiar to).

### General Information<a id="general-information"></a>

- You can rely on both `success` booleans or status codes to determine if a call was a success. Status code `200` always means a success. `403` means authentication error. `500` means something went wrong on TorBox's end. `400` means the user did something wrong, or an input wasn't correct, or expected.
- There will always be a user-friendly message in `detail` for a reason why a call was a failure, or a success message. You may forward these directly to users.
- The `/usenet` and the `/webdl` API endpoints are nearly the same as the `/torrents` API endpoints apart from some different named inputs and outputs.
- All outputs are JSON unless otherwise specified. Check out the examples to be sure.

### Rate Limits<a id="rate-limits"></a>

- Unless stated below, all endpoints are rate limited to **300/min** per API token, no edge rate limiting.
- `POST` /torrents/createtorrent is rate limited to **60/hour** for uncached items per API token, **300/min** if the items are cached. Please read the documentation for more information.
- `POST` /usenet/createusenetdownload is rate limited to **60/hour** per API token.
- `POST` /webdl/createwebdownload is rate limited to **60/hour** per API token.
- We no longer accept IP whitelisting requests due to rate limiting being API token based, rather than IP based.

### Standard Response<a id="standard-response"></a>

Below is the standard JSON response that most requests will return. In short, always use the "success" key to determine if a request was successful or not, "error" to determine the exact error reason, "detail" as a user-friendly message whether success or error, and data contains the response information you are looking for.

```json
{
    "success": boolean, // whether a response is successful or not
    "error": string, // an error code if there was an error, or null if success
    "detail": string, // a user-friendly message
    "data": any // usually an object/dict, but can be anything, check the examples
}

```

### Errors Table<a id="errors-table"></a>

Errors codes are part of the standard response type. If the code ends in "ERROR", the error is the server's fault else that error is something that the client caused.

| **Error Code**             | Error Meaning                                                                                                                                                                                                                                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DATABASE_ERROR             | Could not access internal database/memory store information.                                                                                                                                                                                                                                                     |
| UNKNOWN_ERROR              | The reason for the error is unknown. Usually there will be error data attached in the "data" key. In these cases please report the request to [contact@torbox.app](https://mailto:contact@torbox.app).                                                                                                           |
| NO_AUTH                    | There are no provided credentials.                                                                                                                                                                                                                                                                               |
| BAD_TOKEN                  | The provided token is invalid.                                                                                                                                                                                                                                                                                   |
| AUTH_ERROR                 | There was an error verifying the given authentication.                                                                                                                                                                                                                                                           |
| INVALID_OPTION             | The provided option is invalid.                                                                                                                                                                                                                                                                                  |
| REDIRECT_ERROR             | The server tried redirecting, but it faulted.                                                                                                                                                                                                                                                                    |
| OAUTH_VERIFICATION_ERROR   | The server tried verifying your OAuth token, but it was not accepted by the provider.                                                                                                                                                                                                                            |
| ENDPOINT_NOT_FOUND         | If you have hit an endpoint that doesn't exist.                                                                                                                                                                                                                                                                  |
| ITEM_NOT_FOUND             | The item you queried cannot be found.                                                                                                                                                                                                                                                                            |
| PLAN_RESTRICTED_FEATURE    | This feature is restricted to users of higher plans. The user is recommended to upgrade their plan to use this endpoint.                                                                                                                                                                                         |
| DUPLICATE_ITEM             | This item already exists.                                                                                                                                                                                                                                                                                        |
| BOZO_RSS_FEED              | This RSS feed is invalid or not a well-formed XML.                                                                                                                                                                                                                                                               |
| TOO_MUCH_DATA              | Client sent too much data to the API. Please keep requests under 100MB in size.                                                                                                                                                                                                                                  |
| DOWNLOAD_TOO_LARGE         | This download is oversized for the user's plan. The user is recommended to upgrade their plan to download this file. <br> <br>Free Plan Limit: **10737418240** bytes <br>Essential Plan Limit: **214748364800** bytes <br>Standard Plan Limit: **214748364800** bytes <br>Pro Plan Limit: **536870912000** bytes |
| MISSING_REQUIRED_OPTION    | The API is missing required information to process the request.                                                                                                                                                                                                                                                  |
| TOO_MANY_OPTIONS           | Client sent too many options. Usually this has to do with the API requiring only 1 option but the client sent more than the required.                                                                                                                                                                            |
| BOZO_TORRENT               | The torrent sent is not a valid torrent.                                                                                                                                                                                                                                                                         |
| NO_SERVERS_AVAILABLE_ERROR | There are no download servers available to handle this request. This should never happen. If you receieve this error, please contact us at [contact@torbox.app](https://mailto:contact@torbox.app).                                                                                                              |
| MONTHLY_LIMIT              | User has hit the maximum monthly limit. It is recommended user upgrade their account to be able to download more.                                                                                                                                                                                                |
| COOLDOWN_LIMIT             | User is on download cooldown. It is recommended user upgrade their account to be able to bypass this restriction.                                                                                                                                                                                                |
| ACTIVE_LIMIT               | User has hit their max active download limit. It is recommended user upgrade their account or purchase addons to bypass this restriction.                                                                                                                                                                        |
| DOWNLOAD_SERVER_ERROR      | There was an error interacting with the download on the download server. It is recommdned to simply wait some time before trying again.                                                                                                                                                                          |
| BOZO_NZB                   | The NZB sent is not a valid NZB file.                                                                                                                                                                                                                                                                            |
| SEARCH_ERROR               | There was an error searching using the TorBox Search API.                                                                                                                                                                                                                                                        |
| INVALID_DEVICE             | The client is sending requests from the incorrect device.                                                                                                                                                                                                                                                        |
| DIFF_ISSUE                 | The request parameters sent does not allow for this request to complete.                                                                                                                                                                                                                                         |
| LINK_OFFLINE               | The link given is inaccessible or has no online files.                                                                                                                                                                                                                                                           |
| VENDOR_DISABLED            | This vendor account has been disabled. Please contact support.                                                                                                                                                                                                                                                   |
| BOZO_REGEX                 | The regex you entered is bad.                                                                                                                                                                                                                                                                                    |
| BAD_CONFIRMATION           | The confirmation code you have given is invalid.                                                                                                                                                                                                                                                                 |
| CONFIRMATION_EXPIRED       | The confirmation code you have given is expired. Request a new code.                                                                                                                                                                                                                                             |
| BOZO_FILE                  | This file doesn't match the required mimetype. Please use a different file.                                                                                                                                                                                                                                      |

### Translation to Real-Debrid API<a id="translation-to-real-debrid-api"></a>

Useful for if you want to add TorBox to an app where Real-Debrid is already existing. These are the API routes that are nearly the same with Real-Debrid API routes. You will have to change things such as parameters and check outputs as they both are not the same. You can find docs to Real-Debrid's API [here](https://api.real-debrid.com/).

| Real-Debrid API Routes                     | TorBox API Routes                                                                   |
| ------------------------------------------ | ----------------------------------------------------------------------------------- |
| `GET` /torrents                            | `GET` /torrents/mylist                                                              |
| `GET` /torrents/info/{id}                  | `GET` /torrents/mylist?id={id}                                                      |
| `GET` /torrents/instantAvailability/{hash} | `GET` /torrents/checkcached                                                         |
| `PUT` /torrents/addTorrent                 | `POST` /torrents/createtorrent                                                      |
| `POST` /torrents/addMagnet                 | `POST` /torrents/createtorrent                                                      |
| `POST` /torrents/selectFiles/{id}          | **None**, _not needed. Torrents will download all files. This will not be changed._ |
| `DELETE` /torrents/delete/{id}             | `POST` /torrents/controltorrent                                                     |
| `POST` /unrestrict/link                    | `GET` /torrents/requestdl                                                           |

### Dates<a id="dates"></a>

All dates returned from the API are normalized to UTC time. All dates are in the format:

`%Y-%m-%dT%H:%M:%SZ`

Example: `2024-10-21T20:47:03Z` = The 21st of October, 2024 at 8:47:03 PM UTC.

This makes it easy for users and integrations to parse these dates and change them to the user's time zone for better UX. For more information on these formats, you can take a look at this [cheat sheet](https://strftime.org/).

### SDK<a id="sdk"></a>

There are many official and even non-official community created SDKs that wrap TorBox's API making it simple for developers to easily and quickly create applications using TorBox's API with their native programming language. There are already SDKs for the most popular languages and more are being added all the time!

_Note: Being the official SDK does not mean you should use it over another SDK of the same language. There are some very impressive and highly updated SDKs!_

| **Language**          | **Project Link**                                                                               | **Official** |
| --------------------- | ---------------------------------------------------------------------------------------------- | ------------ |
| Python                | [https://github.com/TorBox-App/torbox-sdk-py](https://github.com/TorBox-App/torbox-sdk-py)     | **YES**      |
| Python                | [https://github.com/eliasbenb/TorBox.py](https://github.com/eliasbenb/TorBox.py)               | **NO**       |
| Javascript/Typescript | [https://github.com/TorBox-App/torbox-sdk-js](https://github.com/TorBox-App/torbox-sdk-js)     | **YES**      |
| Javascript/Typescript | [https://www.npmjs.com/package/node-torbox-api](https://www.npmjs.com/package/node-torbox-api) | **NO**       |
| Go                    | [https://github.com/TorBox-App/torbox-sdk-go](https://github.com/TorBox-App/torbox-sdk-go)     | **YES**      |
| C#                    | [https://github.com/asylumexp/TorBox.NET](https://github.com/asylumexp/TorBox.NET)             | **NO**       |

## Table of Contents<a id="table-of-contents"></a>

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [Access Token Authentication](#access-token-authentication)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)

# Setup & Configuration<a id="setup--configuration"></a>

## Supported Language Versions<a id="supported-language-versions"></a>

This SDK is compatible with the following versions: `Python >= 3.9`

## Installation<a id="installation"></a>

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install main_api_sdk
```

If you are using Python 3, you can use `pip3` instead:

```bash
pip3 install main_api_sdk
```

## Disabling Redirects<a id="disabling-redirects"></a>

By default, the SDK follows HTTP redirects (3xx responses) automatically. Pass
`follow_redirects=False` to get the redirect response back as-is instead:

```python
client = MainApiSdk(follow_redirects=False)
```

This can also be changed later with `client.set_follow_redirects(False)`.

## Logging<a id="logging"></a>

The SDK is silent by default. Pass a standard library `logging.Logger` as `logger` to log
every outgoing request and its response (method, URL, status, and duration):

```python
import logging

logger = logging.getLogger("MainApiSdk")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

client = MainApiSdk(logger=logger)
```

This can also be changed later with `client.set_logging(logger)`.

`Authorization` and `Cookie` header values are always redacted in logged output, regardless
of the logger's own configuration.

## Authentication<a id="authentication"></a>

### Access Token Authentication<a id="access-token-authentication"></a>

The MainApiSdk API uses an Access Token for authentication.

This token must be provided to authenticate your requests to the API.

#### Setting the Access Token<a id="setting-the-access-token"></a>

When you initialize the SDK, you can set the access token as follows:

```py
MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10
)
```

If you need to set or update the access token after initializing the SDK, you can use:

```py
sdk.set_access_token("YOUR_ACCESS_TOKEN")
```

## Setting a Custom Timeout<a id="setting-a-custom-timeout"></a>

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from main_api_sdk import MainApiSdk

sdk = MainApiSdk(timeout=10)
```

# Sample Usage<a id="sample-usage"></a>

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_up_status()

print(result)

```

# Async Usage<a id="async-usage"></a>

The SDK includes an Async Client for making asynchronous API requests. This is useful for applications that need non-blocking operations, like web servers or apps with a graphical user interface.

```py
import asyncio
from main_api_sdk import MainApiSdkAsync, Environment

sdk = MainApiSdkAsync(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)


async def main():
  result = await sdk.main_api_sdk.get_up_status()
  print(result)

asyncio.run(main())
```

## Services<a id="services"></a>

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services:</summary>

| Name         |
| :----------- |
| main_api_sdk |

</details>

## Models<a id="models"></a>

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models:</summary>

| Name                                         | Description |
| :------------------------------------------- | :---------- |
| CreateTorrentRequest                         |             |
| AsyncCreateTorrentRequest                    |             |
| MainApiSdkRequestDownloadLinksPostRequest1   |             |
| GetTorrentCachedAvailabilityBatchRequest     |             |
| GetTorrentInfoRequest                        |             |
| EditTorrentItemRequest                       |             |
| MagnetToFileRequest                          |             |
| CreateUsenetDownloadRequest                  |             |
| MainApiSdkRequestDownloadLinksPostRequest2   |             |
| GetUsenetCachedAvailabilityBatchRequest      |             |
| EditUsenetItemRequest                        |             |
| CreateWebDownloadRequest                     |             |
| MainApiSdkRequestDownloadLinksPostRequest3   |             |
| GetWebDownloadCachedAvailabilityBatchRequest |             |
| EditWebDownloadItemRequest                   |             |
| GetTokenFromDeviceCodeProcessRequest         |             |

</details>
