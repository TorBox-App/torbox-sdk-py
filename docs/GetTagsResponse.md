# GetTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetTagsResponseData**](GetTagsResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_tags_response import GetTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagsResponse from a JSON string
get_tags_response_instance = GetTagsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTagsResponse.to_json())

# convert the object into a dict
get_tags_response_dict = get_tags_response_instance.to_dict()
# create an instance of GetTagsResponse from a dict
get_tags_response_from_dict = GetTagsResponse.from_dict(get_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


