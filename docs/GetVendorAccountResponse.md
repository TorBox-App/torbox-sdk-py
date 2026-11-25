# GetVendorAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetVendorAccountResponseData**](GetVendorAccountResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_vendor_account_response import GetVendorAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVendorAccountResponse from a JSON string
get_vendor_account_response_instance = GetVendorAccountResponse.from_json(json)
# print the JSON string representation of the object
print(GetVendorAccountResponse.to_json())

# convert the object into a dict
get_vendor_account_response_dict = get_vendor_account_response_instance.to_dict()
# create an instance of GetVendorAccountResponse from a dict
get_vendor_account_response_from_dict = GetVendorAccountResponse.from_dict(get_vendor_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


