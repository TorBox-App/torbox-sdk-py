# OAuthRegisterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | OAuth access token the service issued for the user. Required. | 
**refresh_token** | **str** | OAuth refresh token the service issued for the user. Required. | 

## Example

```python
from torbox.models.o_auth_register_request import OAuthRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthRegisterRequest from a JSON string
o_auth_register_request_instance = OAuthRegisterRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthRegisterRequest.to_json())

# convert the object into a dict
o_auth_register_request_dict = o_auth_register_request_instance.to_dict()
# create an instance of OAuthRegisterRequest from a dict
o_auth_register_request_from_dict = OAuthRegisterRequest.from_dict(o_auth_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


