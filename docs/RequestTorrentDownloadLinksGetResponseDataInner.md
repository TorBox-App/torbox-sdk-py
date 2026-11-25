# RequestTorrentDownloadLinksGetResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**error** | **object** |  | [optional] 

## Example

```python
from torbox.models.request_torrent_download_links_get_response_data_inner import RequestTorrentDownloadLinksGetResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTorrentDownloadLinksGetResponseDataInner from a JSON string
request_torrent_download_links_get_response_data_inner_instance = RequestTorrentDownloadLinksGetResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(RequestTorrentDownloadLinksGetResponseDataInner.to_json())

# convert the object into a dict
request_torrent_download_links_get_response_data_inner_dict = request_torrent_download_links_get_response_data_inner_instance.to_dict()
# create an instance of RequestTorrentDownloadLinksGetResponseDataInner from a dict
request_torrent_download_links_get_response_data_inner_from_dict = RequestTorrentDownloadLinksGetResponseDataInner.from_dict(request_torrent_download_links_get_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


