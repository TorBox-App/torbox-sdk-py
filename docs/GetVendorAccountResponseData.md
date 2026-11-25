# GetVendorAccountResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **int** |  | [optional] 
**vendor_token** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**vendor_email** | **str** |  | [optional] 
**vendor_url** | **str** |  | [optional] 
**vendor_status** | **str** |  | [optional] 
**users_allowed** | **float** |  | [optional] 
**current_users** | **float** |  | [optional] 
**can_register_new** | **bool** |  | [optional] 
**account_type** | **str** |  | [optional] 
**plan** | **int** |  | [optional] 
**paid_until** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**can_generate_vouchers** | **bool** |  | [optional] 

## Example

```python
from torbox.models.get_vendor_account_response_data import GetVendorAccountResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetVendorAccountResponseData from a JSON string
get_vendor_account_response_data_instance = GetVendorAccountResponseData.from_json(json)
# print the JSON string representation of the object
print(GetVendorAccountResponseData.to_json())

# convert the object into a dict
get_vendor_account_response_data_dict = get_vendor_account_response_data_instance.to_dict()
# create an instance of GetVendorAccountResponseData from a dict
get_vendor_account_response_data_from_dict = GetVendorAccountResponseData.from_dict(get_vendor_account_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


