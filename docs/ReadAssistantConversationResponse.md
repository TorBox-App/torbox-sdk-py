# ReadAssistantConversationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**ReadAssistantConversationResponseData**](ReadAssistantConversationResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.read_assistant_conversation_response import ReadAssistantConversationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAssistantConversationResponse from a JSON string
read_assistant_conversation_response_instance = ReadAssistantConversationResponse.from_json(json)
# print the JSON string representation of the object
print(ReadAssistantConversationResponse.to_json())

# convert the object into a dict
read_assistant_conversation_response_dict = read_assistant_conversation_response_instance.to_dict()
# create an instance of ReadAssistantConversationResponse from a dict
read_assistant_conversation_response_from_dict = ReadAssistantConversationResponse.from_dict(read_assistant_conversation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


