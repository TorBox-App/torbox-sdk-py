# GetQueuedDownloadsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**magnet** | **str** |  | [optional] 
**torrent_file** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name_override** | **str** |  | [optional] 
**seed_torrent_override** | **int** |  | [optional] 

## Example

```python
from torbox.models.get_queued_downloads_response_data_inner import GetQueuedDownloadsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetQueuedDownloadsResponseDataInner from a JSON string
get_queued_downloads_response_data_inner_instance = GetQueuedDownloadsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetQueuedDownloadsResponseDataInner.to_json())

# convert the object into a dict
get_queued_downloads_response_data_inner_dict = get_queued_downloads_response_data_inner_instance.to_dict()
# create an instance of GetQueuedDownloadsResponseDataInner from a dict
get_queued_downloads_response_data_inner_from_dict = GetQueuedDownloadsResponseDataInner.from_dict(get_queued_downloads_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


