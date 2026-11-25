# EditTorrentItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.edit_torrent_item_response import EditTorrentItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditTorrentItemResponse from a JSON string
edit_torrent_item_response_instance = EditTorrentItemResponse.from_json(json)
# print the JSON string representation of the object
print(EditTorrentItemResponse.to_json())

# convert the object into a dict
edit_torrent_item_response_dict = edit_torrent_item_response_instance.to_dict()
# create an instance of EditTorrentItemResponse from a dict
edit_torrent_item_response_from_dict = EditTorrentItemResponse.from_dict(edit_torrent_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


