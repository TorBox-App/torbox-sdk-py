# CreateWebDownloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**CreateWebDownloadResponseData**](CreateWebDownloadResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.create_web_download_response import CreateWebDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebDownloadResponse from a JSON string
create_web_download_response_instance = CreateWebDownloadResponse.from_json(json)
# print the JSON string representation of the object
print(CreateWebDownloadResponse.to_json())

# convert the object into a dict
create_web_download_response_dict = create_web_download_response_instance.to_dict()
# create an instance of CreateWebDownloadResponse from a dict
create_web_download_response_from_dict = CreateWebDownloadResponse.from_dict(create_web_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


