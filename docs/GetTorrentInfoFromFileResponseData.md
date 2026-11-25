# GetTorrentInfoFromFileResponseData


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
from torbox.models.get_torrent_info_from_file_response_data import GetTorrentInfoFromFileResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentInfoFromFileResponseData from a JSON string
get_torrent_info_from_file_response_data_instance = GetTorrentInfoFromFileResponseData.from_json(json)
# print the JSON string representation of the object
print(GetTorrentInfoFromFileResponseData.to_json())

# convert the object into a dict
get_torrent_info_from_file_response_data_dict = get_torrent_info_from_file_response_data_instance.to_dict()
# create an instance of GetTorrentInfoFromFileResponseData from a dict
get_torrent_info_from_file_response_data_from_dict = GetTorrentInfoFromFileResponseData.from_dict(get_torrent_info_from_file_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


