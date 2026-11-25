# EditRssFeedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.edit_rss_feed_response import EditRssFeedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditRssFeedResponse from a JSON string
edit_rss_feed_response_instance = EditRssFeedResponse.from_json(json)
# print the JSON string representation of the object
print(EditRssFeedResponse.to_json())

# convert the object into a dict
edit_rss_feed_response_dict = edit_rss_feed_response_instance.to_dict()
# create an instance of EditRssFeedResponse from a dict
edit_rss_feed_response_from_dict = EditRssFeedResponse.from_dict(edit_rss_feed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


