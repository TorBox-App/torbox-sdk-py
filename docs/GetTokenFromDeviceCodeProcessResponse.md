# GetTokenFromDeviceCodeProcessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetTokenFromDeviceCodeProcessResponseData**](GetTokenFromDeviceCodeProcessResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_token_from_device_code_process_response import GetTokenFromDeviceCodeProcessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTokenFromDeviceCodeProcessResponse from a JSON string
get_token_from_device_code_process_response_instance = GetTokenFromDeviceCodeProcessResponse.from_json(json)
# print the JSON string representation of the object
print(GetTokenFromDeviceCodeProcessResponse.to_json())

# convert the object into a dict
get_token_from_device_code_process_response_dict = get_token_from_device_code_process_response_instance.to_dict()
# create an instance of GetTokenFromDeviceCodeProcessResponse from a dict
get_token_from_device_code_process_response_from_dict = GetTokenFromDeviceCodeProcessResponse.from_dict(get_token_from_device_code_process_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


