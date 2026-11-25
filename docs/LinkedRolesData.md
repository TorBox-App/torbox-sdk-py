# LinkedRolesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discord_token** | **str** | Discord OAuth access token of the user. It is issued by Discord, not by TorBox. Required. | 

## Example

```python
from torbox.models.linked_roles_data import LinkedRolesData

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedRolesData from a JSON string
linked_roles_data_instance = LinkedRolesData.from_json(json)
# print the JSON string representation of the object
print(LinkedRolesData.to_json())

# convert the object into a dict
linked_roles_data_dict = linked_roles_data_instance.to_dict()
# create an instance of LinkedRolesData from a dict
linked_roles_data_from_dict = LinkedRolesData.from_dict(linked_roles_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


