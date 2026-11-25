# torbox.IntegrationsApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_oauth**](IntegrationsApi.md#authenticate_oauth) | **GET** /v1/api/integration/oauth/{provider} | Authenticate OAuth
[**cancel_specific_job**](IntegrationsApi.md#cancel_specific_job) | **DELETE** /v1/api/integration/job/{job_id} | Cancel Specific Job
[**get_all_jobs**](IntegrationsApi.md#get_all_jobs) | **GET** /v1/api/integration/jobs | Get All Jobs
[**get_all_jobs_by_hash**](IntegrationsApi.md#get_all_jobs_by_hash) | **GET** /v1/api/integration/jobs/{hash} | Get All Jobs By Hash
[**get_oauth_integrations**](IntegrationsApi.md#get_oauth_integrations) | **GET** /v1/api/integration/oauth/me | Get OAuth Integrations
[**get_specific_job**](IntegrationsApi.md#get_specific_job) | **GET** /v1/api/integration/job/{job_id} | Get Specific Job
[**link_discord_roles**](IntegrationsApi.md#link_discord_roles) | **POST** /v1/api/integration/oauth/discord/linked_roles | Link Discord Roles
[**oauth_callback_get**](IntegrationsApi.md#oauth_callback_get) | **GET** /v1/api/integration/oauth/{provider}/callback | OAuth Callback Get
[**oauth_callback_post**](IntegrationsApi.md#oauth_callback_post) | **POST** /v1/api/integration/oauth/{provider}/callback | OAuth Callback Post
[**oauth_success**](IntegrationsApi.md#oauth_success) | **GET** /v1/api/integration/oauth/{provider}/success | OAuth Success
[**register_oauth_link**](IntegrationsApi.md#register_oauth_link) | **POST** /v1/api/integration/oauth/{provider}/register | Register OAuth Link
[**unregister_oauth_link**](IntegrationsApi.md#unregister_oauth_link) | **DELETE** /v1/api/integration/oauth/{provider}/unregister | Unregister OAuth Link
[**upload_to1fichier**](IntegrationsApi.md#upload_to1fichier) | **POST** /v1/api/integration/1fichier | Upload To 1Fichier
[**upload_to_dropbox**](IntegrationsApi.md#upload_to_dropbox) | **POST** /v1/api/integration/dropbox | Upload To Dropbox
[**upload_to_gofile**](IntegrationsApi.md#upload_to_gofile) | **POST** /v1/api/integration/gofile | Upload To Gofile
[**upload_to_google_drive**](IntegrationsApi.md#upload_to_google_drive) | **POST** /v1/api/integration/googledrive | Upload To Google Drive
[**upload_to_onedrive**](IntegrationsApi.md#upload_to_onedrive) | **POST** /v1/api/integration/onedrive | Upload To OneDrive
[**upload_to_pixeldrain**](IntegrationsApi.md#upload_to_pixeldrain) | **POST** /v1/api/integration/pixeldrain | Upload To Pixeldrain


# **authenticate_oauth**
> authenticate_oauth(provider)

Authenticate OAuth

### Overview

Starts the OAuth login with another service. This is a browser redirect, not a call for a script: open it in the user's browser. It answers with a redirect to the login page of the service named in `provider`. When the user has approved, the service sends the browser back to the callback route of this API, `https://api.torbox.app/v1/api/integration/oauth/{provider}/callback`, which finishes the login.

The accepted providers and where the browser is sent:

- `google` -> `https://accounts.google.com/o/oauth2/auth`, asking for the scopes `https://www.googleapis.com/auth/drive.file` and `https://www.googleapis.com/auth/userinfo.email`
- `dropbox` -> `https://www.dropbox.com/oauth2/authorize`, asking for `files.content.write sharing.write`
- `discord` -> `https://discord.com/api/oauth2/authorize`, asking for `identify role_connections.write`
- `onedrive` -> `https://login.microsoftonline.com/common/oauth2/v2.0/authorize`, asking for `files.readwrite.all`
- `patreon` -> `https://www.patreon.com/oauth2/authorize`, asking for `identity`
- `apple` -> the Apple sign-in page, asking for `openid email`. Apple is asked to send the result back as a form POST.
- `anilist` -> `https://anilist.co/api/v2/oauth/authorize`
- `mal` -> `https://myanimelist.net/v1/oauth2/authorize`, asking for `write:users`
- `trakt` -> `https://trakt.tv/oauth/authorize`
- `simkl` -> `https://simkl.com/oauth/authorize`

Any other provider is answered with a JSON error instead of a redirect.

### Authorization

None required.


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
    api_instance = torbox.IntegrationsApi(api_client)
    provider = 'provider_example' # str | The service to log in with. One of `google`, `dropbox`, `discord`, `onedrive`, `patreon`, `apple`, `anilist`, `mal`, `trakt` or `simkl`.

    try:
        # Authenticate OAuth
        api_instance.authenticate_oauth(provider)
    except Exception as e:
        print("Exception when calling IntegrationsApi->authenticate_oauth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The service to log in with. One of &#x60;google&#x60;, &#x60;dropbox&#x60;, &#x60;discord&#x60;, &#x60;onedrive&#x60;, &#x60;patreon&#x60;, &#x60;apple&#x60;, &#x60;anilist&#x60;, &#x60;mal&#x60;, &#x60;trakt&#x60; or &#x60;simkl&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Found |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_specific_job**
> CancelSpecificJobResponse cancel_specific_job(job_id)

Cancel Specific Job

### Overview

Cancels a job or deletes the job. Cancels while in progess (pending, uploading), or deletes the job any other time. It will delete it from the database completely.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.cancel_specific_job_response import CancelSpecificJobResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    job_id = 56 # int | 

    try:
        # Cancel Specific Job
        api_response = api_instance.cancel_specific_job(job_id)
        print("The response of IntegrationsApi->cancel_specific_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->cancel_specific_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**|  | 

### Return type

[**CancelSpecificJobResponse**](CancelSpecificJobResponse.md)

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

# **get_all_jobs**
> GetAllJobsResponse get_all_jobs()

Get All Jobs

### Overview

Gets all the jobs attached to a user account. This is good for an overall view of the jobs, such as on a dashboard, or something similar.

### Statuses

- "pending" -> Upload is still waiting in the queue. Waiting for spot to upload.
- "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues.
- "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated.

- "failed" -> The upload has failed. Check the Detail key for information.


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_all_jobs_response import GetAllJobsResponse
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
    api_instance = torbox.IntegrationsApi(api_client)

    try:
        # Get All Jobs
        api_response = api_instance.get_all_jobs()
        print("The response of IntegrationsApi->get_all_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_all_jobs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllJobsResponse**](GetAllJobsResponse.md)

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

# **get_all_jobs_by_hash**
> GetAllJobsByHashResponse get_all_jobs_by_hash(hash)

Get All Jobs By Hash

### Overview

Gets all jobs that match a specific hash. Good for checking on specific downloads such as a download page, that could contain a lot of jobs.

### Statuses

- "pending" -> Upload is still waiting in the queue. Waiting for spot to upload.
- "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues.
- "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated.
- "failed" -> The upload has failed. Check the Detail key for information.


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_all_jobs_by_hash_response import GetAllJobsByHashResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    hash = 'hash_example' # str | 

    try:
        # Get All Jobs By Hash
        api_response = api_instance.get_all_jobs_by_hash(hash)
        print("The response of IntegrationsApi->get_all_jobs_by_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_all_jobs_by_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  | 

### Return type

[**GetAllJobsByHashResponse**](GetAllJobsByHashResponse.md)

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

# **get_oauth_integrations**
> GetOauthIntegrationsResponse get_oauth_integrations()

Get OAuth Integrations

### Overview

Shows which tracking services are linked to your account through an OAuth link. `data` has one boolean for each of `trakt`, `mal`, `anilist` and `simkl`, true when a link for that service is stored on your account. A link is stored with Register OAuth Link and removed with Unregister OAuth Link.

Only these four services are reported. A link for any other provider that Register OAuth Link accepts, such as `discord`, is not part of the answer. The answer also does not say whether a stored token still works. If the lookup itself fails, `data` is an empty object under the same success message.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_oauth_integrations_response import GetOauthIntegrationsResponse
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
    api_instance = torbox.IntegrationsApi(api_client)

    try:
        # Get OAuth Integrations
        api_response = api_instance.get_oauth_integrations()
        print("The response of IntegrationsApi->get_oauth_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_oauth_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOauthIntegrationsResponse**](GetOauthIntegrationsResponse.md)

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

# **get_specific_job**
> GetSpecificJobResponse get_specific_job(job_id)

Get Specific Job

### Overview

Gets a specifc job using the Job's ID. To get the ID, you will have to Get All Jobs, and get the ID you want.

### Statuses

- "pending" -> Upload is still waiting in the queue. Waiting for spot to upload.
- "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues.
- "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated.
- "failed" -> The upload has failed. Check the Detail key for information.


### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_specific_job_response import GetSpecificJobResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    job_id = 56 # int | 

    try:
        # Get Specific Job
        api_response = api_instance.get_specific_job(job_id)
        print("The response of IntegrationsApi->get_specific_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_specific_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**|  | 

### Return type

[**GetSpecificJobResponse**](GetSpecificJobResponse.md)

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

# **link_discord_roles**
> LinkDiscordRolesResponse link_discord_roles(linked_roles_data)

Link Discord Roles

### Overview

Updates the Discord linked roles of a user from their TorBox account. Send a Discord OAuth access token of the user in `discord_token`. The token is issued by Discord, not by TorBox: it is the `token` handed over at the end of the login started by Authenticate OAuth with the provider `discord`, which asks Discord for the `identify` and `role_connections.write` scopes.

TorBox reads the Discord user behind the token and writes the TorBox role connection of that Discord user: the platform name "TorBox", that the user has signed up, the date the TorBox account was created, and the key of the account's plan: `essential_plan` for plan 1, `pro_plan` for plan 2 or `standard_plan` for plan 3.

Once Discord has accepted the update, the Discord user id is saved as the `discord_id` of your TorBox settings. The answer carries no data.

When Discord returns no user for the token, or does not accept the update, the answer is an error and the Discord user id is not saved.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.link_discord_roles_response import LinkDiscordRolesResponse
from torbox.models.linked_roles_data import LinkedRolesData
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
    api_instance = torbox.IntegrationsApi(api_client)
    linked_roles_data = {"discord_token":"string"} # LinkedRolesData | 

    try:
        # Link Discord Roles
        api_response = api_instance.link_discord_roles(linked_roles_data)
        print("The response of IntegrationsApi->link_discord_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->link_discord_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_roles_data** | [**LinkedRolesData**](LinkedRolesData.md)|  | 

### Return type

[**LinkDiscordRolesResponse**](LinkDiscordRolesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **oauth_callback_get**
> oauth_callback_get(provider)

OAuth Callback Get

### Overview

The address a service sends the user's browser back to after the login started by Authenticate OAuth. It is reached by the browser on its way back from the service, not called by you. The service adds its `code` and `state` to the query string.

TorBox exchanges the code for the service's tokens, looks up who the user is at that service, and redirects the browser to the TorBox website with the result in the query string:

`https://torbox.app/oauth/{provider}/success?token=...&expires_in=...&expires_at=...&user_id=...&id_token=...&nonce=...&refresh_token=...`

- `token` -> the access token the service issued
- `refresh_token` -> the refresh token the service issued
- `expires_in`, `expires_at` -> as found in the service's token answer
- `user_id` -> who the user is at the service. The email address for `google` and `apple`, the `email` field of the Discord user for `discord`, the user id for `patreon`, `anilist` and `mal`, the user name for `trakt` and `simkl`. Not set for `dropbox` and `onedrive`.
- `id_token` -> the ID token for `google` and `apple`, the Discord user id for `discord`. Not set for the other providers.
- `nonce` -> the name of the provider

A value the service did not give is sent as the text `None`.

This route stores nothing on a TorBox account. The tokens it hands over are the ones Register OAuth Link, Link Discord Roles and the upload routes take.

If the login was cancelled, has expired or fails, the route answers with a JSON error instead of a redirect.

### Authorization

None required.


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
    api_instance = torbox.IntegrationsApi(api_client)
    provider = 'provider_example' # str | The service the login was started with. One of `google`, `dropbox`, `discord`, `onedrive`, `patreon`, `apple`, `anilist`, `mal`, `trakt` or `simkl`.

    try:
        # OAuth Callback Get
        api_instance.oauth_callback_get(provider)
    except Exception as e:
        print("Exception when calling IntegrationsApi->oauth_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The service the login was started with. One of &#x60;google&#x60;, &#x60;dropbox&#x60;, &#x60;discord&#x60;, &#x60;onedrive&#x60;, &#x60;patreon&#x60;, &#x60;apple&#x60;, &#x60;anilist&#x60;, &#x60;mal&#x60;, &#x60;trakt&#x60; or &#x60;simkl&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Found |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_callback_post**
> oauth_callback_post(provider)

OAuth Callback Post

### Overview

The same callback as OAuth Callback Get, for a service that sends the browser back with a form POST instead of a GET. Apple does this: the login for `apple` asks for the result as a form POST, and this route reads the form fields `state` and `code` from it. It is reached by the browser on its way back from the service, not called by you.

TorBox exchanges the code for the service's tokens, looks up who the user is at that service, and redirects the browser to the TorBox website with the result in the query string:

`https://torbox.app/oauth/{provider}/success?token=...&expires_in=...&expires_at=...&user_id=...&id_token=...&nonce=...&refresh_token=...`

The query parameters are the ones described under OAuth Callback Get. For `apple`, `user_id` is the email address from Apple's ID token and `id_token` is that ID token. A value the service did not give is sent as the text `None`.

This route stores nothing on a TorBox account. If the login was cancelled, has expired or fails, the route answers with a JSON error instead of a redirect.

### Authorization

None required.


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
    api_instance = torbox.IntegrationsApi(api_client)
    provider = 'provider_example' # str | The service the login was started with. One of `google`, `dropbox`, `discord`, `onedrive`, `patreon`, `apple`, `anilist`, `mal`, `trakt` or `simkl`.

    try:
        # OAuth Callback Post
        api_instance.oauth_callback_post(provider)
    except Exception as e:
        print("Exception when calling IntegrationsApi->oauth_callback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The service the login was started with. One of &#x60;google&#x60;, &#x60;dropbox&#x60;, &#x60;discord&#x60;, &#x60;onedrive&#x60;, &#x60;patreon&#x60;, &#x60;apple&#x60;, &#x60;anilist&#x60;, &#x60;mal&#x60;, &#x60;trakt&#x60; or &#x60;simkl&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Found |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_success**
> OauthSuccessResponse oauth_success(provider)

OAuth Success

### Overview

Answers with a fixed success message for the providers `google`, `dropbox`, `discord`, `onedrive` and `patreon`. It reads nothing but the provider name and hands over no token: `data` is always null. Any other provider is answered with a JSON error.

This is not where the OAuth callback redirects to. The callback sends the browser to the page with the same path on the TorBox website, `https://torbox.app/oauth/{provider}/success`, with the tokens in the query string. This route on the API takes no part in handing them over.

### Authorization

None required.


### Example


```python
import torbox
from torbox.models.oauth_success_response import OauthSuccessResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    provider = 'provider_example' # str | The service. One of `google`, `dropbox`, `discord`, `onedrive` or `patreon`.

    try:
        # OAuth Success
        api_response = api_instance.oauth_success(provider)
        print("The response of IntegrationsApi->oauth_success:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->oauth_success: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The service. One of &#x60;google&#x60;, &#x60;dropbox&#x60;, &#x60;discord&#x60;, &#x60;onedrive&#x60; or &#x60;patreon&#x60;. | 

### Return type

[**OauthSuccessResponse**](OauthSuccessResponse.md)

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

# **register_oauth_link**
> RegisterOauthLinkResponse register_oauth_link(provider, o_auth_register_request)

Register OAuth Link

### Overview

Stores an OAuth link to another service on your TorBox account. Send the access token and the refresh token that the service issued for the user. TorBox does not issue these tokens: they are the `token` and `refresh_token` handed over at the end of the login started by Authenticate OAuth.

Both tokens are stored encrypted. If the account already has a link for that provider, its tokens are replaced and the link is marked active again. The tokens are not checked with the service when they are registered. The stored tokens of `mal`, `trakt`, `anilist` and `discord` links are refreshed once a day with the refresh token.

Get OAuth Integrations shows whether a `trakt`, `mal`, `anilist` or `simkl` link is stored.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.o_auth_register_request import OAuthRegisterRequest
from torbox.models.register_oauth_link_response import RegisterOauthLinkResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    provider = 'provider_example' # str | The service to link. One of `google`, `dropbox`, `discord`, `onedrive`, `patreon`, `apple`, `anilist`, `mal`, `trakt` or `simkl`.
    o_auth_register_request = {"token":"string","refresh_token":"string"} # OAuthRegisterRequest | 

    try:
        # Register OAuth Link
        api_response = api_instance.register_oauth_link(provider, o_auth_register_request)
        print("The response of IntegrationsApi->register_oauth_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->register_oauth_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The service to link. One of &#x60;google&#x60;, &#x60;dropbox&#x60;, &#x60;discord&#x60;, &#x60;onedrive&#x60;, &#x60;patreon&#x60;, &#x60;apple&#x60;, &#x60;anilist&#x60;, &#x60;mal&#x60;, &#x60;trakt&#x60; or &#x60;simkl&#x60;. | 
 **o_auth_register_request** | [**OAuthRegisterRequest**](OAuthRegisterRequest.md)|  | 

### Return type

[**RegisterOauthLinkResponse**](RegisterOauthLinkResponse.md)

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

# **unregister_oauth_link**
> UnregisterOauthLinkResponse unregister_oauth_link(provider)

Unregister OAuth Link

### Overview

Removes the OAuth link to a service from your TorBox account by deleting the stored tokens. The tokens are deleted from TorBox only, nothing is revoked at the service itself.

The route answers with success whether or not a link existed. It does not check the provider name either: a name that was never registered removes nothing and is still answered with success.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.unregister_oauth_link_response import UnregisterOauthLinkResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    provider = 'provider_example' # str | The service to unlink, by the name it was registered with in Register OAuth Link (`google`, `dropbox`, `discord`, `onedrive`, `patreon`, `apple`, `anilist`, `mal`, `trakt` or `simkl`). The name is not checked by the route.

    try:
        # Unregister OAuth Link
        api_response = api_instance.unregister_oauth_link(provider)
        print("The response of IntegrationsApi->unregister_oauth_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->unregister_oauth_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The service to unlink, by the name it was registered with in Register OAuth Link (&#x60;google&#x60;, &#x60;dropbox&#x60;, &#x60;discord&#x60;, &#x60;onedrive&#x60;, &#x60;patreon&#x60;, &#x60;apple&#x60;, &#x60;anilist&#x60;, &#x60;mal&#x60;, &#x60;trakt&#x60; or &#x60;simkl&#x60;). The name is not checked by the route. | 

### Return type

[**UnregisterOauthLinkResponse**](UnregisterOauthLinkResponse.md)

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

# **upload_to1fichier**
> UploadTo1fichierResponse upload_to1fichier(add_to1_fichier)

Upload To 1Fichier

### Overview

Uploads a file, or a zip of a whole download, from your TorBox account to 1Fichier. Send the `id` of the torrent, usenet download or web download, its `type`, and either the `file_id` of one file or `zip` set to true. `onefichier_token` is optional: with it the upload is made with that 1Fichier account's API token, without it the upload is sent without a 1Fichier login.

The route answers at once with a `job_id`. The upload itself runs in the background as a transfer job, and nothing is checked with 1Fichier before the answer, so a token 1Fichier does not accept only shows up as a failed job. Follow the job with Get Specific Job (`/v1/api/integration/job/{job_id}`), Get All Jobs (`/v1/api/integration/jobs`) or Get All Jobs By Hash (`/v1/api/integration/jobs/{hash}`), and stop it with Cancel Specific Job.

The job goes from "pending" through "preparing" and "uploading" to "completed" or "failed". Its `detail` says what it is doing or why it failed, and its `progress` runs from 0 to 1. When it is completed, its `download_url` is the 1Fichier download link of the file and you get an "Upload Complete" notification. A failed job is deleted about an hour after it failed, a completed job about 7 days after it completed.

A file larger than 2 GB (2,147,483,647 bytes) is not uploaded: the request is queued and the job fails. The download has to be cached on TorBox, otherwise the job fails. If you send neither `file_id` nor `zip`, the request is still queued, but there is no file to upload and the job fails. If your settings have a `onefichier_folder_id`, the file is put in that folder, but only when a `onefichier_token` is sent.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.add_to1_fichier import AddTo1Fichier
from torbox.models.upload_to1fichier_response import UploadTo1fichierResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    add_to1_fichier = {"id":0,"file_id":0,"zip":false,"type":"torrent","onefichier_token":"string"} # AddTo1Fichier | 

    try:
        # Upload To 1Fichier
        api_response = api_instance.upload_to1fichier(add_to1_fichier)
        print("The response of IntegrationsApi->upload_to1fichier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->upload_to1fichier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to1_fichier** | [**AddTo1Fichier**](AddTo1Fichier.md)|  | 

### Return type

[**UploadTo1fichierResponse**](UploadTo1fichierResponse.md)

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

# **upload_to_dropbox**
> upload_to_dropbox(add_to_dropbox)

Upload To Dropbox

### Overview

The Dropbox integration has been removed from TorBox. The route still exists, but it no longer uploads anything and never starts a transfer job. After the API key and the `type` are checked, every request is answered with status 400, the error `DIFF_ISSUE` and the detail "Dropbox integration has been removed from TorBox."

The body fields are still read, so they are listed here, but none of them changes the answer. Use one of the other upload routes instead.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.add_to_dropbox import AddToDropbox
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
    api_instance = torbox.IntegrationsApi(api_client)
    add_to_dropbox = {"id":0,"file_id":0,"zip":false,"type":"torrent","dropbox_token":"string"} # AddToDropbox | 

    try:
        # Upload To Dropbox
        api_instance.upload_to_dropbox(add_to_dropbox)
    except Exception as e:
        print("Exception when calling IntegrationsApi->upload_to_dropbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to_dropbox** | [**AddToDropbox**](AddToDropbox.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_to_gofile**
> UploadToGofileResponse upload_to_gofile(add_to_gofile)

Upload To Gofile

### Overview

Uploads a file, or a zip of a whole download, from your TorBox account to Gofile. Send the `id` of the torrent, usenet download or web download, its `type`, and either the `file_id` of one file or `zip` set to true. `gofile_token` is optional: with it the upload is made with that Gofile account's API token, without it the upload is sent without a Gofile login.

The route answers at once with a `job_id`. The upload itself runs in the background as a transfer job, and nothing is checked with Gofile before the answer, so a token Gofile does not accept only shows up as a failed job. Follow the job with Get Specific Job (`/v1/api/integration/job/{job_id}`), Get All Jobs (`/v1/api/integration/jobs`) or Get All Jobs By Hash (`/v1/api/integration/jobs/{hash}`), and stop it with Cancel Specific Job.

The job goes from "pending" through "preparing" and "uploading" to "completed" or "failed". Its `detail` says what it is doing or why it failed, and its `progress` runs from 0 to 1. When it is completed, its `download_url` is the Gofile download page of the file and you get an "Upload Complete" notification. A failed job is deleted about an hour after it failed, a completed job about 7 days after it completed.

The download has to be cached on TorBox, otherwise the job fails. If you send neither `file_id` nor `zip`, the request is still queued, but there is no file to upload and the job fails. If your settings have a `gofile_folder_id`, the file is put in that folder, but only when a `gofile_token` is sent.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.add_to_gofile import AddToGofile
from torbox.models.upload_to_gofile_response import UploadToGofileResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    add_to_gofile = {"id":0,"file_id":0,"zip":false,"type":"torrent","gofile_token":"string"} # AddToGofile | 

    try:
        # Upload To Gofile
        api_response = api_instance.upload_to_gofile(add_to_gofile)
        print("The response of IntegrationsApi->upload_to_gofile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->upload_to_gofile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to_gofile** | [**AddToGofile**](AddToGofile.md)|  | 

### Return type

[**UploadToGofileResponse**](UploadToGofileResponse.md)

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

# **upload_to_google_drive**
> UploadToGoogleDriveResponse upload_to_google_drive(add_to_google_drive)

Upload To Google Drive

### Overview

Uploads a file, or a zip of a whole download, from your TorBox account to a Google Drive. Send the `id` of the torrent, usenet download or web download, its `type`, and either the `file_id` of one file or `zip` set to true. In `google_token` you send a Google OAuth access token for the Drive to upload to. The login started by Authenticate OAuth with the provider `google` asks Google for the `drive.file` scope and ends with such a token.

The route answers at once with a `job_id`. The upload itself runs in the background as a transfer job, and nothing is checked with Google before the answer, so a token Google does not accept only shows up as a failed job. Follow the job with Get Specific Job (`/v1/api/integration/job/{job_id}`), Get All Jobs (`/v1/api/integration/jobs`) or Get All Jobs By Hash (`/v1/api/integration/jobs/{hash}`), and stop it with Cancel Specific Job.

The job goes from "pending" through "preparing" and "uploading" to "completed" or "failed". Its `detail` says what it is doing or why it failed, and its `progress` runs from 0 to 1. When it is completed, its `download_url` is the link to the file on Google Drive and you get an "Upload Complete" notification. A failed job is deleted about an hour after it failed, a completed job about 7 days after it completed.

The download has to be cached on TorBox, otherwise the job fails. If you send neither `file_id` nor `zip`, the request is still queued, but there is no file to upload and the job fails. If your settings have a `google_drive_folder_id`, the file is put in that folder.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.add_to_google_drive import AddToGoogleDrive
from torbox.models.upload_to_google_drive_response import UploadToGoogleDriveResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    add_to_google_drive = {"id":0,"file_id":0,"zip":false,"type":"torrent","google_token":"string"} # AddToGoogleDrive | 

    try:
        # Upload To Google Drive
        api_response = api_instance.upload_to_google_drive(add_to_google_drive)
        print("The response of IntegrationsApi->upload_to_google_drive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->upload_to_google_drive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to_google_drive** | [**AddToGoogleDrive**](AddToGoogleDrive.md)|  | 

### Return type

[**UploadToGoogleDriveResponse**](UploadToGoogleDriveResponse.md)

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

# **upload_to_onedrive**
> UploadToOnedriveResponse upload_to_onedrive(add_to_onedrive)

Upload To OneDrive

### Overview

Uploads a file, or a zip of a whole download, from your TorBox account to a OneDrive. Send the `id` of the torrent, usenet download or web download, its `type`, and either the `file_id` of one file or `zip` set to true. In `onedrive_token` you send a OneDrive (Microsoft) OAuth access token for the drive to upload to. The login started by Authenticate OAuth with the provider `onedrive` asks Microsoft for the `files.readwrite.all` scope and ends with such a token.

The route answers at once with a `job_id`. The upload itself runs in the background as a transfer job, and nothing is checked with OneDrive before the answer, so a token OneDrive does not accept only shows up as a failed job. Follow the job with Get Specific Job (`/v1/api/integration/job/{job_id}`), Get All Jobs (`/v1/api/integration/jobs`) or Get All Jobs By Hash (`/v1/api/integration/jobs/{hash}`), and stop it with Cancel Specific Job.

The job goes from "pending" through "preparing" and "uploading" to "completed" or "failed". Its `detail` says what it is doing or why it failed, and its `progress` runs from 0 to 1. When it is completed, its `download_url` is the link to the file on OneDrive and you get an "Upload Complete" notification. A failed job is deleted about an hour after it failed, a completed job about 7 days after it completed.

The download has to be cached on TorBox, otherwise the job fails. If you send neither `file_id` nor `zip`, the request is still queued, but there is no file to upload and the job fails. The file is saved under the `onedrive_save_path` of your settings, or in the root of the drive when that setting is empty. A file with the same name in that place is replaced.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.add_to_onedrive import AddToOnedrive
from torbox.models.upload_to_onedrive_response import UploadToOnedriveResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    add_to_onedrive = {"id":0,"file_id":0,"zip":false,"type":"torrent","onedrive_token":"string"} # AddToOnedrive | 

    try:
        # Upload To OneDrive
        api_response = api_instance.upload_to_onedrive(add_to_onedrive)
        print("The response of IntegrationsApi->upload_to_onedrive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->upload_to_onedrive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to_onedrive** | [**AddToOnedrive**](AddToOnedrive.md)|  | 

### Return type

[**UploadToOnedriveResponse**](UploadToOnedriveResponse.md)

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

# **upload_to_pixeldrain**
> UploadToPixeldrainResponse upload_to_pixeldrain(add_to_pixeldrain)

Upload To Pixeldrain

### Overview

Uploads a file, or a zip of a whole download, from your TorBox account to Pixeldrain. Send the `id` of the torrent, usenet download or web download, its `type`, either the `file_id` of one file or `zip` set to true, and the API key of the Pixeldrain account to upload to in `pixeldrain_token`.

The route accepts a request without `pixeldrain_token`, but nothing can be uploaded without one: the job then fails with the detail "No API key provided. Please provide an API key to upload to Pixeldrain." Only the key sent in the request is used.

The route answers at once with a `job_id`. The upload itself runs in the background as a transfer job, and nothing is checked with Pixeldrain before the answer, so a key Pixeldrain does not accept only shows up as a failed job. Follow the job with Get Specific Job (`/v1/api/integration/job/{job_id}`), Get All Jobs (`/v1/api/integration/jobs`) or Get All Jobs By Hash (`/v1/api/integration/jobs/{hash}`), and stop it with Cancel Specific Job.

The job goes from "pending" through "preparing" and "uploading" to "completed" or "failed". Its `detail` says what it is doing or why it failed, and its `progress` runs from 0 to 1. When it is completed, its `download_url` is the Pixeldrain link of the file (`https://pixeldrain.com/u/...`) and you get an "Upload Complete" notification. A failed job is deleted about an hour after it failed, a completed job about 7 days after it completed.

A file of 100 GB (107,374,182,400 bytes) or more is not uploaded: the request is queued and the job fails. The download has to be cached on TorBox, otherwise the job fails. Send `file_id` or `zip`: with neither there is no file to upload and the job never completes.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.add_to_pixeldrain import AddToPixeldrain
from torbox.models.upload_to_pixeldrain_response import UploadToPixeldrainResponse
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
    api_instance = torbox.IntegrationsApi(api_client)
    add_to_pixeldrain = {"id":0,"file_id":0,"zip":false,"type":"torrent","pixeldrain_token":"string"} # AddToPixeldrain | 

    try:
        # Upload To Pixeldrain
        api_response = api_instance.upload_to_pixeldrain(add_to_pixeldrain)
        print("The response of IntegrationsApi->upload_to_pixeldrain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->upload_to_pixeldrain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to_pixeldrain** | [**AddToPixeldrain**](AddToPixeldrain.md)|  | 

### Return type

[**UploadToPixeldrainResponse**](UploadToPixeldrainResponse.md)

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

