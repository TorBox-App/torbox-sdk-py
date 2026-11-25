# GetNewsServerConnectionInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetNewsServerConnectionInformationResponseData**](GetNewsServerConnectionInformationResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_news_server_connection_information_response import GetNewsServerConnectionInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewsServerConnectionInformationResponse from a JSON string
get_news_server_connection_information_response_instance = GetNewsServerConnectionInformationResponse.from_json(json)
# print the JSON string representation of the object
print(GetNewsServerConnectionInformationResponse.to_json())

# convert the object into a dict
get_news_server_connection_information_response_dict = get_news_server_connection_information_response_instance.to_dict()
# create an instance of GetNewsServerConnectionInformationResponse from a dict
get_news_server_connection_information_response_from_dict = GetNewsServerConnectionInformationResponse.from_dict(get_news_server_connection_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


