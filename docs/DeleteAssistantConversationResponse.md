# DeleteAssistantConversationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.delete_assistant_conversation_response import DeleteAssistantConversationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAssistantConversationResponse from a JSON string
delete_assistant_conversation_response_instance = DeleteAssistantConversationResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAssistantConversationResponse.to_json())

# convert the object into a dict
delete_assistant_conversation_response_dict = delete_assistant_conversation_response_instance.to_dict()
# create an instance of DeleteAssistantConversationResponse from a dict
delete_assistant_conversation_response_from_dict = DeleteAssistantConversationResponse.from_dict(delete_assistant_conversation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


