# ControlTorrentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.control_torrent_response import ControlTorrentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTorrentResponse from a JSON string
control_torrent_response_instance = ControlTorrentResponse.from_json(json)
# print the JSON string representation of the object
print(ControlTorrentResponse.to_json())

# convert the object into a dict
control_torrent_response_dict = control_torrent_response_instance.to_dict()
# create an instance of ControlTorrentResponse from a dict
control_torrent_response_from_dict = ControlTorrentResponse.from_dict(control_torrent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


