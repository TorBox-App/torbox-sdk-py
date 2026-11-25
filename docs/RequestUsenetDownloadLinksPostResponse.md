# RequestUsenetDownloadLinksPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[RequestTorrentDownloadLinksGetResponseDataInner]**](RequestTorrentDownloadLinksGetResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.request_usenet_download_links_post_response import RequestUsenetDownloadLinksPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestUsenetDownloadLinksPostResponse from a JSON string
request_usenet_download_links_post_response_instance = RequestUsenetDownloadLinksPostResponse.from_json(json)
# print the JSON string representation of the object
print(RequestUsenetDownloadLinksPostResponse.to_json())

# convert the object into a dict
request_usenet_download_links_post_response_dict = request_usenet_download_links_post_response_instance.to_dict()
# create an instance of RequestUsenetDownloadLinksPostResponse from a dict
request_usenet_download_links_post_response_from_dict = RequestUsenetDownloadLinksPostResponse.from_dict(request_usenet_download_links_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


