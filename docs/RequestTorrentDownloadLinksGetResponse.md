# RequestTorrentDownloadLinksGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[RequestTorrentDownloadLinksGetResponseDataInner]**](RequestTorrentDownloadLinksGetResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.request_torrent_download_links_get_response import RequestTorrentDownloadLinksGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTorrentDownloadLinksGetResponse from a JSON string
request_torrent_download_links_get_response_instance = RequestTorrentDownloadLinksGetResponse.from_json(json)
# print the JSON string representation of the object
print(RequestTorrentDownloadLinksGetResponse.to_json())

# convert the object into a dict
request_torrent_download_links_get_response_dict = request_torrent_download_links_get_response_instance.to_dict()
# create an instance of RequestTorrentDownloadLinksGetResponse from a dict
request_torrent_download_links_get_response_from_dict = RequestTorrentDownloadLinksGetResponse.from_dict(request_torrent_download_links_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


