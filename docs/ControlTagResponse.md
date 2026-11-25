# ControlTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.control_tag_response import ControlTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTagResponse from a JSON string
control_tag_response_instance = ControlTagResponse.from_json(json)
# print the JSON string representation of the object
print(ControlTagResponse.to_json())

# convert the object into a dict
control_tag_response_dict = control_tag_response_instance.to_dict()
# create an instance of ControlTagResponse from a dict
control_tag_response_from_dict = ControlTagResponse.from_dict(control_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


