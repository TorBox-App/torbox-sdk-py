# EditUsenetItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.edit_usenet_item_response import EditUsenetItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditUsenetItemResponse from a JSON string
edit_usenet_item_response_instance = EditUsenetItemResponse.from_json(json)
# print the JSON string representation of the object
print(EditUsenetItemResponse.to_json())

# convert the object into a dict
edit_usenet_item_response_dict = edit_usenet_item_response_instance.to_dict()
# create an instance of EditUsenetItemResponse from a dict
edit_usenet_item_response_from_dict = EditUsenetItemResponse.from_dict(edit_usenet_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


