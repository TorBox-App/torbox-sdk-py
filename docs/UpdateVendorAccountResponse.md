# UpdateVendorAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetVendorAccountResponseData**](GetVendorAccountResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.update_vendor_account_response import UpdateVendorAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVendorAccountResponse from a JSON string
update_vendor_account_response_instance = UpdateVendorAccountResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateVendorAccountResponse.to_json())

# convert the object into a dict
update_vendor_account_response_dict = update_vendor_account_response_instance.to_dict()
# create an instance of UpdateVendorAccountResponse from a dict
update_vendor_account_response_from_dict = UpdateVendorAccountResponse.from_dict(update_vendor_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


