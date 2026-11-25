# Get30DayStatsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_downloads** | **int** |  | [optional] 
**total_users** | **int** |  | [optional] 
**total_bytes_downloaded** | **object** |  | [optional] 
**total_bytes_uploaded** | **object** |  | [optional] 
**total_bytes_egressed** | **object** |  | [optional] 
**total_servers** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from torbox.models.get30_day_stats_response_data_inner import Get30DayStatsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of Get30DayStatsResponseDataInner from a JSON string
get30_day_stats_response_data_inner_instance = Get30DayStatsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(Get30DayStatsResponseDataInner.to_json())

# convert the object into a dict
get30_day_stats_response_data_inner_dict = get30_day_stats_response_data_inner_instance.to_dict()
# create an instance of Get30DayStatsResponseDataInner from a dict
get30_day_stats_response_data_inner_from_dict = Get30DayStatsResponseDataInner.from_dict(get30_day_stats_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


