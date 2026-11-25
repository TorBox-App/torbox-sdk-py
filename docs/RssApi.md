# torbox.RssApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rss_feed**](RssApi.md#add_rss_feed) | **POST** /v1/api/rss/addrss | Add RSS Feed
[**control_rss_feed**](RssApi.md#control_rss_feed) | **POST** /v1/api/rss/controlrss | Control RSS Feed
[**edit_rss_feed**](RssApi.md#edit_rss_feed) | **POST** /v1/api/rss/modifyrss | Edit RSS Feed
[**get_rss_feed_items**](RssApi.md#get_rss_feed_items) | **GET** /v1/api/rss/getfeeditems | Get RSS Feed Items
[**get_user_rss_feeds**](RssApi.md#get_user_rss_feeds) | **GET** /v1/api/rss/getfeeds | Get User RSS Feeds


# **add_rss_feed**
> AddRssFeedResponse add_rss_feed(add_rss)

Add RSS Feed

### Overview

Allows adding an RSS feed to your account. This API gives you a lot of customization options, but is best used with the UI on the website. This endpoint only works for Pro users (plan: 2).

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.add_rss import AddRss
from torbox.models.add_rss_feed_response import AddRssFeedResponse
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
    api_instance = torbox.RssApi(api_client)
    add_rss = {"url":"https://example.com/feed.xml","name":"string","do_regex":"string","dont_regex":"string","dont_older_than":0,"scan_interval":0,"pass_check":false,"rss_type":"torrent","torrent_seeding":1} # AddRss | 

    try:
        # Add RSS Feed
        api_response = api_instance.add_rss_feed(add_rss)
        print("The response of RssApi->add_rss_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RssApi->add_rss_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_rss** | [**AddRss**](AddRss.md)|  | 

### Return type

[**AddRssFeedResponse**](AddRssFeedResponse.md)

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

# **control_rss_feed**
> ControlRssFeedResponse control_rss_feed(control_rss)

Control RSS Feed

### Overview

Controls an RSS Feed. By sending the RSS feed's ID and the type of operation you want to perform, it will perform said action on the RSS feed checker.

Operations are either:

- **Update** `forces an update on the rss feed`
- **Delete** `deletes the rss feed from your account permanently. This also deletes all associated RSS feed items. This does not remove queued items spawned from the RSS feed.`
- **Pause** `pauses checking the rss feed on the scan interval`
- **Resume** `resumes a paused rss feed`


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.control_rss import ControlRss
from torbox.models.control_rss_feed_response import ControlRssFeedResponse
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
    api_instance = torbox.RssApi(api_client)
    control_rss = {"operation":"pause","rss_feed_id":0} # ControlRss | 

    try:
        # Control RSS Feed
        api_response = api_instance.control_rss_feed(control_rss)
        print("The response of RssApi->control_rss_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RssApi->control_rss_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_rss** | [**ControlRss**](ControlRss.md)|  | 

### Return type

[**ControlRssFeedResponse**](ControlRssFeedResponse.md)

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

# **edit_rss_feed**
> EditRssFeedResponse edit_rss_feed(modify_rss)

Edit RSS Feed

### Overview

Allows you to edit the RSS feed based on the RSS feed ID passed. Allows you to change everything about an RSS feed, except for the URL.

When updating the "rss_type" or the "torrent_seeding" options, it will update all of the RSS items associated with the RSS feed, including all previous items.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.edit_rss_feed_response import EditRssFeedResponse
from torbox.models.modify_rss import ModifyRss
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
    api_instance = torbox.RssApi(api_client)
    modify_rss = {"rss_feed_id":0,"name":"string","do_regex":"string","dont_regex":"string","dont_older_than":0,"scan_interval":0,"rss_type":"torrent","torrent_seeding":1} # ModifyRss | 

    try:
        # Edit RSS Feed
        api_response = api_instance.edit_rss_feed(modify_rss)
        print("The response of RssApi->edit_rss_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RssApi->edit_rss_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_rss** | [**ModifyRss**](ModifyRss.md)|  | 

### Return type

[**EditRssFeedResponse**](EditRssFeedResponse.md)

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

# **get_rss_feed_items**
> GetRssFeedItemsResponse get_rss_feed_items(rss_feed_id)

Get RSS Feed Items

### Overview

Gets the first 10,000 RSS feed items associated with an RSS feed. RSS feed items are scraped items from the RSS feed. They contain a direct download link as well as the content name, and additional information.

##### Type Key

The "type" key in the response is used for showing what type of downloads this RSS feed item is. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct. When the parent RSS feed's type is changed, it changes all of the items types as well.

- **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.`
- "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.`
- "webdl" `uses generic links and adds as a web download when downloaded.`


##### Status Key

The "status" key tells the status of the RSS feed item. This is useful for seeing what the item is doing, and what it will do next. Each item also includes a "status_message" key which gives a user friendly message about anything about the RSS feed item, such as errors and explainations.

- "new" `the RSS feed item is set to be downloaded.`
- "ignored" `the RSS feed item has been ignored due to the parents RSS feed settings, as it doesn't match the chosen settings. The item will not be downloaded.`
- "error" `the RSS feed item had an error while attempting to download. The item will be retried on the next scrape.`
- "downloaded" `the RSS feed item has already been downloaded to the user's account. It will not be downloaded again.`


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_rss_feed_items_response import GetRssFeedItemsResponse
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
    api_instance = torbox.RssApi(api_client)
    rss_feed_id = 56 # int | The RSS Feed ID of the RSS Feed you want to retrieve the scraped items of.

    try:
        # Get RSS Feed Items
        api_response = api_instance.get_rss_feed_items(rss_feed_id)
        print("The response of RssApi->get_rss_feed_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RssApi->get_rss_feed_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rss_feed_id** | **int**| The RSS Feed ID of the RSS Feed you want to retrieve the scraped items of. | 

### Return type

[**GetRssFeedItemsResponse**](GetRssFeedItemsResponse.md)

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

# **get_user_rss_feeds**
> GetUserRssFeedsResponse get_user_rss_feeds(id=id)

Get User RSS Feeds

### Overview

Gets all of a user's RSS feeds located on their account. Can only be accessed on a Pro (plan: 2) account. Also allows you to get a specific by passing an "id" in the parameters.

##### Type Key

The "type" key in the response is used for showing what type of downloads are spawned from this RSS feed. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct.

- **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.`
- "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.`
- "webdl" `uses generic links and adds as a web download when downloaded.`


##### Status Key

The "status" key tells the user selected status of the RSS feed. These statuses are **not** the same as the status key for the RSS items associated with the RSS feed. Each feed also includes a "status_message" key which gives a user friendly message about anything about the RSS feed, such as errors and explainations.

- "active" `the RSS feed is set to be scraped.`
- "paused" `the RSS feed will not be scraped as it is paused by the user.`

- "error" `the RSS feed had an error while scraping, and cannot continue.`


##### State Key

The "state" key tells you exactly in real time, what the RSS feed is doing. This is useful for realtime status updates.

- "idle" `the RSS feed is idle, and is currently not doing anything in the current moment.`
- "scraping" `the RSS feed is currently scraping new RSS items.`
- "downloading" `the RSS feed is currently downloading the newly scraped RSS items.`


##### Torrent Seeding Key

The "torrent_seeding" key is returned with every response, regardless of the type of the RSS feed. This controls what seeding setting the RSS feed is using when it adds new torrents. These are the same options as when adding a torrent using the /torrent/createtorrent endpoint.

> Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings.


- 1 `auto, the torrent will seed based on what the user has in their settings.`
- 2 `always, TorBox will be instructed to seed this torrent regardless of any other settings.`
- 3 `never, TorBox will not seed this torrent.`


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_user_rss_feeds_response import GetUserRssFeedsResponse
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
    api_instance = torbox.RssApi(api_client)
    id = 56 # int | A specific RSS feed ID that you want to retrieve. Optional. (optional)

    try:
        # Get User RSS Feeds
        api_response = api_instance.get_user_rss_feeds(id=id)
        print("The response of RssApi->get_user_rss_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RssApi->get_user_rss_feeds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A specific RSS feed ID that you want to retrieve. Optional. | [optional] 

### Return type

[**GetUserRssFeedsResponse**](GetUserRssFeedsResponse.md)

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

