# GetSubscriptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetSubscriptionsResponseDataInner]**](GetSubscriptionsResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_subscriptions_response import GetSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionsResponse from a JSON string
get_subscriptions_response_instance = GetSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionsResponse.to_json())

# convert the object into a dict
get_subscriptions_response_dict = get_subscriptions_response_instance.to_dict()
# create an instance of GetSubscriptionsResponse from a dict
get_subscriptions_response_from_dict = GetSubscriptionsResponse.from_dict(get_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


