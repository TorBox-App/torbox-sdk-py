# GetRssFeedItemsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**rss_name** | **str** |  | [optional] 
**rss_url** | **str** |  | [optional] 
**ignored** | **bool** |  | [optional] 
**downloaded** | **bool** |  | [optional] 
**link** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**seed_torrents** | **float** |  | [optional] 

## Example

```python
from torbox.models.get_rss_feed_items_response_data_inner import GetRssFeedItemsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRssFeedItemsResponseDataInner from a JSON string
get_rss_feed_items_response_data_inner_instance = GetRssFeedItemsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetRssFeedItemsResponseDataInner.to_json())

# convert the object into a dict
get_rss_feed_items_response_data_inner_dict = get_rss_feed_items_response_data_inner_instance.to_dict()
# create an instance of GetRssFeedItemsResponseDataInner from a dict
get_rss_feed_items_response_data_inner_from_dict = GetRssFeedItemsResponseDataInner.from_dict(get_rss_feed_items_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


