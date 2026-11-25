# GetHosterListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetHosterListResponseDataInner]**](GetHosterListResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_hoster_list_response import GetHosterListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHosterListResponse from a JSON string
get_hoster_list_response_instance = GetHosterListResponse.from_json(json)
# print the JSON string representation of the object
print(GetHosterListResponse.to_json())

# convert the object into a dict
get_hoster_list_response_dict = get_hoster_list_response_instance.to_dict()
# create an instance of GetHosterListResponse from a dict
get_hoster_list_response_from_dict = GetHosterListResponse.from_dict(get_hoster_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


