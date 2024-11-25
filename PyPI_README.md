# TorboxApi Python SDK 1.0.0<a id="torboxapi-python-sdk-100"></a>

Welcome to the TorboxApi SDK documentation. This guide will help you get started with integrating and using the TorboxApi SDK in your project.

## Versions<a id="versions"></a>

- API version: `1.0.0`
- SDK version: `1.0.0`

## About the API<a id="about-the-api"></a>

You can view the full documentation at https://api-docs.torbox.app.

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
  - [Using Union Types](#using-union-types)
- [License](#license)

## Setup & Configuration<a id="setup--configuration"></a>

### Supported Language Versions<a id="supported-language-versions"></a>

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation<a id="installation"></a>

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install torbox-api
```

## Authentication<a id="authentication"></a>

### Access Token Authentication<a id="access-token-authentication"></a>

The TorboxApi API uses an Access Token for authentication.

This token must be provided to authenticate your requests to the API.

#### Setting the Access Token<a id="setting-the-access-token"></a>

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

## Setting a Custom Timeout<a id="setting-a-custom-timeout"></a>

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from torbox_api import TorboxApi

sdk = TorboxApi(timeout=10000)
```

# Sample Usage<a id="sample-usage"></a>

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

## Services<a id="services"></a>

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services:</summary>

| Name                 |
| :------------------- |
| torrents             |
| usenet               |
| web_downloads_debrid |
| general              |
| notifications        |
| user                 |
| rss_feeds            |
| integrations         |

</details>

## Models<a id="models"></a>

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models:</summary>

| Name                                   | Description |
| :------------------------------------- | :---------- |
| CreateTorrentRequest                   |             |
| CreateTorrentOkResponse                |             |
| ControlTorrentOkResponse               |             |
| ControlQueuedTorrentOkResponse         |             |
| RequestDownloadLinkOkResponse          |             |
| GetTorrentListOkResponse               |             |
| GetTorrentCachedAvailabilityOkResponse |             |
| SearchAllTorrentsFromScraperOkResponse |             |
| ExportTorrentDataOkResponse            |             |
| GetTorrentInfoOkResponse               |             |
| CreateUsenetDownloadRequest            |             |
| CreateUsenetDownloadOkResponse         |             |
| GetUsenetListOkResponse                |             |
| CreateWebDownloadRequest               |             |
| CreateWebDownloadOkResponse            |             |
| GetWebDownloadListOkResponse           |             |
| GetUpStatusOkResponse                  |             |
| GetStatsOkResponse                     |             |
| GetNotificationFeedOkResponse          |             |
| GetUserDataOkResponse                  |             |
| AddReferralToAccountOkResponse         |             |
| GetAllJobsOkResponse                   |             |
| GetAllJobsByHashOkResponse             |             |

</details>

### Using Union Types<a id="using-union-types"></a>

Union types allow you to specify that a variable can have more than one type. This is particularly useful when a function can accept multiple types of inputs. The Union type hint is used for this purpose.

#### Example Function with Union Types<a id="example-function-with-union-types"></a>

You can call service method with an instance of `TypeA`, `TypeB`, or a dictionary that can be converted to an instance of either type.

```python
# Model Definition<a id="model-definition"></a>
ParamType = Union[TypeA, TypeB]

# Service Method<a id="service-method"></a>
def service_method(param: ParamType):
...

## Usage<a id="usage"></a>
type_a = TypeA(key="value")
type_b = TypeB(key="value")

sdk.service.service_method(type_a)
sdk.service.service_method(type_b)
sdk.service.service_method({"key": "value"})
```

You cannot create an instance of a `Union` type itself. Instead, pass an instance of one of the types in the `Union`, or a dictionary that can be converted to one of those types.

## License<a id="license"></a>

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.
