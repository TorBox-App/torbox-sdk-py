# RequestUsenetDownloadLinksGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[RequestTorrentDownloadLinksGetResponseDataInner]**](RequestTorrentDownloadLinksGetResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.request_usenet_download_links_get_response import RequestUsenetDownloadLinksGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestUsenetDownloadLinksGetResponse from a JSON string
request_usenet_download_links_get_response_instance = RequestUsenetDownloadLinksGetResponse.from_json(json)
# print the JSON string representation of the object
print(RequestUsenetDownloadLinksGetResponse.to_json())

# convert the object into a dict
request_usenet_download_links_get_response_dict = request_usenet_download_links_get_response_instance.to_dict()
# create an instance of RequestUsenetDownloadLinksGetResponse from a dict
request_usenet_download_links_get_response_from_dict = RequestUsenetDownloadLinksGetResponse.from_dict(request_usenet_download_links_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


