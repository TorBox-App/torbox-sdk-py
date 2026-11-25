# GetRssFeedItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetRssFeedItemsResponseDataInner]**](GetRssFeedItemsResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_rss_feed_items_response import GetRssFeedItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRssFeedItemsResponse from a JSON string
get_rss_feed_items_response_instance = GetRssFeedItemsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRssFeedItemsResponse.to_json())

# convert the object into a dict
get_rss_feed_items_response_dict = get_rss_feed_items_response_instance.to_dict()
# create an instance of GetRssFeedItemsResponse from a dict
get_rss_feed_items_response_from_dict = GetRssFeedItemsResponse.from_dict(get_rss_feed_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


