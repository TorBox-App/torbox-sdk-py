# GetTorrentInfoResponseDataFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from torbox.models.get_torrent_info_response_data_files_inner import GetTorrentInfoResponseDataFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentInfoResponseDataFilesInner from a JSON string
get_torrent_info_response_data_files_inner_instance = GetTorrentInfoResponseDataFilesInner.from_json(json)
# print the JSON string representation of the object
print(GetTorrentInfoResponseDataFilesInner.to_json())

# convert the object into a dict
get_torrent_info_response_data_files_inner_dict = get_torrent_info_response_data_files_inner_instance.to_dict()
# create an instance of GetTorrentInfoResponseDataFilesInner from a dict
get_torrent_info_response_data_files_inner_from_dict = GetTorrentInfoResponseDataFilesInner.from_dict(get_torrent_info_response_data_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


