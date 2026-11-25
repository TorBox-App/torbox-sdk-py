# RegisterVendorUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**RegisterVendorUserResponseData**](RegisterVendorUserResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.register_vendor_user_response import RegisterVendorUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterVendorUserResponse from a JSON string
register_vendor_user_response_instance = RegisterVendorUserResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterVendorUserResponse.to_json())

# convert the object into a dict
register_vendor_user_response_dict = register_vendor_user_response_instance.to_dict()
# create an instance of RegisterVendorUserResponse from a dict
register_vendor_user_response_from_dict = RegisterVendorUserResponse.from_dict(register_vendor_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


