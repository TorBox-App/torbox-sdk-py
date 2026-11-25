# EditTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**EditTagResponseData**](EditTagResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.edit_tag_response import EditTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditTagResponse from a JSON string
edit_tag_response_instance = EditTagResponse.from_json(json)
# print the JSON string representation of the object
print(EditTagResponse.to_json())

# convert the object into a dict
edit_tag_response_dict = edit_tag_response_instance.to_dict()
# create an instance of EditTagResponse from a dict
edit_tag_response_from_dict = EditTagResponse.from_dict(edit_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


