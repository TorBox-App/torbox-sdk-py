# DeleteAssistantConversationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**DeleteAssistantConversationsResponseData**](DeleteAssistantConversationsResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.delete_assistant_conversations_response import DeleteAssistantConversationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAssistantConversationsResponse from a JSON string
delete_assistant_conversations_response_instance = DeleteAssistantConversationsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAssistantConversationsResponse.to_json())

# convert the object into a dict
delete_assistant_conversations_response_dict = delete_assistant_conversations_response_instance.to_dict()
# create an instance of DeleteAssistantConversationsResponse from a dict
delete_assistant_conversations_response_from_dict = DeleteAssistantConversationsResponse.from_dict(delete_assistant_conversations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


