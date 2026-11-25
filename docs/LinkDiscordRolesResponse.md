# LinkDiscordRolesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.link_discord_roles_response import LinkDiscordRolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkDiscordRolesResponse from a JSON string
link_discord_roles_response_instance = LinkDiscordRolesResponse.from_json(json)
# print the JSON string representation of the object
print(LinkDiscordRolesResponse.to_json())

# convert the object into a dict
link_discord_roles_response_dict = link_discord_roles_response_instance.to_dict()
# create an instance of LinkDiscordRolesResponse from a dict
link_discord_roles_response_from_dict = LinkDiscordRolesResponse.from_dict(link_discord_roles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


