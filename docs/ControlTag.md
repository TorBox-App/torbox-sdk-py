# ControlTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**operation** | **str** |  | 

## Example

```python
from torbox.models.control_tag import ControlTag

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTag from a JSON string
control_tag_instance = ControlTag.from_json(json)
# print the JSON string representation of the object
print(ControlTag.to_json())

# convert the object into a dict
control_tag_dict = control_tag_instance.to_dict()
# create an instance of ControlTag from a dict
control_tag_from_dict = ControlTag.from_dict(control_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


