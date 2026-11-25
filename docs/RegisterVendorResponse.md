# RegisterVendorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**RegisterVendorResponseData**](RegisterVendorResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.register_vendor_response import RegisterVendorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterVendorResponse from a JSON string
register_vendor_response_instance = RegisterVendorResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterVendorResponse.to_json())

# convert the object into a dict
register_vendor_response_dict = register_vendor_response_instance.to_dict()
# create an instance of RegisterVendorResponse from a dict
register_vendor_response_from_dict = RegisterVendorResponse.from_dict(register_vendor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


