# GetNewsServerAccountResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**ssl** | **bool** |  | [optional] 
**connections** | **float** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_news_server_account_response_data import GetNewsServerAccountResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewsServerAccountResponseData from a JSON string
get_news_server_account_response_data_instance = GetNewsServerAccountResponseData.from_json(json)
# print the JSON string representation of the object
print(GetNewsServerAccountResponseData.to_json())

# convert the object into a dict
get_news_server_account_response_data_dict = get_news_server_account_response_data_instance.to_dict()
# create an instance of GetNewsServerAccountResponseData from a dict
get_news_server_account_response_data_from_dict = GetNewsServerAccountResponseData.from_dict(get_news_server_account_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


