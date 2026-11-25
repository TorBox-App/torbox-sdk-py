# StartDeviceCodeAuthorizationProcessResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**interval** | **float** |  | [optional] 
**expires_in** | **float** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**verification_url** | **str** |  | [optional] 
**verification_url_complete** | **str** |  | [optional] 
**friendly_verification_url** | **str** |  | [optional] 

## Example

```python
from torbox.models.start_device_code_authorization_process_response_data import StartDeviceCodeAuthorizationProcessResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of StartDeviceCodeAuthorizationProcessResponseData from a JSON string
start_device_code_authorization_process_response_data_instance = StartDeviceCodeAuthorizationProcessResponseData.from_json(json)
# print the JSON string representation of the object
print(StartDeviceCodeAuthorizationProcessResponseData.to_json())

# convert the object into a dict
start_device_code_authorization_process_response_data_dict = start_device_code_authorization_process_response_data_instance.to_dict()
# create an instance of StartDeviceCodeAuthorizationProcessResponseData from a dict
start_device_code_authorization_process_response_data_from_dict = StartDeviceCodeAuthorizationProcessResponseData.from_dict(start_device_code_authorization_process_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


