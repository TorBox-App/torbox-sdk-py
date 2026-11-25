# GetNotificationFeedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetNotificationFeedResponseDataInner]**](GetNotificationFeedResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_notification_feed_response import GetNotificationFeedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotificationFeedResponse from a JSON string
get_notification_feed_response_instance = GetNotificationFeedResponse.from_json(json)
# print the JSON string representation of the object
print(GetNotificationFeedResponse.to_json())

# convert the object into a dict
get_notification_feed_response_dict = get_notification_feed_response_instance.to_dict()
# create an instance of GetNotificationFeedResponse from a dict
get_notification_feed_response_from_dict = GetNotificationFeedResponse.from_dict(get_notification_feed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


