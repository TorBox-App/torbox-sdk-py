# RequestWebDownloadLinksPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[RequestTorrentDownloadLinksGetResponseDataInner]**](RequestTorrentDownloadLinksGetResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.request_web_download_links_post_response import RequestWebDownloadLinksPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestWebDownloadLinksPostResponse from a JSON string
request_web_download_links_post_response_instance = RequestWebDownloadLinksPostResponse.from_json(json)
# print the JSON string representation of the object
print(RequestWebDownloadLinksPostResponse.to_json())

# convert the object into a dict
request_web_download_links_post_response_dict = request_web_download_links_post_response_instance.to_dict()
# create an instance of RequestWebDownloadLinksPostResponse from a dict
request_web_download_links_post_response_from_dict = RequestWebDownloadLinksPostResponse.from_dict(request_web_download_links_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


