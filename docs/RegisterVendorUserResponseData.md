# RegisterVendorUserResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**base_email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**customer** | **str** |  | [optional] 
**vendor_id** | **int** |  | [optional] 

## Example

```python
from torbox.models.register_vendor_user_response_data import RegisterVendorUserResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterVendorUserResponseData from a JSON string
register_vendor_user_response_data_instance = RegisterVendorUserResponseData.from_json(json)
# print the JSON string representation of the object
print(RegisterVendorUserResponseData.to_json())

# convert the object into a dict
register_vendor_user_response_data_dict = register_vendor_user_response_data_instance.to_dict()
# create an instance of RegisterVendorUserResponseData from a dict
register_vendor_user_response_data_from_dict = RegisterVendorUserResponseData.from_dict(register_vendor_user_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


