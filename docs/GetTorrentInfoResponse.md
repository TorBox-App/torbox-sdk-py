# GetTorrentInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetTorrentInfoResponseData**](GetTorrentInfoResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_torrent_info_response import GetTorrentInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentInfoResponse from a JSON string
get_torrent_info_response_instance = GetTorrentInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetTorrentInfoResponse.to_json())

# convert the object into a dict
get_torrent_info_response_dict = get_torrent_info_response_instance.to_dict()
# create an instance of GetTorrentInfoResponse from a dict
get_torrent_info_response_from_dict = GetTorrentInfoResponse.from_dict(get_torrent_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


