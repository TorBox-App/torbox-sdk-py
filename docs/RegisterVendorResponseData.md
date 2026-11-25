# RegisterVendorResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **int** |  | [optional] 
**vendor_token** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**vendor_url** | **str** |  | [optional] 
**vendor_status** | **str** |  | [optional] 

## Example

```python
from torbox.models.register_vendor_response_data import RegisterVendorResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterVendorResponseData from a JSON string
register_vendor_response_data_instance = RegisterVendorResponseData.from_json(json)
# print the JSON string representation of the object
print(RegisterVendorResponseData.to_json())

# convert the object into a dict
register_vendor_response_data_dict = register_vendor_response_data_instance.to_dict()
# create an instance of RegisterVendorResponseData from a dict
register_vendor_response_data_from_dict = RegisterVendorResponseData.from_dict(register_vendor_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


