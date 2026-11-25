# DeleteAccountSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_token** | **str** | The user&#39;s session token from the website. It must belong to the same account as the API key. | 
**confirmation_code** | **int** | The confirmation code that was sent to the user&#39;s email by the Get Confirmation Code endpoint. | 

## Example

```python
from torbox.models.delete_account_schema import DeleteAccountSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAccountSchema from a JSON string
delete_account_schema_instance = DeleteAccountSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteAccountSchema.to_json())

# convert the object into a dict
delete_account_schema_dict = delete_account_schema_instance.to_dict()
# create an instance of DeleteAccountSchema from a dict
delete_account_schema_from_dict = DeleteAccountSchema.from_dict(delete_account_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


