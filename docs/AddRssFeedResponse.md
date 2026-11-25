# AddRssFeedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.add_rss_feed_response import AddRssFeedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddRssFeedResponse from a JSON string
add_rss_feed_response_instance = AddRssFeedResponse.from_json(json)
# print the JSON string representation of the object
print(AddRssFeedResponse.to_json())

# convert the object into a dict
add_rss_feed_response_dict = add_rss_feed_response_instance.to_dict()
# create an instance of AddRssFeedResponse from a dict
add_rss_feed_response_from_dict = AddRssFeedResponse.from_dict(add_rss_feed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


