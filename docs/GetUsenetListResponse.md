# GetUsenetListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetUsenetListResponseDataInner]**](GetUsenetListResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_usenet_list_response import GetUsenetListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsenetListResponse from a JSON string
get_usenet_list_response_instance = GetUsenetListResponse.from_json(json)
# print the JSON string representation of the object
print(GetUsenetListResponse.to_json())

# convert the object into a dict
get_usenet_list_response_dict = get_usenet_list_response_instance.to_dict()
# create an instance of GetUsenetListResponse from a dict
get_usenet_list_response_from_dict = GetUsenetListResponse.from_dict(get_usenet_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


