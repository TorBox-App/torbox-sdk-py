# CreateWebDownloadResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | [optional] 
**webdownload_id** | **int** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**jdownloader_id** | **object** |  | [optional] 
**link_list** | **List[str]** |  | [optional] 

## Example

```python
from torbox.models.create_web_download_response_data import CreateWebDownloadResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebDownloadResponseData from a JSON string
create_web_download_response_data_instance = CreateWebDownloadResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateWebDownloadResponseData.to_json())

# convert the object into a dict
create_web_download_response_data_dict = create_web_download_response_data_instance.to_dict()
# create an instance of CreateWebDownloadResponseData from a dict
create_web_download_response_data_from_dict = CreateWebDownloadResponseData.from_dict(create_web_download_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


