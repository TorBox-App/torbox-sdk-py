# ExportTorrentDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **str** |  | [optional] 

## Example

```python
from torbox.models.export_torrent_data_response import ExportTorrentDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportTorrentDataResponse from a JSON string
export_torrent_data_response_instance = ExportTorrentDataResponse.from_json(json)
# print the JSON string representation of the object
print(ExportTorrentDataResponse.to_json())

# convert the object into a dict
export_torrent_data_response_dict = export_torrent_data_response_instance.to_dict()
# create an instance of ExportTorrentDataResponse from a dict
export_torrent_data_response_from_dict = ExportTorrentDataResponse.from_dict(export_torrent_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


