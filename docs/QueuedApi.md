# torbox.QueuedApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**control_queued_downloads**](QueuedApi.md#control_queued_downloads) | **POST** /v1/api/queued/controlqueued | Control Queued Downloads
[**get_queued_downloads**](QueuedApi.md#get_queued_downloads) | **GET** /v1/api/queued/getqueued | Get Queued Downloads


# **control_queued_downloads**
> ControlQueuedDownloadsResponse control_queued_downloads(control_queued_download)

Control Queued Downloads

### Overview

Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent.

Operations are either:

- **Delete** `deletes the queued download from your account`

- **Start** `starts a queued download, cannot be used with the "all" parameter`


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.control_queued_download import ControlQueuedDownload
from torbox.models.control_queued_downloads_response import ControlQueuedDownloadsResponse
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
    api_instance = torbox.QueuedApi(api_client)
    control_queued_download = {"queued_id":0,"operation":"delete","all":false} # ControlQueuedDownload | 

    try:
        # Control Queued Downloads
        api_response = api_instance.control_queued_downloads(control_queued_download)
        print("The response of QueuedApi->control_queued_downloads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueuedApi->control_queued_downloads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_queued_download** | [**ControlQueuedDownload**](ControlQueuedDownload.md)|  | 

### Return type

[**ControlQueuedDownloadsResponse**](ControlQueuedDownloadsResponse.md)

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

# **get_queued_downloads**
> GetQueuedDownloadsResponse get_queued_downloads(id=id, type=type, bypass_cache=bypass_cache, offset=offset, limit=limit)

Get Queued Downloads

### Overview

Retrieves all of a user's queued downloads by type. If you want to get all 3 types, "torrent", "usenet" and "webdl" then you will need to run this request 3 times, each with the different type.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_queued_downloads_response import GetQueuedDownloadsResponse
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
    api_instance = torbox.QueuedApi(api_client)
    id = 56 # int | Determines the queued download requested, will return an object rather than list. Optional. (optional)
    type = 'torrent' # str | The type of the queued download you want to retrieve. Can be \"torrent\", \"usenet\" or \"webdl\". Optional. Default is \"torrent\". (optional) (default to 'torrent')
    bypass_cache = False # bool | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. (optional) (default to False)
    offset = 0 # int | Determines the offset of items to get from the database. Default is 0. Optional. (optional) (default to 0)
    limit = 1000 # int | Determines the number of items to recieve per request. Default is 1000. Optional. (optional) (default to 1000)

    try:
        # Get Queued Downloads
        api_response = api_instance.get_queued_downloads(id=id, type=type, bypass_cache=bypass_cache, offset=offset, limit=limit)
        print("The response of QueuedApi->get_queued_downloads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueuedApi->get_queued_downloads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Determines the queued download requested, will return an object rather than list. Optional. | [optional] 
 **type** | **str**| The type of the queued download you want to retrieve. Can be \&quot;torrent\&quot;, \&quot;usenet\&quot; or \&quot;webdl\&quot;. Optional. Default is \&quot;torrent\&quot;. | [optional] [default to &#39;torrent&#39;]
 **bypass_cache** | **bool**| Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. | [optional] [default to False]
 **offset** | **int**| Determines the offset of items to get from the database. Default is 0. Optional. | [optional] [default to 0]
 **limit** | **int**| Determines the number of items to recieve per request. Default is 1000. Optional. | [optional] [default to 1000]

### Return type

[**GetQueuedDownloadsResponse**](GetQueuedDownloadsResponse.md)

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

