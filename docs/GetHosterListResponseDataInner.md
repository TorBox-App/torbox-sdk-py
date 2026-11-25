# GetHosterListResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**domains** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**note** | **object** |  | [optional] 
**nsfw** | **bool** |  | [optional] 
**daily_link_limit** | **int** |  | [optional] 
**daily_link_used** | **float** |  | [optional] 
**daily_bandwidth_limit** | **int** |  | [optional] 
**daily_bandwidth_used** | **int** |  | [optional] 
**per_link_size_limit** | **int** |  | [optional] 
**regex** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_hoster_list_response_data_inner import GetHosterListResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHosterListResponseDataInner from a JSON string
get_hoster_list_response_data_inner_instance = GetHosterListResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetHosterListResponseDataInner.to_json())

# convert the object into a dict
get_hoster_list_response_data_inner_dict = get_hoster_list_response_data_inner_instance.to_dict()
# create an instance of GetHosterListResponseDataInner from a dict
get_hoster_list_response_data_inner_from_dict = GetHosterListResponseDataInner.from_dict(get_hoster_list_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


