# GetChangelogsJsonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetChangelogsJsonResponseDataInner]**](GetChangelogsJsonResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_changelogs_json_response import GetChangelogsJsonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChangelogsJsonResponse from a JSON string
get_changelogs_json_response_instance = GetChangelogsJsonResponse.from_json(json)
# print the JSON string representation of the object
print(GetChangelogsJsonResponse.to_json())

# convert the object into a dict
get_changelogs_json_response_dict = get_changelogs_json_response_instance.to_dict()
# create an instance of GetChangelogsJsonResponse from a dict
get_changelogs_json_response_from_dict = GetChangelogsJsonResponse.from_dict(get_changelogs_json_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


