# EditUserSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.edit_user_settings_response import EditUserSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserSettingsResponse from a JSON string
edit_user_settings_response_instance = EditUserSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(EditUserSettingsResponse.to_json())

# convert the object into a dict
edit_user_settings_response_dict = edit_user_settings_response_instance.to_dict()
# create an instance of EditUserSettingsResponse from a dict
edit_user_settings_response_from_dict = EditUserSettingsResponse.from_dict(edit_user_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


