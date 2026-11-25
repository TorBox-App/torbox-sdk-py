# GetOauthIntegrationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetOauthIntegrationsResponseData**](GetOauthIntegrationsResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_oauth_integrations_response import GetOauthIntegrationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOauthIntegrationsResponse from a JSON string
get_oauth_integrations_response_instance = GetOauthIntegrationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOauthIntegrationsResponse.to_json())

# convert the object into a dict
get_oauth_integrations_response_dict = get_oauth_integrations_response_instance.to_dict()
# create an instance of GetOauthIntegrationsResponse from a dict
get_oauth_integrations_response_from_dict = GetOauthIntegrationsResponse.from_dict(get_oauth_integrations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


