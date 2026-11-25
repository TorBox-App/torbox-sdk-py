# RefreshTokenSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_token** | **str** | you can get this by logging into https://torbox.app and finding the torbox_session_token in local storage | 

## Example

```python
from torbox.models.refresh_token_schema import RefreshTokenSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenSchema from a JSON string
refresh_token_schema_instance = RefreshTokenSchema.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenSchema.to_json())

# convert the object into a dict
refresh_token_schema_dict = refresh_token_schema_instance.to_dict()
# create an instance of RefreshTokenSchema from a dict
refresh_token_schema_from_dict = RefreshTokenSchema.from_dict(refresh_token_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


