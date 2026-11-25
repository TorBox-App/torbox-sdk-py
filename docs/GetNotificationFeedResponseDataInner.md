# GetNotificationFeedResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**action_data** | **str** |  | [optional] 
**action_cta** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_notification_feed_response_data_inner import GetNotificationFeedResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotificationFeedResponseDataInner from a JSON string
get_notification_feed_response_data_inner_instance = GetNotificationFeedResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetNotificationFeedResponseDataInner.to_json())

# convert the object into a dict
get_notification_feed_response_data_inner_dict = get_notification_feed_response_data_inner_instance.to_dict()
# create an instance of GetNotificationFeedResponseDataInner from a dict
get_notification_feed_response_data_inner_from_dict = GetNotificationFeedResponseDataInner.from_dict(get_notification_feed_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


