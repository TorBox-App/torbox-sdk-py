# torbox.TagsApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**control_tag**](TagsApi.md#control_tag) | **POST** /v1/api/tags/controltag | Control Tag
[**edit_tag**](TagsApi.md#edit_tag) | **PUT** /v1/api/tags/edittag | Edit Tag
[**get_tags**](TagsApi.md#get_tags) | **GET** /v1/api/tags/mytags | Get User Tags


# **control_tag**
> ControlTagResponse control_tag(control_tag)

Control Tag

### Overview

Controls a tag. Currently, the only operation is "delete", which deletes the tag and removes it from every download using it; the downloads stay in your account and are otherwise unmodified. The ID is the tag's ID from `/mytags` endpoint.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.control_tag import ControlTag
from torbox.models.control_tag_response import ControlTagResponse
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
    api_instance = torbox.TagsApi(api_client)
    control_tag = {"id":0,"operation":"delete"} # ControlTag | 

    try:
        # Control Tag
        api_response = api_instance.control_tag(control_tag)
        print("The response of TagsApi->control_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->control_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_tag** | [**ControlTag**](ControlTag.md)|  | 

### Return type

[**ControlTagResponse**](ControlTagResponse.md)

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

# **edit_tag**
> EditTagResponse edit_tag(edit_tag)

Edit Tag

### Overview

Renames a tag. This new name is case sensitive. The ID is the tag's ID from the `/mytags`. Fails with `DUPLICATE_ITEM` when another of the user's tags already has the same name, in any casing.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.edit_tag import EditTag
from torbox.models.edit_tag_response import EditTagResponse
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
    api_instance = torbox.TagsApi(api_client)
    edit_tag = {"id":0,"new_name":"string"} # EditTag | 

    try:
        # Edit Tag
        api_response = api_instance.edit_tag(edit_tag)
        print("The response of TagsApi->edit_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->edit_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_tag** | [**EditTag**](EditTag.md)|  | 

### Return type

[**EditTagResponse**](EditTagResponse.md)

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

# **get_tags**
> GetTagsResponse get_tags()

Get User Tags

### Overview

Gets the tags attached to a user account, with the downloads using each tag, their count and total size.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_tags_response import GetTagsResponse
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
    api_instance = torbox.TagsApi(api_client)

    try:
        # Get User Tags
        api_response = api_instance.get_tags()
        print("The response of TagsApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTagsResponse**](GetTagsResponse.md)

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

