# GetVendorUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetVendorUsersResponseDataInner]**](GetVendorUsersResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_vendor_users_response import GetVendorUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVendorUsersResponse from a JSON string
get_vendor_users_response_instance = GetVendorUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetVendorUsersResponse.to_json())

# convert the object into a dict
get_vendor_users_response_dict = get_vendor_users_response_instance.to_dict()
# create an instance of GetVendorUsersResponse from a dict
get_vendor_users_response_from_dict = GetVendorUsersResponse.from_dict(get_vendor_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


