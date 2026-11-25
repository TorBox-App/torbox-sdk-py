# StartDeviceCodeAuthorizationProcessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**StartDeviceCodeAuthorizationProcessResponseData**](StartDeviceCodeAuthorizationProcessResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.start_device_code_authorization_process_response import StartDeviceCodeAuthorizationProcessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartDeviceCodeAuthorizationProcessResponse from a JSON string
start_device_code_authorization_process_response_instance = StartDeviceCodeAuthorizationProcessResponse.from_json(json)
# print the JSON string representation of the object
print(StartDeviceCodeAuthorizationProcessResponse.to_json())

# convert the object into a dict
start_device_code_authorization_process_response_dict = start_device_code_authorization_process_response_instance.to_dict()
# create an instance of StartDeviceCodeAuthorizationProcessResponse from a dict
start_device_code_authorization_process_response_from_dict = StartDeviceCodeAuthorizationProcessResponse.from_dict(start_device_code_authorization_process_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


