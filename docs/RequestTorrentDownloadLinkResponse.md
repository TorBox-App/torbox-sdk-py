# RequestTorrentDownloadLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **str** |  | [optional] 

## Example

```python
from torbox.models.request_torrent_download_link_response import RequestTorrentDownloadLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTorrentDownloadLinkResponse from a JSON string
request_torrent_download_link_response_instance = RequestTorrentDownloadLinkResponse.from_json(json)
# print the JSON string representation of the object
print(RequestTorrentDownloadLinkResponse.to_json())

# convert the object into a dict
request_torrent_download_link_response_dict = request_torrent_download_link_response_instance.to_dict()
# create an instance of RequestTorrentDownloadLinkResponse from a dict
request_torrent_download_link_response_from_dict = RequestTorrentDownloadLinkResponse.from_dict(request_torrent_download_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


