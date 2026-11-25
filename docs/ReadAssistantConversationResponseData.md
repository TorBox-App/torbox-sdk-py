# ReadAssistantConversationResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**created_at** | **float** |  | [optional] 
**updated_at** | **float** |  | [optional] 
**revision** | **float** |  | [optional] 
**messages** | [**List[ReadAssistantConversationResponseDataMessagesInner]**](ReadAssistantConversationResponseDataMessagesInner.md) |  | [optional] 
**support** | **object** |  | [optional] 

## Example

```python
from torbox.models.read_assistant_conversation_response_data import ReadAssistantConversationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAssistantConversationResponseData from a JSON string
read_assistant_conversation_response_data_instance = ReadAssistantConversationResponseData.from_json(json)
# print the JSON string representation of the object
print(ReadAssistantConversationResponseData.to_json())

# convert the object into a dict
read_assistant_conversation_response_data_dict = read_assistant_conversation_response_data_instance.to_dict()
# create an instance of ReadAssistantConversationResponseData from a dict
read_assistant_conversation_response_data_from_dict = ReadAssistantConversationResponseData.from_dict(read_assistant_conversation_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


