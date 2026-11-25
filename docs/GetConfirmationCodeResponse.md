# GetConfirmationCodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.get_confirmation_code_response import GetConfirmationCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfirmationCodeResponse from a JSON string
get_confirmation_code_response_instance = GetConfirmationCodeResponse.from_json(json)
# print the JSON string representation of the object
print(GetConfirmationCodeResponse.to_json())

# convert the object into a dict
get_confirmation_code_response_dict = get_confirmation_code_response_instance.to_dict()
# create an instance of GetConfirmationCodeResponse from a dict
get_confirmation_code_response_from_dict = GetConfirmationCodeResponse.from_dict(get_confirmation_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


