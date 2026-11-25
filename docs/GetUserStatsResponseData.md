# GetUserStatsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**GetUserStatsResponseDataGeneral**](GetUserStatsResponseDataGeneral.md) |  | [optional] 
**bandwidth** | [**List[GetUserStatsResponseDataBandwidthInner]**](GetUserStatsResponseDataBandwidthInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_user_stats_response_data import GetUserStatsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserStatsResponseData from a JSON string
get_user_stats_response_data_instance = GetUserStatsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetUserStatsResponseData.to_json())

# convert the object into a dict
get_user_stats_response_data_dict = get_user_stats_response_data_instance.to_dict()
# create an instance of GetUserStatsResponseData from a dict
get_user_stats_response_data_from_dict = GetUserStatsResponseData.from_dict(get_user_stats_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


