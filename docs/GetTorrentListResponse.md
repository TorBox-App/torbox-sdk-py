# GetTorrentListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetTorrentListResponseDataInner]**](GetTorrentListResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_torrent_list_response import GetTorrentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentListResponse from a JSON string
get_torrent_list_response_instance = GetTorrentListResponse.from_json(json)
# print the JSON string representation of the object
print(GetTorrentListResponse.to_json())

# convert the object into a dict
get_torrent_list_response_dict = get_torrent_list_response_instance.to_dict()
# create an instance of GetTorrentListResponse from a dict
get_torrent_list_response_from_dict = GetTorrentListResponse.from_dict(get_torrent_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


