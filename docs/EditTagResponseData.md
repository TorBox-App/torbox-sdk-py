# EditTagResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from torbox.models.edit_tag_response_data import EditTagResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EditTagResponseData from a JSON string
edit_tag_response_data_instance = EditTagResponseData.from_json(json)
# print the JSON string representation of the object
print(EditTagResponseData.to_json())

# convert the object into a dict
edit_tag_response_data_dict = edit_tag_response_data_instance.to_dict()
# create an instance of EditTagResponseData from a dict
edit_tag_response_data_from_dict = EditTagResponseData.from_dict(edit_tag_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


