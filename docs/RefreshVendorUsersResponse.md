# RefreshVendorUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.refresh_vendor_users_response import RefreshVendorUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshVendorUsersResponse from a JSON string
refresh_vendor_users_response_instance = RefreshVendorUsersResponse.from_json(json)
# print the JSON string representation of the object
print(RefreshVendorUsersResponse.to_json())

# convert the object into a dict
refresh_vendor_users_response_dict = refresh_vendor_users_response_instance.to_dict()
# create an instance of RefreshVendorUsersResponse from a dict
refresh_vendor_users_response_from_dict = RefreshVendorUsersResponse.from_dict(refresh_vendor_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


