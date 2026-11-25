# RequestUsenetDownloadLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **str** |  | [optional] 

## Example

```python
from torbox.models.request_usenet_download_link_response import RequestUsenetDownloadLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestUsenetDownloadLinkResponse from a JSON string
request_usenet_download_link_response_instance = RequestUsenetDownloadLinkResponse.from_json(json)
# print the JSON string representation of the object
print(RequestUsenetDownloadLinkResponse.to_json())

# convert the object into a dict
request_usenet_download_link_response_dict = request_usenet_download_link_response_instance.to_dict()
# create an instance of RequestUsenetDownloadLinkResponse from a dict
request_usenet_download_link_response_from_dict = RequestUsenetDownloadLinkResponse.from_dict(request_usenet_download_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


