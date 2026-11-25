# GetTorrentInfoFromFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetTorrentInfoFromFileResponseData**](GetTorrentInfoFromFileResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_torrent_info_from_file_response import GetTorrentInfoFromFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentInfoFromFileResponse from a JSON string
get_torrent_info_from_file_response_instance = GetTorrentInfoFromFileResponse.from_json(json)
# print the JSON string representation of the object
print(GetTorrentInfoFromFileResponse.to_json())

# convert the object into a dict
get_torrent_info_from_file_response_dict = get_torrent_info_from_file_response_instance.to_dict()
# create an instance of GetTorrentInfoFromFileResponse from a dict
get_torrent_info_from_file_response_from_dict = GetTorrentInfoFromFileResponse.from_dict(get_torrent_info_from_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


