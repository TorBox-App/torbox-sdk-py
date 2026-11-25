# GetWebDownloadListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetWebDownloadListResponseDataInner]**](GetWebDownloadListResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_web_download_list_response import GetWebDownloadListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebDownloadListResponse from a JSON string
get_web_download_list_response_instance = GetWebDownloadListResponse.from_json(json)
# print the JSON string representation of the object
print(GetWebDownloadListResponse.to_json())

# convert the object into a dict
get_web_download_list_response_dict = get_web_download_list_response_instance.to_dict()
# create an instance of GetWebDownloadListResponse from a dict
get_web_download_list_response_from_dict = GetWebDownloadListResponse.from_dict(get_web_download_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


