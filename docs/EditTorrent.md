# EditTorrent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**torrent_id** | **int** |  | 
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**alternative_hashes** | **List[str]** |  | [optional] 
**airlocked** | **bool** |  | [optional] 

## Example

```python
from torbox.models.edit_torrent import EditTorrent

# TODO update the JSON string below
json = "{}"
# create an instance of EditTorrent from a JSON string
edit_torrent_instance = EditTorrent.from_json(json)
# print the JSON string representation of the object
print(EditTorrent.to_json())

# convert the object into a dict
edit_torrent_dict = edit_torrent_instance.to_dict()
# create an instance of EditTorrent from a dict
edit_torrent_from_dict = EditTorrent.from_dict(edit_torrent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


