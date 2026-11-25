# torbox.StreamApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stream**](StreamApi.md#create_stream) | **GET** /v1/api/stream/createstream | Create Stream
[**get_stream_data**](StreamApi.md#get_stream_data) | **GET** /v1/api/stream/getstreamdata | Get Stream Data


# **create_stream**
> CreateStreamResponse create_stream(id, file_id=file_id, type=type, chosen_subtitle_index=chosen_subtitle_index, chosen_audio_index=chosen_audio_index, chosen_resolution_index=chosen_resolution_index, scrobbling_enabled=scrobbling_enabled)

Create Stream

### Overview

Creates a new stream based off of the data provided.

#### Selecting Subtitles and Audios

We use indexes to determine which audio and subtitle you would like to select. To view all available indexes, you must request this endpoint intially with "null" or 0, for the chosen indexes. This will return a metadata dictionary in the response, which will contain the list of audios and subtitles available for this stream. When choosing a subtitle or audio stream, use the **relative index**, starting from 0, rather than the "index" value. This is important for selecting the correct index. Once your user gets a selection of audios and subtitles available, you can submit this to the endpoint again to get the chosen stream.

- **null** - Selecting no subtitle. Not available for audio as one must always be selected.

- **0** - Selecting first subtitle or audio


#### Selecting Resolution

Similar to the subtitles and audios, we use indexes to determine the resolution chosen. Unlike the above, these are predetermined. We do not upscale video, so if for example, you pass a 1080p video, and request it with resolution, 7, it will stay at 1080p. Please see the below for options.

- **null** - Original video resolution. No downscaling will take place.

- **0** - 144p

- **1** - 240p

- **2** - 360p

- **3** - 480p

- **4** - 720p

- **5** - 1080p

- **6** - 1440p

- **7** - 2160p


#### Types

This endpoint allows you to handle torrents, usenet and web downloads all in one. This is why the "type" parameter is available. It defaults to "torrent".

- **torrent** - Torrents

- **usenet** - Usenet downloads

- **webdownload** - Web Downloads


#### Important Notes

- Only text based subtitles are supported. If a non-text based subtitle is selected, it will be ignored.

- If a subtitle or audio index does not exist on the stream, it will be ignored.

- There are a lot of edge-case videos, if something doesn't work, don't hesitate to report the download hash and file_id of the failing video file.

- This is a **Pro** only feature.


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.create_stream_response import CreateStreamResponse
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
    api_instance = torbox.StreamApi(api_client)
    id = 56 # int | The ID of the type of download.
    file_id = 0 # int | The file ID inside of the download you would like to stream. (optional) (default to 0)
    type = 'torrent' # str | The type of download that this is. If choosing the incorrect one, the ID will be incorrect. (optional) (default to 'torrent')
    chosen_subtitle_index = 'chosen_subtitle_index_example' # str | The relative index of the subtitle you would like to stream. This is default null for none. 0 is the first subtitle found. (optional)
    chosen_audio_index = 0 # int | The relative index of the subtitle you would like to stream. Defaults to 0 for the first audio stream found inside the file. Cannot be null. (optional) (default to 0)
    chosen_resolution_index = 'chosen_resolution_index_example' # str | The index of the resolution you would like to stream. This is default null for original. (optional)
    scrobbling_enabled = True # bool |  (optional) (default to True)

    try:
        # Create Stream
        api_response = api_instance.create_stream(id, file_id=file_id, type=type, chosen_subtitle_index=chosen_subtitle_index, chosen_audio_index=chosen_audio_index, chosen_resolution_index=chosen_resolution_index, scrobbling_enabled=scrobbling_enabled)
        print("The response of StreamApi->create_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->create_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the type of download. | 
 **file_id** | **int**| The file ID inside of the download you would like to stream. | [optional] [default to 0]
 **type** | **str**| The type of download that this is. If choosing the incorrect one, the ID will be incorrect. | [optional] [default to &#39;torrent&#39;]
 **chosen_subtitle_index** | **str**| The relative index of the subtitle you would like to stream. This is default null for none. 0 is the first subtitle found. | [optional] 
 **chosen_audio_index** | **int**| The relative index of the subtitle you would like to stream. Defaults to 0 for the first audio stream found inside the file. Cannot be null. | [optional] [default to 0]
 **chosen_resolution_index** | **str**| The index of the resolution you would like to stream. This is default null for original. | [optional] 
 **scrobbling_enabled** | **bool**|  | [optional] [default to True]

### Return type

[**CreateStreamResponse**](CreateStreamResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_stream_data**
> GetStreamDataResponse get_stream_data(token, presigned_token, chosen_subtitle_index=chosen_subtitle_index, chosen_audio_index=chosen_audio_index, chosen_resolution_index=chosen_resolution_index)

Get Stream Data

### Overview

Gets stream data from an already created stream. Requires the presigned token and user API token from the original request.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example


```python
import torbox
from torbox.models.get_stream_data_response import GetStreamDataResponse
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
    api_instance = torbox.StreamApi(api_client)
    token = 'token_example' # str | The user's API token, can also be used from the original, /createstream request.
    presigned_token = 'presigned_token_example' # str | The presigned token given from the original, /createstream request.
    chosen_subtitle_index = 'chosen_subtitle_index_example' # str | The chosen subtitle index that you are requesting information about. (optional)
    chosen_audio_index = 0 # int | The chosen audio index that you are requesting information about. (optional) (default to 0)
    chosen_resolution_index = 'chosen_resolution_index_example' # str | The index of the resolution you would like to stream. This is default null for original. (optional)

    try:
        # Get Stream Data
        api_response = api_instance.get_stream_data(token, presigned_token, chosen_subtitle_index=chosen_subtitle_index, chosen_audio_index=chosen_audio_index, chosen_resolution_index=chosen_resolution_index)
        print("The response of StreamApi->get_stream_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->get_stream_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The user&#39;s API token, can also be used from the original, /createstream request. | 
 **presigned_token** | **str**| The presigned token given from the original, /createstream request. | 
 **chosen_subtitle_index** | **str**| The chosen subtitle index that you are requesting information about. | [optional] 
 **chosen_audio_index** | **int**| The chosen audio index that you are requesting information about. | [optional] [default to 0]
 **chosen_resolution_index** | **str**| The index of the resolution you would like to stream. This is default null for original. | [optional] 

### Return type

[**GetStreamDataResponse**](GetStreamDataResponse.md)

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

