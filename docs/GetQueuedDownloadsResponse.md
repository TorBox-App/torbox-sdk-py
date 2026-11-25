# GetQueuedDownloadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetQueuedDownloadsResponseDataInner]**](GetQueuedDownloadsResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_queued_downloads_response import GetQueuedDownloadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetQueuedDownloadsResponse from a JSON string
get_queued_downloads_response_instance = GetQueuedDownloadsResponse.from_json(json)
# print the JSON string representation of the object
print(GetQueuedDownloadsResponse.to_json())

# convert the object into a dict
get_queued_downloads_response_dict = get_queued_downloads_response_instance.to_dict()
# create an instance of GetQueuedDownloadsResponse from a dict
get_queued_downloads_response_from_dict = GetQueuedDownloadsResponse.from_dict(get_queued_downloads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


