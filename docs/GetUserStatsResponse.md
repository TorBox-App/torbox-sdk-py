# GetUserStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetUserStatsResponseData**](GetUserStatsResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_user_stats_response import GetUserStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserStatsResponse from a JSON string
get_user_stats_response_instance = GetUserStatsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserStatsResponse.to_json())

# convert the object into a dict
get_user_stats_response_dict = get_user_stats_response_instance.to_dict()
# create an instance of GetUserStatsResponse from a dict
get_user_stats_response_from_dict = GetUserStatsResponse.from_dict(get_user_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


