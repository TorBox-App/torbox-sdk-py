# GetOauthIntegrationsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trakt** | **bool** |  | [optional] 
**mal** | **bool** |  | [optional] 
**anilist** | **bool** |  | [optional] 
**simkl** | **bool** |  | [optional] 

## Example

```python
from torbox.models.get_oauth_integrations_response_data import GetOauthIntegrationsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetOauthIntegrationsResponseData from a JSON string
get_oauth_integrations_response_data_instance = GetOauthIntegrationsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetOauthIntegrationsResponseData.to_json())

# convert the object into a dict
get_oauth_integrations_response_data_dict = get_oauth_integrations_response_data_instance.to_dict()
# create an instance of GetOauthIntegrationsResponseData from a dict
get_oauth_integrations_response_data_from_dict = GetOauthIntegrationsResponseData.from_dict(get_oauth_integrations_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


