# GetUserRssFeedsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetUserRssFeedsResponseDataInner]**](GetUserRssFeedsResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_user_rss_feeds_response import GetUserRssFeedsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserRssFeedsResponse from a JSON string
get_user_rss_feeds_response_instance = GetUserRssFeedsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserRssFeedsResponse.to_json())

# convert the object into a dict
get_user_rss_feeds_response_dict = get_user_rss_feeds_response_instance.to_dict()
# create an instance of GetUserRssFeedsResponse from a dict
get_user_rss_feeds_response_from_dict = GetUserRssFeedsResponse.from_dict(get_user_rss_feeds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


