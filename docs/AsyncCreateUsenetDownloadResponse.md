# AsyncCreateUsenetDownloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.async_create_usenet_download_response import AsyncCreateUsenetDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncCreateUsenetDownloadResponse from a JSON string
async_create_usenet_download_response_instance = AsyncCreateUsenetDownloadResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncCreateUsenetDownloadResponse.to_json())

# convert the object into a dict
async_create_usenet_download_response_dict = async_create_usenet_download_response_instance.to_dict()
# create an instance of AsyncCreateUsenetDownloadResponse from a dict
async_create_usenet_download_response_from_dict = AsyncCreateUsenetDownloadResponse.from_dict(async_create_usenet_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


