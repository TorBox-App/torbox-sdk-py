# Get30DayStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[Get30DayStatsResponseDataInner]**](Get30DayStatsResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get30_day_stats_response import Get30DayStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get30DayStatsResponse from a JSON string
get30_day_stats_response_instance = Get30DayStatsResponse.from_json(json)
# print the JSON string representation of the object
print(Get30DayStatsResponse.to_json())

# convert the object into a dict
get30_day_stats_response_dict = get30_day_stats_response_instance.to_dict()
# create an instance of Get30DayStatsResponse from a dict
get30_day_stats_response_from_dict = Get30DayStatsResponse.from_dict(get30_day_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


