# GetUpStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.get_up_status_response import GetUpStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUpStatusResponse from a JSON string
get_up_status_response_instance = GetUpStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetUpStatusResponse.to_json())

# convert the object into a dict
get_up_status_response_dict = get_up_status_response_instance.to_dict()
# create an instance of GetUpStatusResponse from a dict
get_up_status_response_from_dict = GetUpStatusResponse.from_dict(get_up_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


