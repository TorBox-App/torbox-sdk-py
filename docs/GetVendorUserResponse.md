# GetVendorUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetVendorUserResponseData**](GetVendorUserResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_vendor_user_response import GetVendorUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVendorUserResponse from a JSON string
get_vendor_user_response_instance = GetVendorUserResponse.from_json(json)
# print the JSON string representation of the object
print(GetVendorUserResponse.to_json())

# convert the object into a dict
get_vendor_user_response_dict = get_vendor_user_response_instance.to_dict()
# create an instance of GetVendorUserResponse from a dict
get_vendor_user_response_from_dict = GetVendorUserResponse.from_dict(get_vendor_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


