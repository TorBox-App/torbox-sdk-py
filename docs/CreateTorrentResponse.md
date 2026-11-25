# CreateTorrentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**CreateTorrentResponseData**](CreateTorrentResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.create_torrent_response import CreateTorrentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTorrentResponse from a JSON string
create_torrent_response_instance = CreateTorrentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTorrentResponse.to_json())

# convert the object into a dict
create_torrent_response_dict = create_torrent_response_instance.to_dict()
# create an instance of CreateTorrentResponse from a dict
create_torrent_response_from_dict = CreateTorrentResponse.from_dict(create_torrent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


