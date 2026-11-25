# GetAssistantUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetAssistantUsageResponseData**](GetAssistantUsageResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_assistant_usage_response import GetAssistantUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssistantUsageResponse from a JSON string
get_assistant_usage_response_instance = GetAssistantUsageResponse.from_json(json)
# print the JSON string representation of the object
print(GetAssistantUsageResponse.to_json())

# convert the object into a dict
get_assistant_usage_response_dict = get_assistant_usage_response_instance.to_dict()
# create an instance of GetAssistantUsageResponse from a dict
get_assistant_usage_response_from_dict = GetAssistantUsageResponse.from_dict(get_assistant_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


