# GetTransactionsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_transactions_response_data_inner import GetTransactionsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsResponseDataInner from a JSON string
get_transactions_response_data_inner_instance = GetTransactionsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsResponseDataInner.to_json())

# convert the object into a dict
get_transactions_response_data_inner_dict = get_transactions_response_data_inner_instance.to_dict()
# create an instance of GetTransactionsResponseDataInner from a dict
get_transactions_response_data_inner_from_dict = GetTransactionsResponseDataInner.from_dict(get_transactions_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


