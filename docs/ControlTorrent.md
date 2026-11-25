# ControlTorrent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | the operation you want to perform on the torrent | 
**torrent_id** | **int** | the torrent&#39;s id, optional if using \&quot;all\&quot; parameter | [optional] 
**all** | **bool** | if you want to do this operation to all torrents in your account, optional if using the \&quot;torrent_id\&quot; parameter | [optional] [default to False]

## Example

```python
from torbox.models.control_torrent import ControlTorrent

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTorrent from a JSON string
control_torrent_instance = ControlTorrent.from_json(json)
# print the JSON string representation of the object
print(ControlTorrent.to_json())

# convert the object into a dict
control_torrent_dict = control_torrent_instance.to_dict()
# create an instance of ControlTorrent from a dict
control_torrent_from_dict = ControlTorrent.from_dict(control_torrent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


