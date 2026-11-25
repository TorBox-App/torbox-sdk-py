# ResetNewsServerAccountPasswordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetNewsServerAccountResponseData**](GetNewsServerAccountResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.reset_news_server_account_password_response import ResetNewsServerAccountPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResetNewsServerAccountPasswordResponse from a JSON string
reset_news_server_account_password_response_instance = ResetNewsServerAccountPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(ResetNewsServerAccountPasswordResponse.to_json())

# convert the object into a dict
reset_news_server_account_password_response_dict = reset_news_server_account_password_response_instance.to_dict()
# create an instance of ResetNewsServerAccountPasswordResponse from a dict
reset_news_server_account_password_response_from_dict = ResetNewsServerAccountPasswordResponse.from_dict(reset_news_server_account_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


