# DeviceTokenSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** |  | 

## Example

```python
from torbox.models.device_token_schema import DeviceTokenSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceTokenSchema from a JSON string
device_token_schema_instance = DeviceTokenSchema.from_json(json)
# print the JSON string representation of the object
print(DeviceTokenSchema.to_json())

# convert the object into a dict
device_token_schema_dict = device_token_schema_instance.to_dict()
# create an instance of DeviceTokenSchema from a dict
device_token_schema_from_dict = DeviceTokenSchema.from_dict(device_token_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


