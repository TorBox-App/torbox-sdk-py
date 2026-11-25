# torbox.GeneralApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get30_day_stats**](GeneralApi.md#get30_day_stats) | **GET** /v1/api/stats/30days | Get 30 Day Stats
[**get_changelogs_json**](GeneralApi.md#get_changelogs_json) | **GET** /v1/api/changelogs/json | Get Changelogs JSON
[**get_changelogs_rss_feed**](GeneralApi.md#get_changelogs_rss_feed) | **GET** /v1/api/changelogs/rss | Get Changelogs RSS Feed
[**get_speedtest_files**](GeneralApi.md#get_speedtest_files) | **GET** /v1/api/speedtest | Get Speedtest Files
[**get_stats**](GeneralApi.md#get_stats) | **GET** /v1/api/stats | Get Stats
[**get_up_status**](GeneralApi.md#get_up_status) | **GET** / | Get Up Status


# **get30_day_stats**
> Get30DayStatsResponse get30_day_stats()

Get 30 Day Stats

### Overview

Gets the general stats of the TorBox service for the last 30 days, one entry per day. Each entry is a snapshot of the totals at that time.

### Authorization

None needed.


### Example


```python
import torbox
from torbox.models.get30_day_stats_response import Get30DayStatsResponse
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
    api_instance = torbox.GeneralApi(api_client)

    try:
        # Get 30 Day Stats
        api_response = api_instance.get30_day_stats()
        print("The response of GeneralApi->get30_day_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get30_day_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Get30DayStatsResponse**](Get30DayStatsResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changelogs_json**
> GetChangelogsJsonResponse get_changelogs_json(offset=offset, limit=limit)

Get Changelogs JSON

### Overview

Gets most recent changelogs from [https://feedback.torbox.app/changelog](https://feedback.torbox.app/changelog). This is useful for developers who want to integrate the changelog into their apps for their users to see. Includes content in HTML for developers to easily render the text in a fancy yet simple way.

### Authorization

None needed.


### Example


```python
import torbox
from torbox.models.get_changelogs_json_response import GetChangelogsJsonResponse
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
    api_instance = torbox.GeneralApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Changelogs JSON
        api_response = api_instance.get_changelogs_json(offset=offset, limit=limit)
        print("The response of GeneralApi->get_changelogs_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_changelogs_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**GetChangelogsJsonResponse**](GetChangelogsJsonResponse.md)

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
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changelogs_rss_feed**
> str get_changelogs_rss_feed(offset=offset, limit=limit)

Get Changelogs RSS Feed

### Overview

Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog](https://feedback.torbox.app/changelog). This is useful for people who want updates on the TorBox changelog. Includes all the necessary items to make this compatible with RSS feed viewers for notifications, and proper HTML viewing.

### Authorization

None needed.


### Example


```python
import torbox
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
    api_instance = torbox.GeneralApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Changelogs RSS Feed
        api_response = api_instance.get_changelogs_rss_feed(offset=offset, limit=limit)
        print("The response of GeneralApi->get_changelogs_rss_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_changelogs_rss_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_speedtest_files**
> GetSpeedtestFilesResponse get_speedtest_files(user_ip=user_ip, region=region, test_length=test_length)

Get Speedtest Files

### Overview

Gets CDN speedtest files. This can be used for speedtesting TorBox for users or other usages, such as checking download speeds for verification. Provides all necessary data such as region, server name, and even coordinates. Uses the requesting IP to determine if the server is the closest to the user.

You also have the ability to choose between long tests or short tests via the "test_length" parameter. You may also force the region selection by passing the "region" as a specific region.

### Authorization

None needed.


### Example


```python
import torbox
from torbox.models.get_speedtest_files_response import GetSpeedtestFilesResponse
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
    api_instance = torbox.GeneralApi(api_client)
    user_ip = 'user_ip_example' # str | Pass a user's IP to get the closest server to them, otherwise will use the calling IP for location. (optional)
    region = 'all' # str | Determines what cdns are returned. May be any region that TorBox is located in. To get this value, send a request without this value to determine all of the available regions that are available. (optional) (default to 'all')
    test_length = 'short' # str | Determines the size of the file used for the speedtest. May be \"long\" or \"short\". Optional. (optional) (default to 'short')

    try:
        # Get Speedtest Files
        api_response = api_instance.get_speedtest_files(user_ip=user_ip, region=region, test_length=test_length)
        print("The response of GeneralApi->get_speedtest_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_speedtest_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ip** | **str**| Pass a user&#39;s IP to get the closest server to them, otherwise will use the calling IP for location. | [optional] 
 **region** | **str**| Determines what cdns are returned. May be any region that TorBox is located in. To get this value, send a request without this value to determine all of the available regions that are available. | [optional] [default to &#39;all&#39;]
 **test_length** | **str**| Determines the size of the file used for the speedtest. May be \&quot;long\&quot; or \&quot;short\&quot;. Optional. | [optional] [default to &#39;short&#39;]

### Return type

[**GetSpeedtestFilesResponse**](GetSpeedtestFilesResponse.md)

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
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> GetStatsResponse get_stats()

Get Stats

### Overview

Simply gets general stats about the TorBox service.

### Authorization

None needed.


### Example


```python
import torbox
from torbox.models.get_stats_response import GetStatsResponse
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
    api_instance = torbox.GeneralApi(api_client)

    try:
        # Get Stats
        api_response = api_instance.get_stats()
        print("The response of GeneralApi->get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatsResponse**](GetStatsResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_up_status**
> GetUpStatusResponse get_up_status()

Get Up Status

### Overview

Simply gets if the TorBox API is available for use or not. Also might include information about downtimes.

### Authorization

None needed.


### Example


```python
import torbox
from torbox.models.get_up_status_response import GetUpStatusResponse
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
    api_instance = torbox.GeneralApi(api_client)

    try:
        # Get Up Status
        api_response = api_instance.get_up_status()
        print("The response of GeneralApi->get_up_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_up_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUpStatusResponse**](GetUpStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**502** | Bad Gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

