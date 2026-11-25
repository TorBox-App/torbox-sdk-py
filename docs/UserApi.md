# torbox.UserApi

All URIs are relative to *https://api.torbox.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_referral_to_account**](UserApi.md#add_referral_to_account) | **POST** /v1/api/user/addreferral | Add Referral To Account
[**delete_account**](UserApi.md#delete_account) | **DELETE** /v1/api/user/deleteme | Delete Account
[**edit_user_settings**](UserApi.md#edit_user_settings) | **PUT** /v1/api/user/settings/editsettings | Edit User Settings
[**get_confirmation_code**](UserApi.md#get_confirmation_code) | **GET** /v1/api/user/getconfirmation | Get Confirmation Code
[**get_referral_data**](UserApi.md#get_referral_data) | **GET** /v1/api/user/referraldata | Get Referral Data
[**get_subscriptions**](UserApi.md#get_subscriptions) | **GET** /v1/api/user/subscriptions | Get Subscriptions
[**get_token_from_device_code_process**](UserApi.md#get_token_from_device_code_process) | **POST** /v1/api/user/auth/device/token | Get Token From Device Code Process
[**get_transaction_pdf**](UserApi.md#get_transaction_pdf) | **GET** /v1/api/user/transaction/pdf | Get Transaction PDF
[**get_transactions**](UserApi.md#get_transactions) | **GET** /v1/api/user/transactions | Get Transactions
[**get_user_data**](UserApi.md#get_user_data) | **GET** /v1/api/user/me | Get User Data
[**get_user_stats**](UserApi.md#get_user_stats) | **GET** /v1/api/user/stats | Get User Stats
[**refresh_api_token**](UserApi.md#refresh_api_token) | **POST** /v1/api/user/refreshtoken | Refresh API Token
[**start_device_code_authorization_process**](UserApi.md#start_device_code_authorization_process) | **GET** /v1/api/user/auth/device/start | Start Device Code Authorization Process


# **add_referral_to_account**
> AddReferralToAccountResponse add_referral_to_account(referral)

Add Referral To Account

### Overview

Automatically adds a referral code to the user's account. This can be used for developers to automatically add their referral to user's accounts who use their service.

This will not override any referral a user already has. If they already have one, then it cannot be changed using this endpoint. It can only be done by the user on the [website](https://torbox.app/subscription).

### Authorization

Requires an API key using the Authorization Bearer Header. Use the user's API key, not your own.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.add_referral_to_account_response import AddReferralToAccountResponse
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
    api_instance = torbox.UserApi(api_client)
    referral = 'referral_example' # str | A referral code. Must be UUID.

    try:
        # Add Referral To Account
        api_response = api_instance.add_referral_to_account(referral)
        print("The response of UserApi->add_referral_to_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->add_referral_to_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referral** | **str**| A referral code. Must be UUID. | 

### Return type

[**AddReferralToAccountResponse**](AddReferralToAccountResponse.md)

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

# **delete_account**
> DeleteAccountResponse delete_account(delete_account_schema)

Delete Account

### Overview

Permanently deletes the user's TorBox account. This cannot be undone.

Because of how dangerous this action is, it needs two things on top of the API key: the user's session token from the website, and a confirmation code, which is sent to the user's email by the Get Confirmation Code endpoint.

### Authorization

Requires an API key using the Authorization Bearer Header, as well as the session token and the confirmation code in the body.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.delete_account_response import DeleteAccountResponse
from torbox.models.delete_account_schema import DeleteAccountSchema
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
    api_instance = torbox.UserApi(api_client)
    delete_account_schema = {"session_token":"string","confirmation_code":123456} # DeleteAccountSchema | 

    try:
        # Delete Account
        api_response = api_instance.delete_account(delete_account_schema)
        print("The response of UserApi->delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_account_schema** | [**DeleteAccountSchema**](DeleteAccountSchema.md)|  | 

### Return type

[**DeleteAccountResponse**](DeleteAccountResponse.md)

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
**410** | Gone |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user_settings**
> EditUserSettingsResponse edit_user_settings(base_settings_model)

Edit User Settings

### Overview

Edits a user's TorBox settings. These values take effect immediately. Please view the body to read about allowed options and parameters.

To get the user settings, simply use the "[Get User Data](https://api.torbox.app/docs#/User/get_user_data)" endpoint, while sending the "?settings=true" parameter

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.base_settings_model import BaseSettingsModel
from torbox.models.edit_user_settings_response import EditUserSettingsResponse
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
    api_instance = torbox.UserApi(api_client)
    base_settings_model = {"email_notifications":true,"web_notifications":true,"mobile_notifications":true,"rss_notifications":true,"download_speed_in_tab":true,"stremio_quality":[0,1,2,3,4,5,6,7,8,9,10,11],"stremio_resolution":[0,1,2,3],"stremio_language":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],"stremio_cache":[1,2,3],"stremio_size_lower":0,"google_drive_folder_id":"string","onedrive_save_path":"string","discord_id":"string","discord_notifications":true,"stremio_allow_adult":true,"stremio_seed_torrents":1,"seed_torrents":1,"allow_zipped":true,"stremio_allow_zipped":true,"onefichier_folder_id":"string","gofile_folder_id":"string","webhook_notifications":true,"webhook_url":"https://example.com/webhook","telegram_notifications":true,"telegram_id":"string","mega_email":"string","mega_password":"string","stremio_sort":"seeders","cdn_selection":"string","stremio_use_custom_search_engines":true,"stremio_result_sort":"torrent","webdav_use_local_files":true,"stremio_legacy_your_media":true,"stremio_only_your_media_streams":true,"stremio_disable_your_media_streams":true,"webdav_use_folder_view":true,"webdav_flatten":true,"stremio_limit_per_resolution_torrent":0,"stremio_limit_per_resolution_usenet":0,"stremio_size_upper":0,"stremio_torrent_seeders_cutoff":0,"pixeldrain_api_key":"string","onefichier_api_key":"string","gofile_api_key":"string","patreon_id":"string","stremio_wait_for_download_usenet":true,"stremio_wait_for_download_torrent":true,"stremio_disable_filtered_note":true,"stremio_emoji_in_description":true,"dashboard_filter":{"torrents":false,"usenet_downloads":false,"web_downloads":false,"active":false,"inactive":false,"queued":false,"downloading":false,"uploading":false,"processing":false,"download_ready":false,"cached":false,"uncached":false,"private":false,"borrowed":false},"web_player_always_transcode":true,"web_player_always_skip_intro":true,"web_player_audio_preferred_language":"string","web_player_subtitle_preferred_language":"string","web_player_disable_prestream_selector":true,"dashboard_sort":"default","web_player_disable_next_up_dialogue":true,"web_player_enable_scrobbling":true,"append_filename_to_links":true} # BaseSettingsModel | 

    try:
        # Edit User Settings
        api_response = api_instance.edit_user_settings(base_settings_model)
        print("The response of UserApi->edit_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->edit_user_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_settings_model** | [**BaseSettingsModel**](BaseSettingsModel.md)|  | 

### Return type

[**EditUserSettingsResponse**](EditUserSettingsResponse.md)

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

# **get_confirmation_code**
> GetConfirmationCodeResponse get_confirmation_code()

Get Confirmation Code

### Overview

Requests a 6 digit code to be sent to the user's email for verification. Used to verify a user actually wants to perform a potentially dangerous action.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_confirmation_code_response import GetConfirmationCodeResponse
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
    api_instance = torbox.UserApi(api_client)

    try:
        # Get Confirmation Code
        api_response = api_instance.get_confirmation_code()
        print("The response of UserApi->get_confirmation_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_confirmation_code: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetConfirmationCodeResponse**](GetConfirmationCodeResponse.md)

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

# **get_referral_data**
> GetReferralDataResponse get_referral_data()

Get Referral Data

### Overview

Use this endpoint to get the user's referral data. This includes information such as how many referrals they have made, and their referral code.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_referral_data_response import GetReferralDataResponse
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
    api_instance = torbox.UserApi(api_client)

    try:
        # Get Referral Data
        api_response = api_instance.get_referral_data()
        print("The response of UserApi->get_referral_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_referral_data: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetReferralDataResponse**](GetReferralDataResponse.md)

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

# **get_subscriptions**
> GetSubscriptionsResponse get_subscriptions()

Get Subscriptions

### Overview

Gets a users subscriptions. This includes active and inactive subscriptions for all payment processors.

It should be noted that "plan_code" is not normalized to the standard plan codes such as 1, 2, or 3. These "plan_code"s are payment processor specific and used internally. If you want to display these subscriptions, use the "plan_name".

For displaying information to users, use the "status", "gateway", and "plan_name". No other information is relevant to the user, and the rest is used for TorBox internally.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_subscriptions_response import GetSubscriptionsResponse
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
    api_instance = torbox.UserApi(api_client)

    try:
        # Get Subscriptions
        api_response = api_instance.get_subscriptions()
        print("The response of UserApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_subscriptions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSubscriptionsResponse**](GetSubscriptionsResponse.md)

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

# **get_token_from_device_code_process**
> GetTokenFromDeviceCodeProcessResponse get_token_from_device_code_process(device_token_schema)

Get Token From Device Code Process

### Overview

Gets the user's API token from the device code authorization process. This endpoint is expected to be polled in interval until it returns success, or until the expiry has passed. All data you need for this request is in the [original request](https://api.torbox.app/docs#/User/start_device_code_authorization_process), which includes the interval to be polled by, the expiry time to stop at, and `device_code` to be sent to the API to get the correct data.

### Authorization

None required.


### Example


```python
import torbox
from torbox.models.device_token_schema import DeviceTokenSchema
from torbox.models.get_token_from_device_code_process_response import GetTokenFromDeviceCodeProcessResponse
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
    api_instance = torbox.UserApi(api_client)
    device_token_schema = {"device_code":"XXXXXXXXXXXXXXXXXXXXXXXXX"} # DeviceTokenSchema | 

    try:
        # Get Token From Device Code Process
        api_response = api_instance.get_token_from_device_code_process(device_token_schema)
        print("The response of UserApi->get_token_from_device_code_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_token_from_device_code_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_token_schema** | [**DeviceTokenSchema**](DeviceTokenSchema.md)|  | 

### Return type

[**GetTokenFromDeviceCodeProcessResponse**](GetTokenFromDeviceCodeProcessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **get_transaction_pdf**
> str get_transaction_pdf(transaction_id)

Get Transaction PDF

### Overview

Generates a PDF of the transaction information. Requires the transaction ID from the "Get Transactions" request.

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
    api_instance = torbox.UserApi(api_client)
    transaction_id = 'transaction_id_example' # str | The transaction ID that you want to generate the PDF for.

    try:
        # Get Transaction PDF
        api_response = api_instance.get_transaction_pdf(transaction_id)
        print("The response of UserApi->get_transaction_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_transaction_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction ID that you want to generate the PDF for. | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

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

# **get_transactions**
> GetTransactionsResponse get_transactions()

Get Transactions

### Overview

Use this endpoint to get the user's list of transactions. This data isn't exactly relevant to a third party developer, unless you want to build full parity with TorBox's dashboard, or simply want to show this information.

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_transactions_response import GetTransactionsResponse
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
    api_instance = torbox.UserApi(api_client)

    try:
        # Get Transactions
        api_response = api_instance.get_transactions()
        print("The response of UserApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_transactions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTransactionsResponse**](GetTransactionsResponse.md)

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

# **get_user_data**
> GetUserDataResponse get_user_data(settings=settings, download_stats=download_stats, referral=referral)

Get User Data

### Overview

Gets a users account data and information.

### Plans

`0` is Free plan

`1` is Essential plan (_$3 plan_)

`2` is Pro plan (_$10 plan_)

`3` is Standard plan (_$5 plan_)

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_user_data_response import GetUserDataResponse
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
    api_instance = torbox.UserApi(api_client)
    settings = False # bool | Allows you to retrieve user settings. (optional) (default to False)
    download_stats = False # bool |  (optional) (default to False)
    referral = False # bool |  (optional) (default to False)

    try:
        # Get User Data
        api_response = api_instance.get_user_data(settings=settings, download_stats=download_stats, referral=referral)
        print("The response of UserApi->get_user_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | **bool**| Allows you to retrieve user settings. | [optional] [default to False]
 **download_stats** | **bool**|  | [optional] [default to False]
 **referral** | **bool**|  | [optional] [default to False]

### Return type

[**GetUserDataResponse**](GetUserDataResponse.md)

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

# **get_user_stats**
> GetUserStatsResponse get_user_stats(general=general, bandwidth=bandwidth, bandwidth_grouping=bandwidth_grouping)

Get User Stats

### Overview

Gets a users stats. This data is currently split into two sections, "general" and "bandwidth". General shows general data, such as "Total Data Downloaded", "Total Data Egress", "Overall Ratio", and "Total Downloaded". Bandwidth shows the amount of bandwidth a user has downloaded within the past 30 days. We don't store this data for longer than 30 days, and it can be made more or less granular. Makes cool graphs!

### Authorization

Requires an API key using the Authorization Bearer Header.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.get_user_stats_response import GetUserStatsResponse
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
    api_instance = torbox.UserApi(api_client)
    general = True # bool | Retrieve general stats. (optional) (default to True)
    bandwidth = False # bool | Retrieve bandwidth stats. (optional) (default to False)
    bandwidth_grouping = 'day' # str | If the \"bandwidth\" query parameter is sent, this value is used. Allowed is \"hour\", \"day\", \"week\", and \"month\", this narrates how bandwidth is grouped. More granular shows more information. (optional) (default to 'day')

    try:
        # Get User Stats
        api_response = api_instance.get_user_stats(general=general, bandwidth=bandwidth, bandwidth_grouping=bandwidth_grouping)
        print("The response of UserApi->get_user_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **general** | **bool**| Retrieve general stats. | [optional] [default to True]
 **bandwidth** | **bool**| Retrieve bandwidth stats. | [optional] [default to False]
 **bandwidth_grouping** | **str**| If the \&quot;bandwidth\&quot; query parameter is sent, this value is used. Allowed is \&quot;hour\&quot;, \&quot;day\&quot;, \&quot;week\&quot;, and \&quot;month\&quot;, this narrates how bandwidth is grouped. More granular shows more information. | [optional] [default to &#39;day&#39;]

### Return type

[**GetUserStatsResponse**](GetUserStatsResponse.md)

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

# **refresh_api_token**
> RefreshApiTokenResponse refresh_api_token(refresh_token_schema)

Refresh API Token

### Overview

If you want a new API token, or your old one has been compromised, you may request a new one. If you happen to forget the token, go the [TorBox settings page ](https://torbox.app/settings) and copy the current one. If this still doesn't work, you may contact us at our support email for a new one.

### Authorization

Requires an API key using the Authorization Bearer Header as well as passing the `session_token` from the website to be passed in the body. You can find the `session_token` in the localStorage of your browser on any TorBox.app page under the key `torbox_session_token`. This is a temporary token that only lasts for 1 hour, which is why it is used here to verify the identity of a user as well as their API token.


### Example

* Bearer Authentication (ApiKey):

```python
import torbox
from torbox.models.refresh_api_token_response import RefreshApiTokenResponse
from torbox.models.refresh_token_schema import RefreshTokenSchema
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
    api_instance = torbox.UserApi(api_client)
    refresh_token_schema = {"session_token":"string"} # RefreshTokenSchema | 

    try:
        # Refresh API Token
        api_response = api_instance.refresh_api_token(refresh_token_schema)
        print("The response of UserApi->refresh_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->refresh_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_schema** | [**RefreshTokenSchema**](RefreshTokenSchema.md)|  | 

### Return type

[**RefreshApiTokenResponse**](RefreshApiTokenResponse.md)

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

# **start_device_code_authorization_process**
> StartDeviceCodeAuthorizationProcessResponse start_device_code_authorization_process(app=app)

Start Device Code Authorization Process

### Overview

Starts the device code authorization process. Returns all the necessary information to complete the rest of the flow. This includes the following:

- `device_code` - The code your app will use for consecutive requests for getting the user token.

- `code` - This is the 6 digit code that you show to the user to be entered at the following verification_url.

- `verification_url` - This url which you will show as a QR code.

- `friendly_verification_url` - The friendly short url which you can show as plain text to user if they cannot use the QR code method.


You may also submit the `app` parameter to this request to show your app name on the `verification_url` page. This concretes user trust in authorizing your application to use their TorBox account. This is not required, but is a good idea. Default is "Third Party App". This name is also only allowed to be alpha-numeric characters (_A-Z,0-9_). Anything else will be filtered our when being shown to the user. The `friendly_verification_url` will always show "Third Party App" to keep the URL short.

The device_code is only valid for 10 minutes. Make sure the user is aware of this time limit so they submit and login before this time limit is over.

### Authorization

None required.


### Example


```python
import torbox
from torbox.models.start_device_code_authorization_process_response import StartDeviceCodeAuthorizationProcessResponse
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
    api_instance = torbox.UserApi(api_client)
    app = 'Third Party App' # str | The app name that the user will see when verifying the code. This should be the name of your app. (optional) (default to 'Third Party App')

    try:
        # Start Device Code Authorization Process
        api_response = api_instance.start_device_code_authorization_process(app=app)
        print("The response of UserApi->start_device_code_authorization_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->start_device_code_authorization_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| The app name that the user will see when verifying the code. This should be the name of your app. | [optional] [default to &#39;Third Party App&#39;]

### Return type

[**StartDeviceCodeAuthorizationProcessResponse**](StartDeviceCodeAuthorizationProcessResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

