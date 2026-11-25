# CreateTorrentResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | [optional] 
**torrent_id** | **int** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**queued_id** | **int** |  | [optional] 

## Example

```python
from torbox.models.create_torrent_response_data import CreateTorrentResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTorrentResponseData from a JSON string
create_torrent_response_data_instance = CreateTorrentResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateTorrentResponseData.to_json())

# convert the object into a dict
create_torrent_response_data_dict = create_torrent_response_data_instance.to_dict()
# create an instance of CreateTorrentResponseData from a dict
create_torrent_response_data_from_dict = CreateTorrentResponseData.from_dict(create_torrent_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


