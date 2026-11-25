# SendTestNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.send_test_notification_response import SendTestNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendTestNotificationResponse from a JSON string
send_test_notification_response_instance = SendTestNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(SendTestNotificationResponse.to_json())

# convert the object into a dict
send_test_notification_response_dict = send_test_notification_response_instance.to_dict()
# create an instance of SendTestNotificationResponse from a dict
send_test_notification_response_from_dict = SendTestNotificationResponse.from_dict(send_test_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


