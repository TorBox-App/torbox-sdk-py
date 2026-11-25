# GetTorrentListResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**server** | **float** |  | [optional] 
**hash** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**magnet** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**download_state** | **str** |  | [optional] 
**seeds** | **int** |  | [optional] 
**peers** | **int** |  | [optional] 
**ratio** | **float** |  | [optional] 
**progress** | **float** |  | [optional] 
**download_speed** | **float** |  | [optional] 
**upload_speed** | **float** |  | [optional] 
**eta** | **float** |  | [optional] 
**torrent_file** | **bool** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**download_present** | **bool** |  | [optional] 
**files** | [**List[GetTorrentListResponseDataInnerFilesInner]**](GetTorrentListResponseDataInnerFilesInner.md) |  | [optional] 
**download_path** | **str** |  | [optional] 
**availability** | **float** |  | [optional] 
**download_finished** | **bool** |  | [optional] 
**tracker** | **str** |  | [optional] 
**total_uploaded** | **int** |  | [optional] 
**total_downloaded** | **int** |  | [optional] 
**cached** | **bool** |  | [optional] 
**owner** | **str** |  | [optional] 
**seed_torrent** | **bool** |  | [optional] 
**allow_zipped** | **bool** |  | [optional] 
**long_term_seeding** | **bool** |  | [optional] 
**tracker_message** | **str** |  | [optional] 
**cached_at** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**alternative_hashes** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**airlocked** | **bool** |  | [optional] 

## Example

```python
from torbox.models.get_torrent_list_response_data_inner import GetTorrentListResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentListResponseDataInner from a JSON string
get_torrent_list_response_data_inner_instance = GetTorrentListResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetTorrentListResponseDataInner.to_json())

# convert the object into a dict
get_torrent_list_response_data_inner_dict = get_torrent_list_response_data_inner_instance.to_dict()
# create an instance of GetTorrentListResponseDataInner from a dict
get_torrent_list_response_data_inner_from_dict = GetTorrentListResponseDataInner.from_dict(get_torrent_list_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


