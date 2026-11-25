# RegisterOauthLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.register_oauth_link_response import RegisterOauthLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterOauthLinkResponse from a JSON string
register_oauth_link_response_instance = RegisterOauthLinkResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterOauthLinkResponse.to_json())

# convert the object into a dict
register_oauth_link_response_dict = register_oauth_link_response_instance.to_dict()
# create an instance of RegisterOauthLinkResponse from a dict
register_oauth_link_response_from_dict = RegisterOauthLinkResponse.from_dict(register_oauth_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


