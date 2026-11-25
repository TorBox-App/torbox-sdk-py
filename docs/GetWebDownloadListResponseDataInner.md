# GetWebDownloadListResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**download_state** | **str** |  | [optional] 
**download_speed** | **float** |  | [optional] 
**original_url** | **str** |  | [optional] 
**eta** | **float** |  | [optional] 
**progress** | **float** |  | [optional] 
**size** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 
**files** | [**List[GetTorrentListResponseDataInnerFilesInner]**](GetTorrentListResponseDataInnerFilesInner.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**cached** | **bool** |  | [optional] 
**download_present** | **bool** |  | [optional] 
**download_finished** | **bool** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**cached_at** | **str** |  | [optional] 
**server** | **float** |  | [optional] 
**alternative_hashes** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**airlocked** | **bool** |  | [optional] 

## Example

```python
from torbox.models.get_web_download_list_response_data_inner import GetWebDownloadListResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebDownloadListResponseDataInner from a JSON string
get_web_download_list_response_data_inner_instance = GetWebDownloadListResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetWebDownloadListResponseDataInner.to_json())

# convert the object into a dict
get_web_download_list_response_data_inner_dict = get_web_download_list_response_data_inner_instance.to_dict()
# create an instance of GetWebDownloadListResponseDataInner from a dict
get_web_download_list_response_data_inner_from_dict = GetWebDownloadListResponseDataInner.from_dict(get_web_download_list_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


