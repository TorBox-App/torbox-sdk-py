# GetChangelogsJsonResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**html** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 

## Example

```python
from torbox.models.get_changelogs_json_response_data_inner import GetChangelogsJsonResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetChangelogsJsonResponseDataInner from a JSON string
get_changelogs_json_response_data_inner_instance = GetChangelogsJsonResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetChangelogsJsonResponseDataInner.to_json())

# convert the object into a dict
get_changelogs_json_response_data_inner_dict = get_changelogs_json_response_data_inner_instance.to_dict()
# create an instance of GetChangelogsJsonResponseDataInner from a dict
get_changelogs_json_response_data_inner_from_dict = GetChangelogsJsonResponseDataInner.from_dict(get_changelogs_json_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


