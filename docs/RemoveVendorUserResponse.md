# RemoveVendorUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.remove_vendor_user_response import RemoveVendorUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveVendorUserResponse from a JSON string
remove_vendor_user_response_instance = RemoveVendorUserResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveVendorUserResponse.to_json())

# convert the object into a dict
remove_vendor_user_response_dict = remove_vendor_user_response_instance.to_dict()
# create an instance of RemoveVendorUserResponse from a dict
remove_vendor_user_response_from_dict = RemoveVendorUserResponse.from_dict(remove_vendor_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


