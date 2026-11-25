# ClearSingleNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.clear_single_notification_response import ClearSingleNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClearSingleNotificationResponse from a JSON string
clear_single_notification_response_instance = ClearSingleNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(ClearSingleNotificationResponse.to_json())

# convert the object into a dict
clear_single_notification_response_dict = clear_single_notification_response_instance.to_dict()
# create an instance of ClearSingleNotificationResponse from a dict
clear_single_notification_response_from_dict = ClearSingleNotificationResponse.from_dict(clear_single_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


