# GetSubscriptionsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**subscription_code** | **str** |  | [optional] 
**email_token** | **str** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**plan_code** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**plan_name** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_subscriptions_response_data_inner import GetSubscriptionsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionsResponseDataInner from a JSON string
get_subscriptions_response_data_inner_instance = GetSubscriptionsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionsResponseDataInner.to_json())

# convert the object into a dict
get_subscriptions_response_data_inner_dict = get_subscriptions_response_data_inner_instance.to_dict()
# create an instance of GetSubscriptionsResponseDataInner from a dict
get_subscriptions_response_data_inner_from_dict = GetSubscriptionsResponseDataInner.from_dict(get_subscriptions_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


