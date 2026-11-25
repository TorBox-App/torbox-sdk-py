# GetAssistantUsageResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **float** |  | [optional] 
**resets_at** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_assistant_usage_response_data import GetAssistantUsageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssistantUsageResponseData from a JSON string
get_assistant_usage_response_data_instance = GetAssistantUsageResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAssistantUsageResponseData.to_json())

# convert the object into a dict
get_assistant_usage_response_data_dict = get_assistant_usage_response_data_instance.to_dict()
# create an instance of GetAssistantUsageResponseData from a dict
get_assistant_usage_response_data_from_dict = GetAssistantUsageResponseData.from_dict(get_assistant_usage_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


