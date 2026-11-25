# CreateUsenetDownloadResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | [optional] 
**usenetdownload_id** | **int** |  | [optional] 
**auth_id** | **str** |  | [optional] 

## Example

```python
from torbox.models.create_usenet_download_response_data import CreateUsenetDownloadResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsenetDownloadResponseData from a JSON string
create_usenet_download_response_data_instance = CreateUsenetDownloadResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateUsenetDownloadResponseData.to_json())

# convert the object into a dict
create_usenet_download_response_data_dict = create_usenet_download_response_data_instance.to_dict()
# create an instance of CreateUsenetDownloadResponseData from a dict
create_usenet_download_response_data_from_dict = CreateUsenetDownloadResponseData.from_dict(create_usenet_download_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


