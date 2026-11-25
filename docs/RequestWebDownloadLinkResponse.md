# RequestWebDownloadLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **str** |  | [optional] 

## Example

```python
from torbox.models.request_web_download_link_response import RequestWebDownloadLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestWebDownloadLinkResponse from a JSON string
request_web_download_link_response_instance = RequestWebDownloadLinkResponse.from_json(json)
# print the JSON string representation of the object
print(RequestWebDownloadLinkResponse.to_json())

# convert the object into a dict
request_web_download_link_response_dict = request_web_download_link_response_instance.to_dict()
# create an instance of RequestWebDownloadLinkResponse from a dict
request_web_download_link_response_from_dict = RequestWebDownloadLinkResponse.from_dict(request_web_download_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


