# GetUserRssFeedsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**last_checked** | **str** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_name** | **str** |  | [optional] 
**do_regex** | **str** |  | [optional] 
**dont_regex** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**scan_interval** | **float** |  | [optional] 
**dont_older_than** | **float** |  | [optional] 
**status_message** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**torrent_seeding** | **float** |  | [optional] 

## Example

```python
from torbox.models.get_user_rss_feeds_response_data_inner import GetUserRssFeedsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserRssFeedsResponseDataInner from a JSON string
get_user_rss_feeds_response_data_inner_instance = GetUserRssFeedsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetUserRssFeedsResponseDataInner.to_json())

# convert the object into a dict
get_user_rss_feeds_response_data_inner_dict = get_user_rss_feeds_response_data_inner_instance.to_dict()
# create an instance of GetUserRssFeedsResponseDataInner from a dict
get_user_rss_feeds_response_data_inner_from_dict = GetUserRssFeedsResponseDataInner.from_dict(get_user_rss_feeds_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


