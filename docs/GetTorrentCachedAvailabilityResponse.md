# GetTorrentCachedAvailabilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.get_torrent_cached_availability_response import GetTorrentCachedAvailabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentCachedAvailabilityResponse from a JSON string
get_torrent_cached_availability_response_instance = GetTorrentCachedAvailabilityResponse.from_json(json)
# print the JSON string representation of the object
print(GetTorrentCachedAvailabilityResponse.to_json())

# convert the object into a dict
get_torrent_cached_availability_response_dict = get_torrent_cached_availability_response_instance.to_dict()
# create an instance of GetTorrentCachedAvailabilityResponse from a dict
get_torrent_cached_availability_response_from_dict = GetTorrentCachedAvailabilityResponse.from_dict(get_torrent_cached_availability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


