# GetStatsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_users** | **int** |  | [optional] 
**total_servers** | **int** |  | [optional] 

## Example

```python
from torbox.models.get_stats_response_data import GetStatsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsResponseData from a JSON string
get_stats_response_data_instance = GetStatsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetStatsResponseData.to_json())

# convert the object into a dict
get_stats_response_data_dict = get_stats_response_data_instance.to_dict()
# create an instance of GetStatsResponseData from a dict
get_stats_response_data_from_dict = GetStatsResponseData.from_dict(get_stats_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


