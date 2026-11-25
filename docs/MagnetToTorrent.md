# MagnetToTorrent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**magnet** | **str** |  | 

## Example

```python
from torbox.models.magnet_to_torrent import MagnetToTorrent

# TODO update the JSON string below
json = "{}"
# create an instance of MagnetToTorrent from a JSON string
magnet_to_torrent_instance = MagnetToTorrent.from_json(json)
# print the JSON string representation of the object
print(MagnetToTorrent.to_json())

# convert the object into a dict
magnet_to_torrent_dict = magnet_to_torrent_instance.to_dict()
# create an instance of MagnetToTorrent from a dict
magnet_to_torrent_from_dict = MagnetToTorrent.from_dict(magnet_to_torrent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


