# GetTagsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | [**GetTagsResponseDataString**](GetTagsResponseDataString.md) |  | [optional] 

## Example

```python
from torbox.models.get_tags_response_data import GetTagsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagsResponseData from a JSON string
get_tags_response_data_instance = GetTagsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetTagsResponseData.to_json())

# convert the object into a dict
get_tags_response_data_dict = get_tags_response_data_instance.to_dict()
# create an instance of GetTagsResponseData from a dict
get_tags_response_data_from_dict = GetTagsResponseData.from_dict(get_tags_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


