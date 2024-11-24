# TorboxApi Python SDK 1.0.0

Welcome to the TorboxApi SDK documentation. This guide will help you get started with integrating and using the TorboxApi SDK in your project.

## Versions

- API version: `1.0.0`
- SDK version: `1.0.0`

## Table of Contents

- [TorboxApi Python SDK 1.0.0](#torboxapi-python-sdk-100)
  - [Versions](#versions)
  - [Table of Contents](#table-of-contents)
  - [Setup \& Configuration](#setup--configuration)
    - [Supported Language Versions](#supported-language-versions)
    - [Installation](#installation)
  - [Authentication](#authentication)
    - [Access Token Authentication](#access-token-authentication)
      - [Setting the Access Token](#setting-the-access-token)
  - [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
  - [Services](#services)
  - [Models](#models)
    - [Using Union Types](#using-union-types)
      - [Example Function with Union Types](#example-function-with-union-types)
  - [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install torbox_api
```

## Authentication

### Access Token Authentication

The TorboxApi API uses an Access Token for authentication.

This token must be provided to authenticate your requests to the API.

#### Setting the Access Token

When you initialize the SDK, you can set the access token as follows:

```py
TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)
```

If you need to set or update the access token after initializing the SDK, you can use:

```py
sdk.set_access_token("YOUR_ACCESS_TOKEN")
```

## Setting a Custom Timeout

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from torbox_api import TorboxApi

sdk = TorboxApi(timeout=10000)
```

# Sample Usage

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.general.get_up_status()

print(result)

```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                                             |
| :------------------------------------------------------------------------------- |
| [TorrentsService](documentation/services/TorrentsService.md)                     |
| [UsenetService](documentation/services/UsenetService.md)                         |
| [WebDownloadsDebridService](documentation/services/WebDownloadsDebridService.md) |
| [GeneralService](documentation/services/GeneralService.md)                       |
| [NotificationsService](documentation/services/NotificationsService.md)           |
| [UserService](documentation/services/UserService.md)                             |
| [RssFeedsService](documentation/services/RssFeedsService.md)                     |
| [IntegrationsService](documentation/services/IntegrationsService.md)             |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                                                                                     | Description |
| :------------------------------------------------------------------------------------------------------- | :---------- |
| [CreateTorrentRequest](documentation/models/CreateTorrentRequest.md)                                     |             |
| [CreateTorrentOkResponse](documentation/models/CreateTorrentOkResponse.md)                               |             |
| [ControlTorrentOkResponse](documentation/models/ControlTorrentOkResponse.md)                             |             |
| [ControlQueuedTorrentOkResponse](documentation/models/ControlQueuedTorrentOkResponse.md)                 |             |
| [RequestDownloadLinkOkResponse](documentation/models/RequestDownloadLinkOkResponse.md)                   |             |
| [GetTorrentListOkResponse](documentation/models/GetTorrentListOkResponse.md)                             |             |
| [GetTorrentCachedAvailabilityOkResponse](documentation/models/GetTorrentCachedAvailabilityOkResponse.md) |             |
| [SearchAllTorrentsFromScraperOkResponse](documentation/models/SearchAllTorrentsFromScraperOkResponse.md) |             |
| [ExportTorrentDataOkResponse](documentation/models/ExportTorrentDataOkResponse.md)                       |             |
| [GetTorrentInfoOkResponse](documentation/models/GetTorrentInfoOkResponse.md)                             |             |
| [CreateUsenetDownloadRequest](documentation/models/CreateUsenetDownloadRequest.md)                       |             |
| [CreateUsenetDownloadOkResponse](documentation/models/CreateUsenetDownloadOkResponse.md)                 |             |
| [GetUsenetListOkResponse](documentation/models/GetUsenetListOkResponse.md)                               |             |
| [CreateWebDownloadRequest](documentation/models/CreateWebDownloadRequest.md)                             |             |
| [CreateWebDownloadOkResponse](documentation/models/CreateWebDownloadOkResponse.md)                       |             |
| [GetWebDownloadListOkResponse](documentation/models/GetWebDownloadListOkResponse.md)                     |             |
| [GetUpStatusOkResponse](documentation/models/GetUpStatusOkResponse.md)                                   |             |
| [GetStatsOkResponse](documentation/models/GetStatsOkResponse.md)                                         |             |
| [GetNotificationFeedOkResponse](documentation/models/GetNotificationFeedOkResponse.md)                   |             |
| [GetUserDataOkResponse](documentation/models/GetUserDataOkResponse.md)                                   |             |
| [AddReferralToAccountOkResponse](documentation/models/AddReferralToAccountOkResponse.md)                 |             |
| [GetAllJobsOkResponse](documentation/models/GetAllJobsOkResponse.md)                                     |             |
| [GetAllJobsByHashOkResponse](documentation/models/GetAllJobsByHashOkResponse.md)                         |             |

</details>

### Using Union Types

Union types allow you to specify that a variable can have more than one type. This is particularly useful when a function can accept multiple types of inputs. The Union type hint is used for this purpose.

#### Example Function with Union Types

You can call service method with an instance of `TypeA`, `TypeB`, or a dictionary that can be converted to an instance of either type.

```python
# Model Definition
ParamType = Union[TypeA, TypeB]

# Service Method
def service_method(param: ParamType):
...

## Usage
type_a = TypeA(key="value")
type_b = TypeB(key="value")

sdk.service.service_method(type_a)
sdk.service.service_method(type_b)
sdk.service.service_method({"key": "value"})
```

You cannot create an instance of a `Union` type itself. Instead, pass an instance of one of the types in the `Union`, or a dictionary that can be converted to one of those types.

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.
