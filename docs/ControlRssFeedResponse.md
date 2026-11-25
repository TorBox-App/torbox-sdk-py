# ControlRssFeedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.control_rss_feed_response import ControlRssFeedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ControlRssFeedResponse from a JSON string
control_rss_feed_response_instance = ControlRssFeedResponse.from_json(json)
# print the JSON string representation of the object
print(ControlRssFeedResponse.to_json())

# convert the object into a dict
control_rss_feed_response_dict = control_rss_feed_response_instance.to_dict()
# create an instance of ControlRssFeedResponse from a dict
control_rss_feed_response_from_dict = ControlRssFeedResponse.from_dict(control_rss_feed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


