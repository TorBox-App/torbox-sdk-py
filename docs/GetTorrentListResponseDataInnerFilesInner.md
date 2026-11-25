# GetTorrentListResponseDataInnerFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**md5** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**zipped** | **bool** |  | [optional] 
**s3_path** | **str** |  | [optional] 
**infected** | **bool** |  | [optional] 
**mimetype** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**absolute_path** | **str** |  | [optional] 
**opensubtitles_hash** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_torrent_list_response_data_inner_files_inner import GetTorrentListResponseDataInnerFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentListResponseDataInnerFilesInner from a JSON string
get_torrent_list_response_data_inner_files_inner_instance = GetTorrentListResponseDataInnerFilesInner.from_json(json)
# print the JSON string representation of the object
print(GetTorrentListResponseDataInnerFilesInner.to_json())

# convert the object into a dict
get_torrent_list_response_data_inner_files_inner_dict = get_torrent_list_response_data_inner_files_inner_instance.to_dict()
# create an instance of GetTorrentListResponseDataInnerFilesInner from a dict
get_torrent_list_response_data_inner_files_inner_from_dict = GetTorrentListResponseDataInnerFilesInner.from_dict(get_torrent_list_response_data_inner_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


