# UnregisterOauthLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.unregister_oauth_link_response import UnregisterOauthLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterOauthLinkResponse from a JSON string
unregister_oauth_link_response_instance = UnregisterOauthLinkResponse.from_json(json)
# print the JSON string representation of the object
print(UnregisterOauthLinkResponse.to_json())

# convert the object into a dict
unregister_oauth_link_response_dict = unregister_oauth_link_response_instance.to_dict()
# create an instance of UnregisterOauthLinkResponse from a dict
unregister_oauth_link_response_from_dict = UnregisterOauthLinkResponse.from_dict(unregister_oauth_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


