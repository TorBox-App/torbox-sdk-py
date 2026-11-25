# ListAssistantConversationsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**created_at** | **float** |  | [optional] 
**updated_at** | **float** |  | [optional] 
**messages** | **float** |  | [optional] 
**support** | [**ListAssistantConversationsResponseDataInnerSupport**](ListAssistantConversationsResponseDataInnerSupport.md) |  | [optional] 

## Example

```python
from torbox.models.list_assistant_conversations_response_data_inner import ListAssistantConversationsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAssistantConversationsResponseDataInner from a JSON string
list_assistant_conversations_response_data_inner_instance = ListAssistantConversationsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListAssistantConversationsResponseDataInner.to_json())

# convert the object into a dict
list_assistant_conversations_response_data_inner_dict = list_assistant_conversations_response_data_inner_instance.to_dict()
# create an instance of ListAssistantConversationsResponseDataInner from a dict
list_assistant_conversations_response_data_inner_from_dict = ListAssistantConversationsResponseDataInner.from_dict(list_assistant_conversations_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


