# GetTagsResponseDataString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] 
**torrent_ids** | **List[int]** |  | [optional] 
**usenet_ids** | **List[int]** |  | [optional] 
**web_ids** | **List[int]** |  | [optional] 
**num_downloads** | **float** |  | [optional] 
**total_size** | **int** |  | [optional] 

## Example

```python
from torbox.models.get_tags_response_data_string import GetTagsResponseDataString

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagsResponseDataString from a JSON string
get_tags_response_data_string_instance = GetTagsResponseDataString.from_json(json)
# print the JSON string representation of the object
print(GetTagsResponseDataString.to_json())

# convert the object into a dict
get_tags_response_data_string_dict = get_tags_response_data_string_instance.to_dict()
# create an instance of GetTagsResponseDataString from a dict
get_tags_response_data_string_from_dict = GetTagsResponseDataString.from_dict(get_tags_response_data_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


