# ListAssistantConversationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[ListAssistantConversationsResponseDataInner]**](ListAssistantConversationsResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.list_assistant_conversations_response import ListAssistantConversationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAssistantConversationsResponse from a JSON string
list_assistant_conversations_response_instance = ListAssistantConversationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAssistantConversationsResponse.to_json())

# convert the object into a dict
list_assistant_conversations_response_dict = list_assistant_conversations_response_instance.to_dict()
# create an instance of ListAssistantConversationsResponse from a dict
list_assistant_conversations_response_from_dict = ListAssistantConversationsResponse.from_dict(list_assistant_conversations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


