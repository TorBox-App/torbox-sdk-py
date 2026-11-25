# torbox.AssistantApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_with_assistant**](AssistantApi.md#chat_with_assistant) | **POST** /v1/api/assistant/chat | Chat With Assistant
[**delete_assistant_conversation**](AssistantApi.md#delete_assistant_conversation) | **DELETE** /v1/api/assistant/conversations/{session_id} | Delete Assistant Conversation
[**delete_assistant_conversations**](AssistantApi.md#delete_assistant_conversations) | **DELETE** /v1/api/assistant/conversations | Delete All Assistant Conversations
[**get_assistant_usage**](AssistantApi.md#get_assistant_usage) | **GET** /v1/api/assistant/usage | Get Assistant Usage
[**list_assistant_conversations**](AssistantApi.md#list_assistant_conversations) | **GET** /v1/api/assistant/conversations | Get Assistant Conversations
[**read_assistant_conversation**](AssistantApi.md#read_assistant_conversation) | **GET** /v1/api/assistant/conversations/{session_id} | Get Assistant Conversation


# **chat_with_assistant**
> str chat_with_assistant(chat_request)

Chat With Assistant

### Overview

Send a message to the AI Assistant. Optionally include a `session_id` to resume a previous conversation. If no `session_id` is given, the AI will have no previous context and will create a new conversation.

Also included is a way to upload `files` in base64 allowing you to attach a file that the AI Assistant can use.

We also allow you to send `blocks` which is a list of strings that state what additional features your chat interface includes. If no `blocks` are sent, responses are sent in plain text and markdown (for things like tables or bolding text).

The answer is streamed as plain text while it is written. Send the header `Accept: text/event-stream` to get it as server-sent events instead: `tool` with the `name` of each tool the assistant uses, `text` with each piece of the answer, `support` with the `id` of the support conversation when the chat is handed to the support team, `usage` with the share of the day's allowance that is `used` and when it `resets_at`, `error` with the error if the answer fails, and `done` at the end.

```
event: tool
data: {"name": "get_torrent_list"}

event: text
data: {"text": "You have 2 torrents, "}

event: text
data: {"text": "and both have finished downloading."}

event: usage
data: {"used": 0.0123, "resets_at": "2026-01-01T00:00:00Z"}

event: done
data: {}
```

The `X-Session-ID` response header holds the `session_id` to send with the next message.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.chat_request import ChatRequest
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
    api_instance = torbox.AssistantApi(api_client)
    chat_request = {"message":"string","session_id":"string","files":[{"name":"string","data":"string"}],"blocks":["string"]} # ChatRequest | 

    try:
        # Chat With Assistant
        api_response = api_instance.chat_with_assistant(chat_request)
        print("The response of AssistantApi->chat_with_assistant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistantApi->chat_with_assistant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_request** | [**ChatRequest**](ChatRequest.md)|  | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

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

# **delete_assistant_conversation**
> DeleteAssistantConversationResponse delete_assistant_conversation(session_id)

Delete Assistant Conversation

### Overview

Deletes a specific conversation with the AI assistant. Usage persists from the conversation.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.delete_assistant_conversation_response import DeleteAssistantConversationResponse
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
    api_instance = torbox.AssistantApi(api_client)
    session_id = 'session_id_example' # str | The session you want to retrieve.

    try:
        # Delete Assistant Conversation
        api_response = api_instance.delete_assistant_conversation(session_id)
        print("The response of AssistantApi->delete_assistant_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistantApi->delete_assistant_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session you want to retrieve. | 

### Return type

[**DeleteAssistantConversationResponse**](DeleteAssistantConversationResponse.md)

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

# **delete_assistant_conversations**
> DeleteAssistantConversationsResponse delete_assistant_conversations()

Delete All Assistant Conversations

### Overview

Deletes all conversations for a user's account. Usage persists from the conversations.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.delete_assistant_conversations_response import DeleteAssistantConversationsResponse
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
    api_instance = torbox.AssistantApi(api_client)

    try:
        # Delete All Assistant Conversations
        api_response = api_instance.delete_assistant_conversations()
        print("The response of AssistantApi->delete_assistant_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistantApi->delete_assistant_conversations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeleteAssistantConversationsResponse**](DeleteAssistantConversationsResponse.md)

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

# **get_assistant_usage**
> GetAssistantUsageResponse get_assistant_usage()

Get Assistant Usage

### Overview

Gets the current user's AI assistant usage. Users are limited to a certain number of tokens daily, and this endpoint tells you exactly how much is left as a percentage. This makes it easy for developers so they don't have to spend time counting tokens, which is usually inaccurate.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_assistant_usage_response import GetAssistantUsageResponse
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
    api_instance = torbox.AssistantApi(api_client)

    try:
        # Get Assistant Usage
        api_response = api_instance.get_assistant_usage()
        print("The response of AssistantApi->get_assistant_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistantApi->get_assistant_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAssistantUsageResponse**](GetAssistantUsageResponse.md)

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

# **list_assistant_conversations**
> ListAssistantConversationsResponse list_assistant_conversations()

Get Assistant Conversations

### Overview

Gets the user's open conversations. Conversations are sorted newest first. Each conversation is kept for 30 days after its last message.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.list_assistant_conversations_response import ListAssistantConversationsResponse
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
    api_instance = torbox.AssistantApi(api_client)

    try:
        # Get Assistant Conversations
        api_response = api_instance.list_assistant_conversations()
        print("The response of AssistantApi->list_assistant_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistantApi->list_assistant_conversations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAssistantConversationsResponse**](ListAssistantConversationsResponse.md)

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

# **read_assistant_conversation**
> ReadAssistantConversationResponse read_assistant_conversation(session_id, since=since)

Get Assistant Conversation

### Overview

Get a specific user conversation with the AI assistant.

You can pass the `since` parameter with a Unix timestamp, and will show any revisions since that time, this way, you don't waste bandwidth retrieving and updating the entire conversation. If no update has been made since, the data return will be null.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.read_assistant_conversation_response import ReadAssistantConversationResponse
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
    api_instance = torbox.AssistantApi(api_client)
    session_id = 'session_id_example' # str | The session you want to retrieve.
    since = 56 # int | Unix timestamp of the conversation you want to get since this time. (optional)

    try:
        # Get Assistant Conversation
        api_response = api_instance.read_assistant_conversation(session_id, since=since)
        print("The response of AssistantApi->read_assistant_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistantApi->read_assistant_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session you want to retrieve. | 
 **since** | **int**| Unix timestamp of the conversation you want to get since this time. | [optional] 

### Return type

[**ReadAssistantConversationResponse**](ReadAssistantConversationResponse.md)

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

