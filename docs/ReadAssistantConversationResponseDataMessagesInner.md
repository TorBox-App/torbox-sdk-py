# ReadAssistantConversationResponseDataMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**at** | **float** |  | [optional] 

## Example

```python
from torbox.models.read_assistant_conversation_response_data_messages_inner import ReadAssistantConversationResponseDataMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAssistantConversationResponseDataMessagesInner from a JSON string
read_assistant_conversation_response_data_messages_inner_instance = ReadAssistantConversationResponseDataMessagesInner.from_json(json)
# print the JSON string representation of the object
print(ReadAssistantConversationResponseDataMessagesInner.to_json())

# convert the object into a dict
read_assistant_conversation_response_data_messages_inner_dict = read_assistant_conversation_response_data_messages_inner_instance.to_dict()
# create an instance of ReadAssistantConversationResponseDataMessagesInner from a dict
read_assistant_conversation_response_data_messages_inner_from_dict = ReadAssistantConversationResponseDataMessagesInner.from_dict(read_assistant_conversation_response_data_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


