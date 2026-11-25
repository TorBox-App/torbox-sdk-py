# CreateUsenetDownloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**CreateUsenetDownloadResponseData**](CreateUsenetDownloadResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.create_usenet_download_response import CreateUsenetDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsenetDownloadResponse from a JSON string
create_usenet_download_response_instance = CreateUsenetDownloadResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUsenetDownloadResponse.to_json())

# convert the object into a dict
create_usenet_download_response_dict = create_usenet_download_response_instance.to_dict()
# create an instance of CreateUsenetDownloadResponse from a dict
create_usenet_download_response_from_dict = CreateUsenetDownloadResponse.from_dict(create_usenet_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


