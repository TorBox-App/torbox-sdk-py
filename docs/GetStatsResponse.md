# GetStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetStatsResponseData**](GetStatsResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_stats_response import GetStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsResponse from a JSON string
get_stats_response_instance = GetStatsResponse.from_json(json)
# print the JSON string representation of the object
print(GetStatsResponse.to_json())

# convert the object into a dict
get_stats_response_dict = get_stats_response_instance.to_dict()
# create an instance of GetStatsResponse from a dict
get_stats_response_from_dict = GetStatsResponse.from_dict(get_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


