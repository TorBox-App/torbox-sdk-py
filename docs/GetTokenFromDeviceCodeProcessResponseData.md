# GetTokenFromDeviceCodeProcessResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_token_from_device_code_process_response_data import GetTokenFromDeviceCodeProcessResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTokenFromDeviceCodeProcessResponseData from a JSON string
get_token_from_device_code_process_response_data_instance = GetTokenFromDeviceCodeProcessResponseData.from_json(json)
# print the JSON string representation of the object
print(GetTokenFromDeviceCodeProcessResponseData.to_json())

# convert the object into a dict
get_token_from_device_code_process_response_data_dict = get_token_from_device_code_process_response_data_instance.to_dict()
# create an instance of GetTokenFromDeviceCodeProcessResponseData from a dict
get_token_from_device_code_process_response_data_from_dict = GetTokenFromDeviceCodeProcessResponseData.from_dict(get_token_from_device_code_process_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


