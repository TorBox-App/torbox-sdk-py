# GetUserDataResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_referral** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**plan** | **int** |  | [optional] 
**total_downloaded** | **int** |  | [optional] 
**customer** | **str** |  | [optional] 
**is_subscribed** | **bool** |  | [optional] 
**premium_expires_at** | **str** |  | [optional] 
**cooldown_until** | **str** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**base_email** | **str** |  | [optional] 
**total_bytes_downloaded** | **int** |  | [optional] 
**total_bytes_uploaded** | **int** |  | [optional] 
**torrents_downloaded** | **float** |  | [optional] 
**web_downloads_downloaded** | **float** |  | [optional] 
**usenet_downloads_downloaded** | **float** |  | [optional] 
**additional_concurrent_slots** | **int** |  | [optional] 
**long_term_seeding** | **bool** |  | [optional] 
**vendor_id** | **int** |  | [optional] 
**is_vendor** | **bool** |  | [optional] 
**purchases_referred** | **float** |  | [optional] 
**long_term_storage** | **bool** |  | [optional] 
**settings** | [**GetUserDataResponseDataSettings**](GetUserDataResponseDataSettings.md) |  | [optional] 

## Example

```python
from torbox.models.get_user_data_response_data import GetUserDataResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserDataResponseData from a JSON string
get_user_data_response_data_instance = GetUserDataResponseData.from_json(json)
# print the JSON string representation of the object
print(GetUserDataResponseData.to_json())

# convert the object into a dict
get_user_data_response_data_dict = get_user_data_response_data_instance.to_dict()
# create an instance of GetUserDataResponseData from a dict
get_user_data_response_data_from_dict = GetUserDataResponseData.from_dict(get_user_data_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


