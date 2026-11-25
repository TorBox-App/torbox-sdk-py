# torbox.TorrentsApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_create_torrent**](TorrentsApi.md#async_create_torrent) | **POST** /v1/api/torrents/asynccreatetorrent | Async Create Torrent
[**control_queued_torrents**](TorrentsApi.md#control_queued_torrents) | **POST** /v1/api/torrents/controlqueued | Control Queued Torrents
[**control_torrent**](TorrentsApi.md#control_torrent) | **POST** /v1/api/torrents/controltorrent | Control Torrent
[**create_torrent**](TorrentsApi.md#create_torrent) | **POST** /v1/api/torrents/createtorrent | Create Torrent
[**edit_torrent_item**](TorrentsApi.md#edit_torrent_item) | **PUT** /v1/api/torrents/edittorrent | Edit Torrent Item
[**export_torrent_data**](TorrentsApi.md#export_torrent_data) | **GET** /v1/api/torrents/exportdata | Export Torrent Data
[**get_queued_torrents**](TorrentsApi.md#get_queued_torrents) | **GET** /v1/api/torrents/getqueued | Get Queued Torrents
[**get_torrent_cached_availability**](TorrentsApi.md#get_torrent_cached_availability) | **GET** /v1/api/torrents/checkcached | Get Torrent Cached Availability
[**get_torrent_cached_availability_batch**](TorrentsApi.md#get_torrent_cached_availability_batch) | **POST** /v1/api/torrents/checkcached | Get Torrent Cached Availability Batch
[**get_torrent_info**](TorrentsApi.md#get_torrent_info) | **GET** /v1/api/torrents/torrentinfo | Get Torrent Info
[**get_torrent_info_from_file**](TorrentsApi.md#get_torrent_info_from_file) | **POST** /v1/api/torrents/torrentinfo | Get Torrent Info
[**get_torrent_list**](TorrentsApi.md#get_torrent_list) | **GET** /v1/api/torrents/mylist | Get Torrent List
[**magnet_to_file**](TorrentsApi.md#magnet_to_file) | **POST** /v1/api/torrents/magnettofile | Magnet To File
[**request_torrent_download_link**](TorrentsApi.md#request_torrent_download_link) | **GET** /v1/api/torrents/requestdl | Request Download Link
[**request_torrent_download_links_get**](TorrentsApi.md#request_torrent_download_links_get) | **GET** /v1/api/torrents/requestdl/batch | Request Download Links - GET
[**request_torrent_download_links_post**](TorrentsApi.md#request_torrent_download_links_post) | **POST** /v1/api/torrents/requestdl/batch | Request Download Links - POST


# **async_create_torrent**
> AsyncCreateTorrentResponse async_create_torrent(file=file, magnet=magnet, seed=seed, allow_zip=allow_zip, name=name, as_queued=as_queued, add_only_if_cached=add_only_if_cached)

Async Create Torrent

### Overview

Creates a torrent asynchrously under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large.

The request will return instantly, not returning any data other than a success message. This is the same for failures, as they will return the error in the background, rather than immediately.

### Rate Limits

This endpoint has the same limits as the Create Torrent endpoint: **300 requests per minute**, and **60 uncached torrents per hour**. The hourly limit is shared between the two endpoints, so an uncached torrent added through either one counts against the same 60. As on that endpoint, a request sent with `add_only_if_cached` and without `as_queued` is not counted against the hourly limit.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.async_create_torrent_response import AsyncCreateTorrentResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    file = None # bytes | The torrent's torrent file. Optional. (optional)
    magnet = 'magnet_example' # str | The torrent's magnet link. Optional. (optional)
    seed = 56 # int | Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings. (optional)
    allow_zip = True # bool | Tells TorBox if you want to allow this torrent to be zipped or not. TorBox only zips if the torrent is 100 files or larger. (optional) (default to True)
    name = 'name_example' # str | The name you want the torrent to be. Optional. (optional)
    as_queued = False # bool | Tells TorBox you want this torrent instantly queued. This is bypassed if user is on free plan, and will process the request as normal in this case. Optional. (optional) (default to False)
    add_only_if_cached = False # bool | Only adds the download if it is cached on TorBox. If not cached, it won't be added. (optional) (default to False)

    try:
        # Async Create Torrent
        api_response = api_instance.async_create_torrent(file=file, magnet=magnet, seed=seed, allow_zip=allow_zip, name=name, as_queued=as_queued, add_only_if_cached=add_only_if_cached)
        print("The response of TorrentsApi->async_create_torrent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->async_create_torrent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**| The torrent&#39;s torrent file. Optional. | [optional] 
 **magnet** | **str**| The torrent&#39;s magnet link. Optional. | [optional] 
 **seed** | **int**| Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don&#39;t seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings. | [optional] 
 **allow_zip** | **bool**| Tells TorBox if you want to allow this torrent to be zipped or not. TorBox only zips if the torrent is 100 files or larger. | [optional] [default to True]
 **name** | **str**| The name you want the torrent to be. Optional. | [optional] 
 **as_queued** | **bool**| Tells TorBox you want this torrent instantly queued. This is bypassed if user is on free plan, and will process the request as normal in this case. Optional. | [optional] [default to False]
 **add_only_if_cached** | **bool**| Only adds the download if it is cached on TorBox. If not cached, it won&#39;t be added. | [optional] [default to False]

### Return type

[**AsyncCreateTorrentResponse**](AsyncCreateTorrentResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_queued_torrents**
> control_queued_torrents()

Control Queued Torrents

### Overview

This endpoint is deprecated and always answers with a `DEPRECATED` error. Use the Control Queued Downloads endpoint (`/v1/api/queued/controlqueued`) instead.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)

    try:
        # Control Queued Torrents
        api_instance.control_queued_torrents()
    except Exception as e:
        print("Exception when calling TorrentsApi->control_queued_torrents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**410** | Gone |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_torrent**
> ControlTorrentResponse control_torrent(control_torrent)

Control Torrent

### Overview

Controls a torrent. By sending the torrent's ID and the type of operation you want to perform, it will send that request to the torrent client.

Operations are either:

- **Reannounce** `reannounces the torrent to get new peers`

- **Delete** `deletes the torrent from the client and your account permanently`

- **Resume** `resumes a paused torrent`


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.control_torrent import ControlTorrent
from torbox.models.control_torrent_response import ControlTorrentResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    control_torrent = {"torrent_id":1,"operation":"delete","all":false} # ControlTorrent | 

    try:
        # Control Torrent
        api_response = api_instance.control_torrent(control_torrent)
        print("The response of TorrentsApi->control_torrent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->control_torrent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_torrent** | [**ControlTorrent**](ControlTorrent.md)|  | 

### Return type

[**ControlTorrentResponse**](ControlTorrentResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_torrent**
> CreateTorrentResponse create_torrent(file=file, magnet=magnet, seed=seed, allow_zip=allow_zip, name=name, as_queued=as_queued, add_only_if_cached=add_only_if_cached)

Create Torrent

### Overview

Creates a torrent under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large.

### Rate Limits

This endpoint has two limits that apply at the same time:

- **300 requests per minute:** a shared ceiling that _every_ request counts against, whether the torrent is cached or uncached.

- **60 uncached torrents per hour:** an additional, stricter limit that only uncached torrents count against. A request sent with `add_only_if_cached` is not counted, because it adds nothing when the torrent is not cached. It is counted when it is also sent with `as_queued`, because a queued torrent is added whether it is cached or not.


The important thing is that cached and uncached requests both draw from the same 300/min pool, but uncached requests _also_ draw from their own separate 60/hour pool. An uncached request therefore counts twice: once against the per-minute limit, and once against the per-hour uncached limit.

**Example:** In a single minute you add 250 cached + 50 uncached torrents. That's 300 total, so you've hit the per-minute limit for that minute. But those 50 uncached torrents also came out of your 60/hour uncached budget, leaving only **10 uncached torrents** for the remaining 59 minutes of that hour. (You could still add plenty more _cached_ torrents during that hour, since cached requests aren't capped hourly: only by the 300/min ceiling.)

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.create_torrent_response import CreateTorrentResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    file = None # bytes | The torrent's torrent file. Optional. (optional)
    magnet = 'magnet_example' # str | The torrent's magnet link. Optional. (optional)
    seed = 56 # int | Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings. (optional)
    allow_zip = True # bool | Tells TorBox if you want to allow this torrent to be zipped or not. TorBox only zips if the torrent is 100 files or larger. (optional) (default to True)
    name = 'name_example' # str | The name you want the torrent to be. Optional. (optional)
    as_queued = False # bool | Tells TorBox you want this torrent instantly queued. This is bypassed if user is on free plan, and will process the request as normal in this case. Optional. (optional) (default to False)
    add_only_if_cached = False # bool | Only adds the download if it is cached on TorBox. If not cached, it won't be added. (optional) (default to False)

    try:
        # Create Torrent
        api_response = api_instance.create_torrent(file=file, magnet=magnet, seed=seed, allow_zip=allow_zip, name=name, as_queued=as_queued, add_only_if_cached=add_only_if_cached)
        print("The response of TorrentsApi->create_torrent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->create_torrent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**| The torrent&#39;s torrent file. Optional. | [optional] 
 **magnet** | **str**| The torrent&#39;s magnet link. Optional. | [optional] 
 **seed** | **int**| Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don&#39;t seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings. | [optional] 
 **allow_zip** | **bool**| Tells TorBox if you want to allow this torrent to be zipped or not. TorBox only zips if the torrent is 100 files or larger. | [optional] [default to True]
 **name** | **str**| The name you want the torrent to be. Optional. | [optional] 
 **as_queued** | **bool**| Tells TorBox you want this torrent instantly queued. This is bypassed if user is on free plan, and will process the request as normal in this case. Optional. | [optional] [default to False]
 **add_only_if_cached** | **bool**| Only adds the download if it is cached on TorBox. If not cached, it won&#39;t be added. | [optional] [default to False]

### Return type

[**CreateTorrentResponse**](CreateTorrentResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_torrent_item**
> EditTorrentItemResponse edit_torrent_item(edit_torrent)

Edit Torrent Item

### Overview

Updates a download item based on the item's ID.
Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important.

### Restrictions

- Does not affect the cached database (or any other user's item).

- Name must pass validation:

    - Above 1 character long.

    - Below 200 characters long.

    - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically).

    - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically).

- Tags follow the same rules as the name.

- Alternative hashes must be of MD5, SHA1, or SHA256.


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.edit_torrent import EditTorrent
from torbox.models.edit_torrent_item_response import EditTorrentItemResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    edit_torrent = {"torrent_id":0,"name":"string","tags":["string"],"alternative_hashes":["0123456789abcdef0123456789abcdef01234567"],"airlocked":false} # EditTorrent | 

    try:
        # Edit Torrent Item
        api_response = api_instance.edit_torrent_item(edit_torrent)
        print("The response of TorrentsApi->edit_torrent_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->edit_torrent_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_torrent** | [**EditTorrent**](EditTorrent.md)|  | 

### Return type

[**EditTorrentItemResponse**](EditTorrentItemResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_torrent_data**
> ExportTorrentDataResponse export_torrent_data(torrent_id, type)

Export Torrent Data

### Overview

Exports the magnet or torrent file. Requires a type to be passed. If type is **magnet**, it will return a JSON response with the magnet as a string in the _data_ key. If type is **file**, it will return a bittorrent file as a download. Not compatible with cached downloads.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.export_torrent_data_response import ExportTorrentDataResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    torrent_id = 56 # int | The torrent's ID.
    type = 'type_example' # str | Either \"magnet\" or \"file\". Tells how the API what to get, and what to respond as. If magnet, it returns a JSON response with the magnet as a string in the data key. If file, it responds with a torrent file download.

    try:
        # Export Torrent Data
        api_response = api_instance.export_torrent_data(torrent_id, type)
        print("The response of TorrentsApi->export_torrent_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->export_torrent_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **torrent_id** | **int**| The torrent&#39;s ID. | 
 **type** | **str**| Either \&quot;magnet\&quot; or \&quot;file\&quot;. Tells how the API what to get, and what to respond as. If magnet, it returns a JSON response with the magnet as a string in the data key. If file, it responds with a torrent file download. | 

### Return type

[**ExportTorrentDataResponse**](ExportTorrentDataResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-bittorrent

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queued_torrents**
> get_queued_torrents()

Get Queued Torrents

### Overview

This endpoint is deprecated and always answers with a `DEPRECATED` error. Use the Get Queued Downloads endpoint (`/v1/api/queued/getqueued`) instead.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)

    try:
        # Get Queued Torrents
        api_instance.get_queued_torrents()
    except Exception as e:
        print("Exception when calling TorrentsApi->get_queued_torrents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**410** | Gone |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_torrent_cached_availability**
> GetTorrentCachedAvailabilityResponse get_torrent_cached_availability(hash=hash, format=format, list_files=list_files, check_cached=check_cached)

Get Torrent Cached Availability

### Overview

Takes in a list of comma separated torrent hashes and checks if the torrent is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as:
`?hash=XXXX&hash=XXXX&hash=XXXX`

or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX`
and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour.

You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.check_cached import CheckCached
from torbox.models.get_torrent_cached_availability_response import GetTorrentCachedAvailabilityResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    hash = ['hash_example'] # List[str] | The list of torrent hashes you want to check. Comma seperated. (optional)
    format = 'object' # str | Format you want the data in. Acceptable is either \"object\" or \"list\". List is the most performant option as it doesn't require modification of the list. (optional) (default to 'object')
    list_files = False # bool | Allows you to list the files found inside the cached data. (optional) (default to False)
    check_cached = torbox.CheckCached() # CheckCached |  (optional)

    try:
        # Get Torrent Cached Availability
        api_response = api_instance.get_torrent_cached_availability(hash=hash, format=format, list_files=list_files, check_cached=check_cached)
        print("The response of TorrentsApi->get_torrent_cached_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->get_torrent_cached_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | [**List[str]**](str.md)| The list of torrent hashes you want to check. Comma seperated. | [optional] 
 **format** | **str**| Format you want the data in. Acceptable is either \&quot;object\&quot; or \&quot;list\&quot;. List is the most performant option as it doesn&#39;t require modification of the list. | [optional] [default to &#39;object&#39;]
 **list_files** | **bool**| Allows you to list the files found inside the cached data. | [optional] [default to False]
 **check_cached** | [**CheckCached**](CheckCached.md)|  | [optional] 

### Return type

[**GetTorrentCachedAvailabilityResponse**](GetTorrentCachedAvailabilityResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_torrent_cached_availability_batch**
> GetTorrentCachedAvailabilityBatchResponse get_torrent_cached_availability_batch(hash=hash, format=format, list_files=list_files, check_cached=check_cached)

Get Torrent Cached Availability Batch

### Overview

Takes in a list of comma separated torrent hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters.


Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour.

You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.check_cached import CheckCached
from torbox.models.get_torrent_cached_availability_batch_response import GetTorrentCachedAvailabilityBatchResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    hash = ['hash_example'] # List[str] |  (optional)
    format = 'object' # str |  (optional) (default to 'object')
    list_files = False # bool |  (optional) (default to False)
    check_cached = {"hashes":["string","string"]} # CheckCached |  (optional)

    try:
        # Get Torrent Cached Availability Batch
        api_response = api_instance.get_torrent_cached_availability_batch(hash=hash, format=format, list_files=list_files, check_cached=check_cached)
        print("The response of TorrentsApi->get_torrent_cached_availability_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->get_torrent_cached_availability_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**|  | [optional] [default to &#39;object&#39;]
 **list_files** | **bool**|  | [optional] [default to False]
 **check_cached** | [**CheckCached**](CheckCached.md)|  | [optional] 

### Return type

[**GetTorrentCachedAvailabilityBatchResponse**](GetTorrentCachedAvailabilityBatchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_torrent_info**
> GetTorrentInfoResponse get_torrent_info(hash, timeout=timeout, use_cache_lookup=use_cache_lookup)

Get Torrent Info

### Overview

A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant.

**It is not recommended to use this for checking TorBox's cache. Please use the GET /checkcache endpoint instead.**

### Authorization

None required.


### Example


```python
import torbox
from torbox.models.get_torrent_info_response import GetTorrentInfoResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)


# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    hash = 'hash_example' # str | Hash of the torrent you want to get info for. This is required.
    timeout = 30 # int | The amount of time you want TorBox to search for the torrent on the Bittorrent network. If the number of seeders is low or even zero, this value may be helpful to move up. Default is 10. Optional. (optional) (default to 30)
    use_cache_lookup = False # bool | If you want to use a pre-cached request if sent before. This can save a lot of time. Default false. (optional) (default to False)

    try:
        # Get Torrent Info
        api_response = api_instance.get_torrent_info(hash, timeout=timeout, use_cache_lookup=use_cache_lookup)
        print("The response of TorrentsApi->get_torrent_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->get_torrent_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Hash of the torrent you want to get info for. This is required. | 
 **timeout** | **int**| The amount of time you want TorBox to search for the torrent on the Bittorrent network. If the number of seeders is low or even zero, this value may be helpful to move up. Default is 10. Optional. | [optional] [default to 30]
 **use_cache_lookup** | **bool**| If you want to use a pre-cached request if sent before. This can save a lot of time. Default false. | [optional] [default to False]

### Return type

[**GetTorrentInfoResponse**](GetTorrentInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_torrent_info_from_file**
> GetTorrentInfoFromFileResponse get_torrent_info_from_file(timeout=timeout, hash=hash, magnet=magnet, file=file, use_cache_lookup=use_cache_lookup, peers_only=peers_only)

Get Torrent Info

### Overview

Same as the GET route, but allows posting data such as magnet, and torrent files.

Hashes will have precedence over magnets, and magnets will have precedence over torrent files.

Only proper torrent files are accepted.

At least one of hash, magnet, or torrent file is required.

A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant.

**It is not recommended to use this for checking TorBox's cache. Please use the GET /checkcache endpoint instead.**

### Authorization

None required.


### Example


```python
import torbox
from torbox.models.get_torrent_info_from_file_response import GetTorrentInfoFromFileResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)


# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    timeout = 10 # int | The amount of time you want TorBox to search for the torrent on the Bittorrent network. If the number of seeders is low or even zero, this value may be helpful to move up. Default is 10. Optional. (optional) (default to 10)
    hash = 'hash_example' # str | A torrent hash for requesting information about the torrent. Optional. (optional)
    magnet = 'magnet_example' # str | A magnet link for requesting information abouit the torrent. Optional. (optional)
    file = None # bytes | A torrent file for requesting information about the torrent. Optional. (optional)
    use_cache_lookup = False # bool | If you want to use a pre-cached request if sent before. This can save a lot of time. Default false. (optional) (default to False)
    peers_only = False # bool | Uses a quick lookup method using the trackers contained within the magnet or file. Requires the submitted magnet or torrent file to contain trackers of UDP or HTTP(S) to work. This will not get metadata such as name, size, or files. Best used for simply and quickly gathering the current seeds and peers according to the trackers. Uses the highest number of all the trackers as the final value. Default off. (optional) (default to False)

    try:
        # Get Torrent Info
        api_response = api_instance.get_torrent_info_from_file(timeout=timeout, hash=hash, magnet=magnet, file=file, use_cache_lookup=use_cache_lookup, peers_only=peers_only)
        print("The response of TorrentsApi->get_torrent_info_from_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->get_torrent_info_from_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| The amount of time you want TorBox to search for the torrent on the Bittorrent network. If the number of seeders is low or even zero, this value may be helpful to move up. Default is 10. Optional. | [optional] [default to 10]
 **hash** | **str**| A torrent hash for requesting information about the torrent. Optional. | [optional] 
 **magnet** | **str**| A magnet link for requesting information abouit the torrent. Optional. | [optional] 
 **file** | **bytes**| A torrent file for requesting information about the torrent. Optional. | [optional] 
 **use_cache_lookup** | **bool**| If you want to use a pre-cached request if sent before. This can save a lot of time. Default false. | [optional] [default to False]
 **peers_only** | **bool**| Uses a quick lookup method using the trackers contained within the magnet or file. Requires the submitted magnet or torrent file to contain trackers of UDP or HTTP(S) to work. This will not get metadata such as name, size, or files. Best used for simply and quickly gathering the current seeds and peers according to the trackers. Uses the highest number of all the trackers as the final value. Default off. | [optional] [default to False]

### Return type

[**GetTorrentInfoFromFileResponse**](GetTorrentInfoFromFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_torrent_list**
> GetTorrentListResponse get_torrent_list(id=id, bypass_cache=bypass_cache, offset=offset, limit=limit, files=files, active=active)

Get Torrent List

### Overview

Gets the user's torrent list. This gives you the needed information to perform other torrent actions. This information only gets updated every 600 seconds, or when the _Request Update On Torrent_ request is sent to the _relay API_.

#### Download States:

- "downloading" -> The torrent is currently downloading.

- "uploading" -> The torrent is currently seeding.

- "stalled (no seeds)" -> The torrent is trying to download, but there are no seeds connected to download from.

- "paused" -> The torrent is paused.

- "completed" -> The torrent is completely downloaded. Do not use this for download completion status.

- "cached" -> The torrent is cached from the server.

- "metaDL" -> The torrent is downloading metadata from the hoard.

- "checkingResumeData" -> The torrent is checking resumable data.


All other statuses are basic qBittorrent states. [Check out here for the full list](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management).

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_torrent_list_response import GetTorrentListResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = torbox.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    id = 56 # int | Determines the torrent requested, will return an object rather than list. Optional. (optional)
    bypass_cache = False # bool | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. (optional) (default to False)
    offset = 0 # int | Determines the offset of items to get from the database. Default is 0. Optional. (optional) (default to 0)
    limit = 1000 # int | Determines the number of items to recieve per request. Default is 1000. Optional. (optional) (default to 1000)
    files = True # bool | Exclude files from response. Optional (optional) (default to True)
    active = True # bool | Shows only active downloads. Optional (optional)

    try:
        # Get Torrent List
        api_response = api_instance.get_torrent_list(id=id, bypass_cache=bypass_cache, offset=offset, limit=limit, files=files, active=active)
        print("The response of TorrentsApi->get_torrent_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->get_torrent_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Determines the torrent requested, will return an object rather than list. Optional. | [optional] 
 **bypass_cache** | **bool**| Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. | [optional] [default to False]
 **offset** | **int**| Determines the offset of items to get from the database. Default is 0. Optional. | [optional] [default to 0]
 **limit** | **int**| Determines the number of items to recieve per request. Default is 1000. Optional. | [optional] [default to 1000]
 **files** | **bool**| Exclude files from response. Optional | [optional] [default to True]
 **active** | **bool**| Shows only active downloads. Optional | [optional] 

### Return type

[**GetTorrentListResponse**](GetTorrentListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **magnet_to_file**
> str magnet_to_file(magnet_to_torrent)

Magnet To File

### Overview

Converts any magnet to a torrent file. Does not require the magnet to be on your TorBox account or in the TorBox cache. Free endpoint for public use.

### Authorization

None required.


### Example


```python
import torbox
from torbox.models.magnet_to_torrent import MagnetToTorrent
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)


# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    magnet_to_torrent = {"magnet":"string"} # MagnetToTorrent | 

    try:
        # Magnet To File
        api_response = api_instance.magnet_to_file(magnet_to_torrent)
        print("The response of TorrentsApi->magnet_to_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->magnet_to_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **magnet_to_torrent** | [**MagnetToTorrent**](MagnetToTorrent.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-bittorrent, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_torrent_download_link**
> RequestTorrentDownloadLinkResponse request_torrent_download_link(token, torrent_id, file_id=file_id, zip_link=zip_link, user_ip=user_ip, redirect=redirect, append_name=append_name)

Request Download Link

### Overview

Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

### Permalinks

Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard.

### Authorization

Requires an API key as a parameter for the `token` parameter.


### Example


```python
import torbox
from torbox.models.request_torrent_download_link_response import RequestTorrentDownloadLinkResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)


# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    token = 'token_example' # str | Your API Key
    torrent_id = 56 # int | The torrent's ID that you want to download
    file_id = 0 # int | The files's ID that you want to download (optional) (default to 0)
    zip_link = False # bool | If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given. (optional) (default to False)
    user_ip = 'user_ip_example' # str | The user's IP to determine the closest CDN. Optional. (optional)
    redirect = False # bool | If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. (optional) (default to False)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)

    try:
        # Request Download Link
        api_response = api_instance.request_torrent_download_link(token, torrent_id, file_id=file_id, zip_link=zip_link, user_ip=user_ip, redirect=redirect, append_name=append_name)
        print("The response of TorrentsApi->request_torrent_download_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->request_torrent_download_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **torrent_id** | **int**| The torrent&#39;s ID that you want to download | 
 **file_id** | **int**| The files&#39;s ID that you want to download | [optional] [default to 0]
 **zip_link** | **bool**| If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given. | [optional] [default to False]
 **user_ip** | **str**| The user&#39;s IP to determine the closest CDN. Optional. | [optional] 
 **redirect** | **bool**| If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. | [optional] [default to False]
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]

### Return type

[**RequestTorrentDownloadLinkResponse**](RequestTorrentDownloadLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**307** | Temporary Redirect |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_torrent_download_links_get**
> RequestTorrentDownloadLinksGetResponse request_torrent_download_links_get(token, torrent_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)

Request Download Links - GET

### Overview

Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

### Authorization

Requires an API key as a parameter for the `token` parameter.


### Example


```python
import torbox
from torbox.models.request_download_batch import RequestDownloadBatch
from torbox.models.request_torrent_download_links_get_response import RequestTorrentDownloadLinksGetResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)


# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    token = 'token_example' # str | Your API Key
    torrent_id = 56 # int | The torrent's ID that you want to download
    file_ids = [56] # List[int] | The files's ID that you want to download (optional)
    user_ip = 'user_ip_example' # str | The user's IP to determine the closest CDN. Optional. (optional)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)
    request_download_batch = torbox.RequestDownloadBatch() # RequestDownloadBatch |  (optional)

    try:
        # Request Download Links - GET
        api_response = api_instance.request_torrent_download_links_get(token, torrent_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)
        print("The response of TorrentsApi->request_torrent_download_links_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->request_torrent_download_links_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **torrent_id** | **int**| The torrent&#39;s ID that you want to download | 
 **file_ids** | [**List[int]**](int.md)| The files&#39;s ID that you want to download | [optional] 
 **user_ip** | **str**| The user&#39;s IP to determine the closest CDN. Optional. | [optional] 
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]
 **request_download_batch** | [**RequestDownloadBatch**](RequestDownloadBatch.md)|  | [optional] 

### Return type

[**RequestTorrentDownloadLinksGetResponse**](RequestTorrentDownloadLinksGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_torrent_download_links_post**
> RequestTorrentDownloadLinksPostResponse request_torrent_download_links_post(token, torrent_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)

Request Download Links - POST

### Overview

Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

### Authorization

Requires an API key as a parameter for the `token` parameter.


### Example


```python
import torbox
from torbox.models.request_download_batch import RequestDownloadBatch
from torbox.models.request_torrent_download_links_post_response import RequestTorrentDownloadLinksPostResponse
from torbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torbox.app
# See configuration.py for a list of all supported configuration parameters.
configuration = torbox.Configuration(
    host = "https://api.torbox.app"
)


# Enter a context with an instance of the API client
with torbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torbox.TorrentsApi(api_client)
    token = 'token_example' # str | Your API Key
    torrent_id = 56 # int | The torrent's ID that you want to download
    file_ids = [56] # List[int] |  (optional)
    user_ip = 'user_ip_example' # str | The user's IP to determine the closest CDN. Optional. (optional)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)
    request_download_batch = {"file_ids":[0,1,2]} # RequestDownloadBatch |  (optional)

    try:
        # Request Download Links - POST
        api_response = api_instance.request_torrent_download_links_post(token, torrent_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)
        print("The response of TorrentsApi->request_torrent_download_links_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TorrentsApi->request_torrent_download_links_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **torrent_id** | **int**| The torrent&#39;s ID that you want to download | 
 **file_ids** | [**List[int]**](int.md)|  | [optional] 
 **user_ip** | **str**| The user&#39;s IP to determine the closest CDN. Optional. | [optional] 
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]
 **request_download_batch** | [**RequestDownloadBatch**](RequestDownloadBatch.md)|  | [optional] 

### Return type

[**RequestTorrentDownloadLinksPostResponse**](RequestTorrentDownloadLinksPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

