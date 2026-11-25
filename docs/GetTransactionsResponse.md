# GetTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetTransactionsResponseDataInner]**](GetTransactionsResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_transactions_response import GetTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsResponse from a JSON string
get_transactions_response_instance = GetTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsResponse.to_json())

# convert the object into a dict
get_transactions_response_dict = get_transactions_response_instance.to_dict()
# create an instance of GetTransactionsResponse from a dict
get_transactions_response_from_dict = GetTransactionsResponse.from_dict(get_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


