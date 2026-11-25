# RefreshApiTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **str** |  | [optional] 

## Example

```python
from torbox.models.refresh_api_token_response import RefreshApiTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshApiTokenResponse from a JSON string
refresh_api_token_response_instance = RefreshApiTokenResponse.from_json(json)
# print the JSON string representation of the object
print(RefreshApiTokenResponse.to_json())

# convert the object into a dict
refresh_api_token_response_dict = refresh_api_token_response_instance.to_dict()
# create an instance of RefreshApiTokenResponse from a dict
refresh_api_token_response_from_dict = RefreshApiTokenResponse.from_dict(refresh_api_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


