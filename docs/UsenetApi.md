# torbox.UsenetApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_create_usenet_download**](UsenetApi.md#async_create_usenet_download) | **POST** /v1/api/usenet/asynccreateusenetdownload | Async Create Usenet Download
[**control_usenet_download**](UsenetApi.md#control_usenet_download) | **POST** /v1/api/usenet/controlusenetdownload | Control Usenet Download
[**create_usenet_download**](UsenetApi.md#create_usenet_download) | **POST** /v1/api/usenet/createusenetdownload | Create Usenet Download
[**edit_usenet_item**](UsenetApi.md#edit_usenet_item) | **PUT** /v1/api/usenet/editusenetdownload | Edit Usenet Item
[**get_news_server_account**](UsenetApi.md#get_news_server_account) | **GET** /v1/api/usenet/provider/account | Get News Server Account
[**get_news_server_connection_information**](UsenetApi.md#get_news_server_connection_information) | **GET** /v1/api/usenet/provider/connection | Get News Server Connection Information
[**get_usenet_cached_availability**](UsenetApi.md#get_usenet_cached_availability) | **GET** /v1/api/usenet/checkcached | Get Usenet Cached Availability
[**get_usenet_cached_availability_batch**](UsenetApi.md#get_usenet_cached_availability_batch) | **POST** /v1/api/usenet/checkcached | Get Usenet Cached Availability Batch
[**get_usenet_list**](UsenetApi.md#get_usenet_list) | **GET** /v1/api/usenet/mylist | Get Usenet List
[**request_usenet_download_link**](UsenetApi.md#request_usenet_download_link) | **GET** /v1/api/usenet/requestdl | Request Download Link
[**request_usenet_download_links_get**](UsenetApi.md#request_usenet_download_links_get) | **GET** /v1/api/usenet/requestdl/batch | Request Download Links - GET
[**request_usenet_download_links_post**](UsenetApi.md#request_usenet_download_links_post) | **POST** /v1/api/usenet/requestdl/batch | Request Download Links - POST
[**reset_news_server_account_password**](UsenetApi.md#reset_news_server_account_password) | **POST** /v1/api/usenet/provider/account/resetpw | Reset News Server Account Password


# **async_create_usenet_download**
> AsyncCreateUsenetDownloadResponse async_create_usenet_download(link=link, file=file, name=name, password=password, post_processing=post_processing, as_queued=as_queued, add_only_if_cached=add_only_if_cached)

Async Create Usenet Download

### Overview

Creates a usenet download asynchronously under your account. Simply send **either** a link, or an nzb file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large.

The request will return instantly, not returning any data other than a success message. This is the same for failures, as they will return the error in the background as a notification, rather than immediately.

The post processing options are the same as for the Create Usenet Download endpoint.

### Rate Limits

This endpoint is rate limited to **60 requests per hour** per API token.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.async_create_usenet_download_response import AsyncCreateUsenetDownloadResponse
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
    api_instance = torbox.UsenetApi(api_client)
    link = 'link_example' # str | An accessible link to an NZB file. Cannot be a redirection. Optional. (optional)
    file = None # bytes | An NZB File. Optional. (optional)
    name = 'name_example' # str | The name you want the usenet download to be. Optional. (optional)
    password = 'password_example' # str | The password to send to the Usenet client. This is used for extracting the RAR at the end. Optional. (optional)
    post_processing = -1 # int | The post processing option to use. Read the overview of the Create Usenet Download endpoint for the options. Default is -1. Optional. (optional) (default to -1)
    as_queued = False # bool | Tells TorBox you want this usenet download instantly queued. Optional. (optional) (default to False)
    add_only_if_cached = False # bool | Only adds the download if it is cached on TorBox. If not cached, it won't be added. (optional) (default to False)

    try:
        # Async Create Usenet Download
        api_response = api_instance.async_create_usenet_download(link=link, file=file, name=name, password=password, post_processing=post_processing, as_queued=as_queued, add_only_if_cached=add_only_if_cached)
        print("The response of UsenetApi->async_create_usenet_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->async_create_usenet_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | **str**| An accessible link to an NZB file. Cannot be a redirection. Optional. | [optional] 
 **file** | **bytes**| An NZB File. Optional. | [optional] 
 **name** | **str**| The name you want the usenet download to be. Optional. | [optional] 
 **password** | **str**| The password to send to the Usenet client. This is used for extracting the RAR at the end. Optional. | [optional] 
 **post_processing** | **int**| The post processing option to use. Read the overview of the Create Usenet Download endpoint for the options. Default is -1. Optional. | [optional] [default to -1]
 **as_queued** | **bool**| Tells TorBox you want this usenet download instantly queued. Optional. | [optional] [default to False]
 **add_only_if_cached** | **bool**| Only adds the download if it is cached on TorBox. If not cached, it won&#39;t be added. | [optional] [default to False]

### Return type

[**AsyncCreateUsenetDownloadResponse**](AsyncCreateUsenetDownloadResponse.md)

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

# **control_usenet_download**
> ControlUsenetDownloadResponse control_usenet_download(control_usenet_download)

Control Usenet Download

### Overview

Controls a usenet download. By sending the usenet download's ID and the type of operation you want to perform, it will send that request to the usenet client.

Operations are either:

- **Delete** `deletes the nzb from the client and your account permanently`


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.control_usenet_download import ControlUsenetDownload
from torbox.models.control_usenet_download_response import ControlUsenetDownloadResponse
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
    api_instance = torbox.UsenetApi(api_client)
    control_usenet_download = {"usenet_id":1,"operation":"delete","all":false} # ControlUsenetDownload | 

    try:
        # Control Usenet Download
        api_response = api_instance.control_usenet_download(control_usenet_download)
        print("The response of UsenetApi->control_usenet_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->control_usenet_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_usenet_download** | [**ControlUsenetDownload**](ControlUsenetDownload.md)|  | 

### Return type

[**ControlUsenetDownloadResponse**](ControlUsenetDownloadResponse.md)

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

# **create_usenet_download**
> CreateUsenetDownloadResponse create_usenet_download(link=link, file=file, name=name, password=password, post_processing=post_processing, as_queued=as_queued, add_only_if_cached=add_only_if_cached)

Create Usenet Download

### Overview

Creates a usenet download under your account. Simply send **either** a link, or an nzb file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large.

#### Post Processing Options:

All post processing options that the Usenet client will perform before TorBox's own processing to make the files available. It is recommended you either don't send this parameter, or keep it at `-1` for default, which will give only the wanted files.

- `-1`, Default. This runs repairs, and extractions as well as deletes the source files leaving only the wanted downloaded files.

- `0`, None. No post-processing at all. Just download all the files (including all PAR2). TorBox will still do its normal processing to make the download available, but no repairs, or extraction will take place.

- `1`, Repair. Download files and do a PAR2 verification. If the verification fails, download more PAR2 files and attempt to repair the files.

- `2`, Repair and Unpack. Download all files, do a PAR2 verification and unpack the files. The final folder will also include the RAR and ZIP files.

- `3`, Repair, Unpack and Delete. Download all files, do a PAR2 verification, unpack the files to the final folder and delete the source files.


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.create_usenet_download_response import CreateUsenetDownloadResponse
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
    api_instance = torbox.UsenetApi(api_client)
    link = 'link_example' # str | An accessible link to an NZB file. Cannot be a redirection. Optional. (optional)
    file = None # bytes | An NZB File. Optional. (optional)
    name = 'name_example' # str | The name you want the usenet download to be. Optional. (optional)
    password = 'password_example' # str | The password to send to the Usenet client. This is used for extracting the RAR at the end. Optional. (optional)
    post_processing = -1 # int | The post processing option to use. Read the overview for the options. Default is -1. Optional. (optional) (default to -1)
    as_queued = False # bool | Tells TorBox you want this usenet download.instantly queued. Optional. (optional) (default to False)
    add_only_if_cached = False # bool | Only adds the download if it is cached on TorBox. If not cached, it won't be added. (optional) (default to False)

    try:
        # Create Usenet Download
        api_response = api_instance.create_usenet_download(link=link, file=file, name=name, password=password, post_processing=post_processing, as_queued=as_queued, add_only_if_cached=add_only_if_cached)
        print("The response of UsenetApi->create_usenet_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->create_usenet_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | **str**| An accessible link to an NZB file. Cannot be a redirection. Optional. | [optional] 
 **file** | **bytes**| An NZB File. Optional. | [optional] 
 **name** | **str**| The name you want the usenet download to be. Optional. | [optional] 
 **password** | **str**| The password to send to the Usenet client. This is used for extracting the RAR at the end. Optional. | [optional] 
 **post_processing** | **int**| The post processing option to use. Read the overview for the options. Default is -1. Optional. | [optional] [default to -1]
 **as_queued** | **bool**| Tells TorBox you want this usenet download.instantly queued. Optional. | [optional] [default to False]
 **add_only_if_cached** | **bool**| Only adds the download if it is cached on TorBox. If not cached, it won&#39;t be added. | [optional] [default to False]

### Return type

[**CreateUsenetDownloadResponse**](CreateUsenetDownloadResponse.md)

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

# **edit_usenet_item**
> EditUsenetItemResponse edit_usenet_item(edit_usenet_download)

Edit Usenet Item

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
from torbox.models.edit_usenet_download import EditUsenetDownload
from torbox.models.edit_usenet_item_response import EditUsenetItemResponse
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
    api_instance = torbox.UsenetApi(api_client)
    edit_usenet_download = {"usenet_download_id":0,"name":"string","tags":["string"],"alternative_hashes":["0123456789abcdef0123456789abcdef01234567"],"airlocked":false} # EditUsenetDownload | 

    try:
        # Edit Usenet Item
        api_response = api_instance.edit_usenet_item(edit_usenet_download)
        print("The response of UsenetApi->edit_usenet_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->edit_usenet_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_usenet_download** | [**EditUsenetDownload**](EditUsenetDownload.md)|  | 

### Return type

[**EditUsenetItemResponse**](EditUsenetItemResponse.md)

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

# **get_news_server_account**
> GetNewsServerAccountResponse get_news_server_account()

Get News Server Account

### Overview

Gets the user's TorBox News Server Account with authentication details. Does not show password if not creating the account. Account creation happens on the first request. If you need to get the password, or reset the password, use the `/usenet/provider/account/resetpw` `POST` endpoint.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_news_server_account_response import GetNewsServerAccountResponse
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
    api_instance = torbox.UsenetApi(api_client)

    try:
        # Get News Server Account
        api_response = api_instance.get_news_server_account()
        print("The response of UsenetApi->get_news_server_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->get_news_server_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNewsServerAccountResponse**](GetNewsServerAccountResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_server_connection_information**
> GetNewsServerConnectionInformationResponse get_news_server_connection_information()

Get News Server Connection Information

### Overview

Gets the TorBox News Server Connection information. This is a static path, and is not dynamic.

### Authorization

No authentication required.


### Example


```python
import torbox
from torbox.models.get_news_server_connection_information_response import GetNewsServerConnectionInformationResponse
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
    api_instance = torbox.UsenetApi(api_client)

    try:
        # Get News Server Connection Information
        api_response = api_instance.get_news_server_connection_information()
        print("The response of UsenetApi->get_news_server_connection_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->get_news_server_connection_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNewsServerConnectionInformationResponse**](GetNewsServerConnectionInformationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usenet_cached_availability**
> GetUsenetCachedAvailabilityResponse get_usenet_cached_availability(hash=hash, format=format, list_files=list_files, check_cached=check_cached)

Get Usenet Cached Availability

### Overview

Takes in a list of comma separated usenet hashes and checks if the usenet download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as:
`?hash=XXXX&hash=XXXX&hash=XXXX`

or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX`
and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour.

You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below.

To get the hash of a usenet download, you can read [this document](https://support.torbox.app/en/articles/13681109-technical-getting-hashes-for-searches) for all of the strategies.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.check_cached import CheckCached
from torbox.models.get_usenet_cached_availability_response import GetUsenetCachedAvailabilityResponse
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
    api_instance = torbox.UsenetApi(api_client)
    hash = ['hash_example'] # List[str] | The list of usenet hashes you want to check. Comma seperated. To find the hash, md5 the link of the usenet link or file. (optional)
    format = 'object' # str | Format you want the data in. Acceptable is either \"object\" or \"list\". List is the most performant option as it doesn't require modification of the list. (optional) (default to 'object')
    list_files = False # bool | Allows you to list the files found inside the cached data. Optional. (optional) (default to False)
    check_cached = torbox.CheckCached() # CheckCached |  (optional)

    try:
        # Get Usenet Cached Availability
        api_response = api_instance.get_usenet_cached_availability(hash=hash, format=format, list_files=list_files, check_cached=check_cached)
        print("The response of UsenetApi->get_usenet_cached_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->get_usenet_cached_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | [**List[str]**](str.md)| The list of usenet hashes you want to check. Comma seperated. To find the hash, md5 the link of the usenet link or file. | [optional] 
 **format** | **str**| Format you want the data in. Acceptable is either \&quot;object\&quot; or \&quot;list\&quot;. List is the most performant option as it doesn&#39;t require modification of the list. | [optional] [default to &#39;object&#39;]
 **list_files** | **bool**| Allows you to list the files found inside the cached data. Optional. | [optional] [default to False]
 **check_cached** | [**CheckCached**](CheckCached.md)|  | [optional] 

### Return type

[**GetUsenetCachedAvailabilityResponse**](GetUsenetCachedAvailabilityResponse.md)

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

# **get_usenet_cached_availability_batch**
> GetUsenetCachedAvailabilityBatchResponse get_usenet_cached_availability_batch(hash=hash, format=format, list_files=list_files, check_cached=check_cached)

Get Usenet Cached Availability Batch

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
from torbox.models.get_usenet_cached_availability_batch_response import GetUsenetCachedAvailabilityBatchResponse
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
    api_instance = torbox.UsenetApi(api_client)
    hash = ['hash_example'] # List[str] |  (optional)
    format = 'object' # str |  (optional) (default to 'object')
    list_files = False # bool |  (optional) (default to False)
    check_cached = {hashes=[string]} # CheckCached |  (optional)

    try:
        # Get Usenet Cached Availability Batch
        api_response = api_instance.get_usenet_cached_availability_batch(hash=hash, format=format, list_files=list_files, check_cached=check_cached)
        print("The response of UsenetApi->get_usenet_cached_availability_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->get_usenet_cached_availability_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | [**List[str]**](str.md)|  | [optional] 
 **format** | **str**|  | [optional] [default to &#39;object&#39;]
 **list_files** | **bool**|  | [optional] [default to False]
 **check_cached** | [**CheckCached**](CheckCached.md)|  | [optional] 

### Return type

[**GetUsenetCachedAvailabilityBatchResponse**](GetUsenetCachedAvailabilityBatchResponse.md)

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

# **get_usenet_list**
> GetUsenetListResponse get_usenet_list(id=id, bypass_cache=bypass_cache, offset=offset, limit=limit, files=files, active=active)

Get Usenet List

### Overview

Gets the user's usenet download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live usenet downloads.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_usenet_list_response import GetUsenetListResponse
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
    api_instance = torbox.UsenetApi(api_client)
    id = 56 # int | Determines the usenet download requested, will return an object rather than list. Optional. (optional)
    bypass_cache = False # bool | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. (optional) (default to False)
    offset = 0 # int | Determines the offset of items to get from the database. Default is 0. Optional. (optional) (default to 0)
    limit = 1000 # int | Determines the number of items to recieve per request. Default is 1000. Optional. (optional) (default to 1000)
    files = True # bool | Exclude files from response. Optional (optional) (default to True)
    active = True # bool | Shows only active downloads. Optional (optional)

    try:
        # Get Usenet List
        api_response = api_instance.get_usenet_list(id=id, bypass_cache=bypass_cache, offset=offset, limit=limit, files=files, active=active)
        print("The response of UsenetApi->get_usenet_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->get_usenet_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Determines the usenet download requested, will return an object rather than list. Optional. | [optional] 
 **bypass_cache** | **bool**| Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. | [optional] [default to False]
 **offset** | **int**| Determines the offset of items to get from the database. Default is 0. Optional. | [optional] [default to 0]
 **limit** | **int**| Determines the number of items to recieve per request. Default is 1000. Optional. | [optional] [default to 1000]
 **files** | **bool**| Exclude files from response. Optional | [optional] [default to True]
 **active** | **bool**| Shows only active downloads. Optional | [optional] 

### Return type

[**GetUsenetListResponse**](GetUsenetListResponse.md)

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

# **request_usenet_download_link**
> RequestUsenetDownloadLinkResponse request_usenet_download_link(token, usenet_id, file_id=file_id, zip_link=zip_link, user_ip=user_ip, redirect=redirect, append_name=append_name)

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
from torbox.models.request_usenet_download_link_response import RequestUsenetDownloadLinkResponse
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
    api_instance = torbox.UsenetApi(api_client)
    token = 'token_example' # str | Your API Key
    usenet_id = 56 # int | The usenet download's ID that you want to download
    file_id = 0 # int | The files's ID that you want to download. Optional if using \"zip_link\". (optional) (default to 0)
    zip_link = False # bool | If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given. (optional) (default to False)
    user_ip = 'user_ip_example' # str | The user's IPv4 to determine the closest CDN. Optional. (optional)
    redirect = False # bool | If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. (optional) (default to False)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)

    try:
        # Request Download Link
        api_response = api_instance.request_usenet_download_link(token, usenet_id, file_id=file_id, zip_link=zip_link, user_ip=user_ip, redirect=redirect, append_name=append_name)
        print("The response of UsenetApi->request_usenet_download_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->request_usenet_download_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **usenet_id** | **int**| The usenet download&#39;s ID that you want to download | 
 **file_id** | **int**| The files&#39;s ID that you want to download. Optional if using \&quot;zip_link\&quot;. | [optional] [default to 0]
 **zip_link** | **bool**| If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given. | [optional] [default to False]
 **user_ip** | **str**| The user&#39;s IPv4 to determine the closest CDN. Optional. | [optional] 
 **redirect** | **bool**| If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. | [optional] [default to False]
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]

### Return type

[**RequestUsenetDownloadLinkResponse**](RequestUsenetDownloadLinkResponse.md)

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

# **request_usenet_download_links_get**
> RequestUsenetDownloadLinksGetResponse request_usenet_download_links_get(token, usenet_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)

Request Download Links - GET

### Overview

Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

### Authorization

Requires an API key as a parameter for the `token` parameter.


### Example


```python
import torbox
from torbox.models.request_download_batch import RequestDownloadBatch
from torbox.models.request_usenet_download_links_get_response import RequestUsenetDownloadLinksGetResponse
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
    api_instance = torbox.UsenetApi(api_client)
    token = 'token_example' # str | Your API Key
    usenet_id = 56 # int | The usenet download's ID that you want to download
    file_ids = [56] # List[int] | The files's ID that you want to download (optional)
    user_ip = 'user_ip_example' # str | The user's IP to determine the closest CDN. Optional. (optional)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)
    request_download_batch = torbox.RequestDownloadBatch() # RequestDownloadBatch |  (optional)

    try:
        # Request Download Links - GET
        api_response = api_instance.request_usenet_download_links_get(token, usenet_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)
        print("The response of UsenetApi->request_usenet_download_links_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->request_usenet_download_links_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **usenet_id** | **int**| The usenet download&#39;s ID that you want to download | 
 **file_ids** | [**List[int]**](int.md)| The files&#39;s ID that you want to download | [optional] 
 **user_ip** | **str**| The user&#39;s IP to determine the closest CDN. Optional. | [optional] 
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]
 **request_download_batch** | [**RequestDownloadBatch**](RequestDownloadBatch.md)|  | [optional] 

### Return type

[**RequestUsenetDownloadLinksGetResponse**](RequestUsenetDownloadLinksGetResponse.md)

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

# **request_usenet_download_links_post**
> RequestUsenetDownloadLinksPostResponse request_usenet_download_links_post(token, usenet_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)

Request Download Links - POST

### Overview

Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

### Authorization

Requires an API key as a parameter for the `token` parameter.


### Example


```python
import torbox
from torbox.models.request_download_batch import RequestDownloadBatch
from torbox.models.request_usenet_download_links_post_response import RequestUsenetDownloadLinksPostResponse
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
    api_instance = torbox.UsenetApi(api_client)
    token = 'token_example' # str | Your API Key
    usenet_id = 56 # int | The usenet downloads' ID that you want to download
    file_ids = [56] # List[int] |  (optional)
    user_ip = 'user_ip_example' # str | The user's IP to determine the closest CDN. Optional. (optional)
    append_name = False # bool | If you want to add the \"filename\" parameter to the returned CDN link. Optional. Default false. (optional) (default to False)
    request_download_batch = {file_ids=[0, 1, 2]} # RequestDownloadBatch |  (optional)

    try:
        # Request Download Links - POST
        api_response = api_instance.request_usenet_download_links_post(token, usenet_id, file_ids=file_ids, user_ip=user_ip, append_name=append_name, request_download_batch=request_download_batch)
        print("The response of UsenetApi->request_usenet_download_links_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->request_usenet_download_links_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your API Key | 
 **usenet_id** | **int**| The usenet downloads&#39; ID that you want to download | 
 **file_ids** | [**List[int]**](int.md)|  | [optional] 
 **user_ip** | **str**| The user&#39;s IP to determine the closest CDN. Optional. | [optional] 
 **append_name** | **bool**| If you want to add the \&quot;filename\&quot; parameter to the returned CDN link. Optional. Default false. | [optional] [default to False]
 **request_download_batch** | [**RequestDownloadBatch**](RequestDownloadBatch.md)|  | [optional] 

### Return type

[**RequestUsenetDownloadLinksPostResponse**](RequestUsenetDownloadLinksPostResponse.md)

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

# **reset_news_server_account_password**
> ResetNewsServerAccountPasswordResponse reset_news_server_account_password()

Reset News Server Account Password

### Overview

Resets the user's TorBox News Server account password. This password is automatically generated, and is not saved, it is only shown once.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.reset_news_server_account_password_response import ResetNewsServerAccountPasswordResponse
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
    api_instance = torbox.UsenetApi(api_client)

    try:
        # Reset News Server Account Password
        api_response = api_instance.reset_news_server_account_password()
        print("The response of UsenetApi->reset_news_server_account_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsenetApi->reset_news_server_account_password: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResetNewsServerAccountPasswordResponse**](ResetNewsServerAccountPasswordResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

