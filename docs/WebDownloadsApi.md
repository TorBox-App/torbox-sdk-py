# torbox.WebDownloadsApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_create_web_download**](WebDownloadsApi.md#async_create_web_download) | **POST** /v1/api/webdl/asynccreatewebdownload | Async Create Web Download
[**control_web_download**](WebDownloadsApi.md#control_web_download) | **POST** /v1/api/webdl/controlwebdownload | Control Web Download
[**create_web_download**](WebDownloadsApi.md#create_web_download) | **POST** /v1/api/webdl/createwebdownload | Create Web Download
[**edit_web_download_item**](WebDownloadsApi.md#edit_web_download_item) | **PUT** /v1/api/webdl/editwebdownload | Edit Web Download Item
[**get_hoster_list**](WebDownloadsApi.md#get_hoster_list) | **GET** /v1/api/webdl/hosters | Get Hoster List
[**get_web_download_cached_availability**](WebDownloadsApi.md#get_web_download_cached_availability) | **GET** /v1/api/webdl/checkcached | Get Web Download Cached Availability
[**get_web_download_cached_availability_batch**](WebDownloadsApi.md#get_web_download_cached_availability_batch) | **POST** /v1/api/webdl/checkcached | Get Web Download Cached Availability Batch
[**get_web_download_list**](WebDownloadsApi.md#get_web_download_list) | **GET** /v1/api/webdl/mylist | Get Web Download List
[**request_web_download_link**](WebDownloadsApi.md#request_web_download_link) | **GET** /v1/api/webdl/requestdl | Request Download Link
[**request_web_download_links_get**](WebDownloadsApi.md#request_web_download_links_get) | **GET** /v1/api/webdl/requestdl/batch | Request Download Links - GET
[**request_web_download_links_post**](WebDownloadsApi.md#request_web_download_links_post) | **POST** /v1/api/webdl/requestdl/batch | Request Download Links - POST


# **async_create_web_download**
> AsyncCreateWebDownloadResponse async_create_web_download(link, password=password, name=name, as_queued=as_queued, add_only_if_cached=add_only_if_cached)

Async Create Web Download

### Overview

Creates a web download asynchronously under your account. Simply send a link to any file on the internet. Once it has been checked, it will begin downloading assuming your account has available active download slots, and they aren't too large.

The request will return instantly, not returning any data other than a success message. This is the same for failures, as they will return the error in the background as a notification, rather than immediately.

### Rate Limits

This endpoint is rate limited to **60 requests per hour** per API token.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.async_create_web_download_response import AsyncCreateWebDownloadResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    link = 'link_example' # str | An accessible link to any file on the internet. Cannot be a redirection.
    password = 'password_example' # str | Password to the file, if the files requires it. Optional. (optional)
    name = 'name_example' # str | The name you want the web download to be. Optional. (optional)
    as_queued = False # bool | Tells TorBox you want this web download instantly queued. Optional. (optional) (default to False)
    add_only_if_cached = False # bool | Only adds the download if it is cached on TorBox. If not cached, it won't be added. (optional) (default to False)

    try:
        # Async Create Web Download
        api_response = api_instance.async_create_web_download(link, password=password, name=name, as_queued=as_queued, add_only_if_cached=add_only_if_cached)
        print("The response of WebDownloadsApi->async_create_web_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->async_create_web_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | **str**| An accessible link to any file on the internet. Cannot be a redirection. | 
 **password** | **str**| Password to the file, if the files requires it. Optional. | [optional] 
 **name** | **str**| The name you want the web download to be. Optional. | [optional] 
 **as_queued** | **bool**| Tells TorBox you want this web download instantly queued. Optional. | [optional] [default to False]
 **add_only_if_cached** | **bool**| Only adds the download if it is cached on TorBox. If not cached, it won&#39;t be added. | [optional] [default to False]

### Return type

[**AsyncCreateWebDownloadResponse**](AsyncCreateWebDownloadResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
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

# **control_web_download**
> ControlWebDownloadResponse control_web_download(control_web_download)

Control Web Download

### Overview

Controls a web download. By sending the web download's ID and the type of operation you want to perform, it will send that request to the debrid client.

Operations are either:

- **Delete** `deletes the download from the client and your account permanently`


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.control_web_download import ControlWebDownload
from torbox.models.control_web_download_response import ControlWebDownloadResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    control_web_download = {"webdl_id":1,"operation":"delete","all":false} # ControlWebDownload | 

    try:
        # Control Web Download
        api_response = api_instance.control_web_download(control_web_download)
        print("The response of WebDownloadsApi->control_web_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->control_web_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_web_download** | [**ControlWebDownload**](ControlWebDownload.md)|  | 

### Return type

[**ControlWebDownloadResponse**](ControlWebDownloadResponse.md)

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

# **create_web_download**
> CreateWebDownloadResponse create_web_download(link, password=password, name=name, as_queued=as_queued, add_only_if_cached=add_only_if_cached)

Create Web Download

### Overview

Creates a web download under your account. Simply send a link to any file on the internet. Once it has been checked, it will begin downloading assuming your account has available active download slots, and they aren't too large.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.create_web_download_response import CreateWebDownloadResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    link = 'link_example' # str | An accessible link to any file on the internet. Cannot be a redirection.
    password = 'password_example' # str | Password to the file, if the files requires it. Optional. (optional)
    name = 'name_example' # str | The name you want the torrent to be. Optional. (optional)
    as_queued = False # bool | Tells TorBox you want this web download.instantly queued. Optional. (optional) (default to False)
    add_only_if_cached = False # bool | Only adds the download if it is cached on TorBox. If not cached, it won't be added. (optional) (default to False)

    try:
        # Create Web Download
        api_response = api_instance.create_web_download(link, password=password, name=name, as_queued=as_queued, add_only_if_cached=add_only_if_cached)
        print("The response of WebDownloadsApi->create_web_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->create_web_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | **str**| An accessible link to any file on the internet. Cannot be a redirection. | 
 **password** | **str**| Password to the file, if the files requires it. Optional. | [optional] 
 **name** | **str**| The name you want the torrent to be. Optional. | [optional] 
 **as_queued** | **bool**| Tells TorBox you want this web download.instantly queued. Optional. | [optional] [default to False]
 **add_only_if_cached** | **bool**| Only adds the download if it is cached on TorBox. If not cached, it won&#39;t be added. | [optional] [default to False]

### Return type

[**CreateWebDownloadResponse**](CreateWebDownloadResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
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

# **edit_web_download_item**
> EditWebDownloadItemResponse edit_web_download_item(edit_web_download)

Edit Web Download Item

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
from torbox.models.edit_web_download import EditWebDownload
from torbox.models.edit_web_download_item_response import EditWebDownloadItemResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    edit_web_download = {"webdl_id":0,"name":"string","tags":["string"],"alternative_hashes":["0123456789abcdef0123456789abcdef01234567"],"airlocked":false} # EditWebDownload | 

    try:
        # Edit Web Download Item
        api_response = api_instance.edit_web_download_item(edit_web_download)
        print("The response of WebDownloadsApi->edit_web_download_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->edit_web_download_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_web_download** | [**EditWebDownload**](EditWebDownload.md)|  | 

### Return type

[**EditWebDownloadItemResponse**](EditWebDownloadItemResponse.md)

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

# **get_hoster_list**
> GetHosterListResponse get_hoster_list()

Get Hoster List

### Overview

A dynamic list of hosters that TorBox is capable of downloading through its paid service.

- **Name** - a clean name for display use, the well known name of the service, should be recognizable to users.

- **Domains** - an array of known domains that the hoster uses. While each may serve a different purpose it is still included.

- **URL** - the main url of the service. This should take you to the home page or a service page of the hoster.

- **Icon** - a square image, usually a favicon or logo, that represents the service, should be recognizable as the hoster's icon.

- **Status** - whether this hoster can be used on TorBox or not at the current time. It is usually a good idea to check this value before submitting a download to TorBox's servers for download.

- **Type** - values are either "hoster" or "stream". Both do the same thing, but is good to differentiate services used for different things.

- **Note** - a string value (or null) that may give helpful information about the current status or state of a hoster. This can and should be shown to end users.

- **Daily Link Limit** - the number of downloads a user can use per day. As a user submits links, once they hit this number, the API will deny them from adding anymore of this type of link. A zero value means that it is unlimited.

- **Daily Link Used** - the number of downloads a user has already used. Usually zero unless you send authentication to the endpoint. This will return accurate values.

- **Daily Bandwidth Limit** - the value in bytes that a user is allowed to download from this hoster. A zero value means that it is unlimited. It is recommended to use the Daily Link Limit instead.

- **Daily Bandwidth Used** - the value in bytes that a user has already used to download from this hoster. Usually zero unless you send authentication to the endpoint. This will return accurate values.


### Authorization

Optional authorization. Authorization is not required in this endpoint unless you want to get the user's live data. Requires an API key using the Authorization Bearer Header to get the live and accurate data for **Daily Link Used** and **Daily Bandwidth Used**.


### Example


```python
import torbox
from torbox.models.get_hoster_list_response import GetHosterListResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)

    try:
        # Get Hoster List
        api_response = api_instance.get_hoster_list()
        print("The response of WebDownloadsApi->get_hoster_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->get_hoster_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetHosterListResponse**](GetHosterListResponse.md)

### Authorization

No authorization required

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
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_download_cached_availability**
> GetWebDownloadCachedAvailabilityResponse get_web_download_cached_availability(hash=hash, format=format, list_files=list_files, check_cached=check_cached)

Get Web Download Cached Availability

### Overview

Takes in a list of comma separated usenet hashes and checks if the web download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as:
`?hash=XXXX&hash=XXXX&hash=XXXX`

or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX`
and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour.

You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below.

To get the hash of a web download you can read [this document](https://support.torbox.app/en/articles/13681109-technical-getting-hashes-for-searches) for all of the strategies.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.check_cached import CheckCached
from torbox.models.get_web_download_cached_availability_response import GetWebDownloadCachedAvailabilityResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    hash = ['hash_example'] # List[str] | The list of web hashes you want to check. Comma seperated. To find the hash, md5 the link. (optional)
    format = 'object' # str | Format you want the data in. Acceptable is either \"object\" or \"list\". List is the most performant option as it doesn't require modification of the list. (optional) (default to 'object')
    list_files = False # bool | Allows you to list the files found inside the cached data. (optional) (default to False)
    check_cached = torbox.CheckCached() # CheckCached |  (optional)

    try:
        # Get Web Download Cached Availability
        api_response = api_instance.get_web_download_cached_availability(hash=hash, format=format, list_files=list_files, check_cached=check_cached)
        print("The response of WebDownloadsApi->get_web_download_cached_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->get_web_download_cached_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | [**List[str]**](str.md)| The list of web hashes you want to check. Comma seperated. To find the hash, md5 the link. | [optional] 
 **format** | **str**| Format you want the data in. Acceptable is either \&quot;object\&quot; or \&quot;list\&quot;. List is the most performant option as it doesn&#39;t require modification of the list. | [optional] [default to &#39;object&#39;]
 **list_files** | **bool**| Allows you to list the files found inside the cached data. | [optional] [default to False]
 **check_cached** | [**CheckCached**](CheckCached.md)|  | [optional] 

### Return type

[**GetWebDownloadCachedAvailabilityResponse**](GetWebDownloadCachedAvailabilityResponse.md)

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

# **get_web_download_cached_availability_batch**
> GetWebDownloadCachedAvailabilityBatchResponse get_web_download_cached_availability_batch(hash=hash, format=format, list_files=list_files, check_cached=check_cached)

Get Web Download Cached Availability Batch

### Overview

Takes in a list of comma separated hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters.

Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour.

You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.check_cached import CheckCached
from torbox.models.get_web_download_cached_availability_batch_response import GetWebDownloadCachedAvailabilityBatchResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    hash = ['hash_example'] # List[str] |  (optional)
    format = 'object' # str | Format you want the data in. Acceptable is either \"object\" or \"list\". List is the most performant option as it doesn't require modification of the list. (optional) (default to 'object')
    list_files = False # bool | Allows you to list the files found inside the cached data. (optional) (default to False)
    check_cached = {"hashes":["string"]} # CheckCached |  (optional)

    try:
        # Get Web Download Cached Availability Batch
        api_response = api_instance.get_web_download_cached_availability_batch(hash=hash, format=format, list_files=list_files, check_cached=check_cached)
        print("The response of WebDownloadsApi->get_web_download_cached_availability_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->get_web_download_cached_availability_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**| Format you want the data in. Acceptable is either \&quot;object\&quot; or \&quot;list\&quot;. List is the most performant option as it doesn&#39;t require modification of the list. | [optional] [default to &#39;object&#39;]
 **list_files** | **bool**| Allows you to list the files found inside the cached data. | [optional] [default to False]
 **check_cached** | [**CheckCached**](CheckCached.md)|  | [optional] 

### Return type

[**GetWebDownloadCachedAvailabilityBatchResponse**](GetWebDownloadCachedAvailabilityBatchResponse.md)

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

# **get_web_download_list**
> GetWebDownloadListResponse get_web_download_list(id=id, bypass_cache=bypass_cache, offset=offset, limit=limit, files=files, active=active)

Get Web Download List

### Overview

Gets the user's web download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live web downloads.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_web_download_list_response import GetWebDownloadListResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    id = 56 # int | Determines the torrent requested, will return an object rather than list. Optional. (optional)
    bypass_cache = False # bool | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. (optional) (default to False)
    offset = 0 # int | Determines the offset of items to get from the database. Default is 0. Optional. (optional) (default to 0)
    limit = 1000 # int | Determines the number of items to recieve per request. Default is 1000. Optional. (optional) (default to 1000)
    files = True # bool | Exclude files from response. Optional (optional) (default to True)
    active = True # bool | Shows only active downloads. Optional (optional)

    try:
        # Get Web Download List
        api_response = api_instance.get_web_download_list(id=id, bypass_cache=bypass_cache, offset=offset, limit=limit, files=files, active=active)
        print("The response of WebDownloadsApi->get_web_download_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->get_web_download_list: %s\n" % e)
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

[**GetWebDownloadListResponse**](GetWebDownloadListResponse.md)

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

# **request_web_download_link**
> RequestWebDownloadLinkResponse request_web_download_link(token, web_id, file_id=file_id, zip_link=zip_link, user_ip=user_ip, redirect=redirect, append_name=append_name)

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
from torbox.models.request_web_download_link_response import RequestWebDownloadLinkResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    token = 'token_example' # str | Your API Key
    web_id = 56 # int | The web download's ID that you want to download
    file_id = 0 # int | The files's ID that you want to download (optional) (default to 0)
    zip_link = False # bool | If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given. (optional) (default to False)
    user_ip = 'user_ip_example' # str | The user's IP to determine the closest CDN. Optional. (optional)
    redirect = False # bool | If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. (optional) (default to False)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)

    try:
        # Request Download Link
        api_response = api_instance.request_web_download_link(token, web_id, file_id=file_id, zip_link=zip_link, user_ip=user_ip, redirect=redirect, append_name=append_name)
        print("The response of WebDownloadsApi->request_web_download_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->request_web_download_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **web_id** | **int**| The web download&#39;s ID that you want to download | 
 **file_id** | **int**| The files&#39;s ID that you want to download | [optional] [default to 0]
 **zip_link** | **bool**| If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given. | [optional] [default to False]
 **user_ip** | **str**| The user&#39;s IP to determine the closest CDN. Optional. | [optional] 
 **redirect** | **bool**| If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. | [optional] [default to False]
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]

### Return type

[**RequestWebDownloadLinkResponse**](RequestWebDownloadLinkResponse.md)

### Authorization

No authorization required

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

# **request_web_download_links_get**
> RequestWebDownloadLinksGetResponse request_web_download_links_get(token, web_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)

Request Download Links - GET

### Overview

Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

### Authorization

Requires an API key as a parameter for the `token` parameter.


### Example


```python
import torbox
from torbox.models.request_download_batch import RequestDownloadBatch
from torbox.models.request_web_download_links_get_response import RequestWebDownloadLinksGetResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    token = 'token_example' # str | Your API Key
    web_id = 56 # int | The web download's ID that you want to download
    file_ids = [56] # List[int] | The files's ID that you want to download (optional)
    user_ip = 'user_ip_example' # str | The user's IP to determine the closest CDN. Optional. (optional)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)
    request_download_batch = torbox.RequestDownloadBatch() # RequestDownloadBatch |  (optional)

    try:
        # Request Download Links - GET
        api_response = api_instance.request_web_download_links_get(token, web_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)
        print("The response of WebDownloadsApi->request_web_download_links_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->request_web_download_links_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **web_id** | **int**| The web download&#39;s ID that you want to download | 
 **file_ids** | [**List[int]**](int.md)| The files&#39;s ID that you want to download | [optional] 
 **user_ip** | **str**| The user&#39;s IP to determine the closest CDN. Optional. | [optional] 
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]
 **request_download_batch** | [**RequestDownloadBatch**](RequestDownloadBatch.md)|  | [optional] 

### Return type

[**RequestWebDownloadLinksGetResponse**](RequestWebDownloadLinksGetResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_web_download_links_post**
> RequestWebDownloadLinksPostResponse request_web_download_links_post(token, web_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)

Request Download Links - POST

### Overview

Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

### Authorization

Requires an API key as a parameter for the `token` parameter.


### Example


```python
import torbox
from torbox.models.request_download_batch import RequestDownloadBatch
from torbox.models.request_web_download_links_post_response import RequestWebDownloadLinksPostResponse
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
    api_instance = torbox.WebDownloadsApi(api_client)
    token = 'token_example' # str | Your API Key
    web_id = 56 # int | The web downloads' ID that you want to download
    file_ids = [56] # List[int] |  (optional)
    user_ip = 'user_ip_example' # str | The user's IP to determine the closest CDN. Optional. (optional)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)
    request_download_batch = {file_ids=[0, 1, 2]} # RequestDownloadBatch |  (optional)

    try:
        # Request Download Links - POST
        api_response = api_instance.request_web_download_links_post(token, web_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)
        print("The response of WebDownloadsApi->request_web_download_links_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDownloadsApi->request_web_download_links_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **web_id** | **int**| The web downloads&#39; ID that you want to download | 
 **file_ids** | [**List[int]**](int.md)|  | [optional] 
 **user_ip** | **str**| The user&#39;s IP to determine the closest CDN. Optional. | [optional] 
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]
 **request_download_batch** | [**RequestDownloadBatch**](RequestDownloadBatch.md)|  | [optional] 

### Return type

[**RequestWebDownloadLinksPostResponse**](RequestWebDownloadLinksPostResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

