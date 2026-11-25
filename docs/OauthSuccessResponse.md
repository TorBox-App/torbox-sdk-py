# OauthSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.oauth_success_response import OauthSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OauthSuccessResponse from a JSON string
oauth_success_response_instance = OauthSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(OauthSuccessResponse.to_json())

# convert the object into a dict
oauth_success_response_dict = oauth_success_response_instance.to_dict()
# create an instance of OauthSuccessResponse from a dict
oauth_success_response_from_dict = OauthSuccessResponse.from_dict(oauth_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


