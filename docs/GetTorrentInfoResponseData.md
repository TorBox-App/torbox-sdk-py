# GetTorrentInfoResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**trackers** | **List[str]** |  | [optional] 
**seeds** | **int** |  | [optional] 
**peers** | **int** |  | [optional] 
**files** | [**List[GetTorrentInfoResponseDataFilesInner]**](GetTorrentInfoResponseDataFilesInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_torrent_info_response_data import GetTorrentInfoResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentInfoResponseData from a JSON string
get_torrent_info_response_data_instance = GetTorrentInfoResponseData.from_json(json)
# print the JSON string representation of the object
print(GetTorrentInfoResponseData.to_json())

# convert the object into a dict
get_torrent_info_response_data_dict = get_torrent_info_response_data_instance.to_dict()
# create an instance of GetTorrentInfoResponseData from a dict
get_torrent_info_response_data_from_dict = GetTorrentInfoResponseData.from_dict(get_torrent_info_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


