# GetUserStatsResponseDataBandwidthInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**bytes_downloaded** | **int** |  | [optional] 

## Example

```python
from torbox.models.get_user_stats_response_data_bandwidth_inner import GetUserStatsResponseDataBandwidthInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserStatsResponseDataBandwidthInner from a JSON string
get_user_stats_response_data_bandwidth_inner_instance = GetUserStatsResponseDataBandwidthInner.from_json(json)
# print the JSON string representation of the object
print(GetUserStatsResponseDataBandwidthInner.to_json())

# convert the object into a dict
get_user_stats_response_data_bandwidth_inner_dict = get_user_stats_response_data_bandwidth_inner_instance.to_dict()
# create an instance of GetUserStatsResponseDataBandwidthInner from a dict
get_user_stats_response_data_bandwidth_inner_from_dict = GetUserStatsResponseDataBandwidthInner.from_dict(get_user_stats_response_data_bandwidth_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


