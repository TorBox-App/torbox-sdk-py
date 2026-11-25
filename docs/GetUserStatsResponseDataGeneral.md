# GetUserStatsResponseDataGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_downloaded** | **int** |  | [optional] 
**total_uploaded** | **int** |  | [optional] 
**ratio** | **float** |  | [optional] 
**total_items_downloaded** | **int** |  | [optional] 
**airlocked_downloads** | **float** |  | [optional] 
**airlock_storage_limit** | **int** |  | [optional] 

## Example

```python
from torbox.models.get_user_stats_response_data_general import GetUserStatsResponseDataGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserStatsResponseDataGeneral from a JSON string
get_user_stats_response_data_general_instance = GetUserStatsResponseDataGeneral.from_json(json)
# print the JSON string representation of the object
print(GetUserStatsResponseDataGeneral.to_json())

# convert the object into a dict
get_user_stats_response_data_general_dict = get_user_stats_response_data_general_instance.to_dict()
# create an instance of GetUserStatsResponseDataGeneral from a dict
get_user_stats_response_data_general_from_dict = GetUserStatsResponseDataGeneral.from_dict(get_user_stats_response_data_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


