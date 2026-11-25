# GetNewsServerAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetNewsServerAccountResponseData**](GetNewsServerAccountResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_news_server_account_response import GetNewsServerAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewsServerAccountResponse from a JSON string
get_news_server_account_response_instance = GetNewsServerAccountResponse.from_json(json)
# print the JSON string representation of the object
print(GetNewsServerAccountResponse.to_json())

# convert the object into a dict
get_news_server_account_response_dict = get_news_server_account_response_instance.to_dict()
# create an instance of GetNewsServerAccountResponse from a dict
get_news_server_account_response_from_dict = GetNewsServerAccountResponse.from_dict(get_news_server_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


