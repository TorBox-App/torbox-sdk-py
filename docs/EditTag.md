# EditTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**new_name** | **str** |  | 

## Example

```python
from torbox.models.edit_tag import EditTag

# TODO update the JSON string below
json = "{}"
# create an instance of EditTag from a JSON string
edit_tag_instance = EditTag.from_json(json)
# print the JSON string representation of the object
print(EditTag.to_json())

# convert the object into a dict
edit_tag_dict = edit_tag_instance.to_dict()
# create an instance of EditTag from a dict
edit_tag_from_dict = EditTag.from_dict(edit_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


