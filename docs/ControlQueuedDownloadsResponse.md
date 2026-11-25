# ControlQueuedDownloadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.control_queued_downloads_response import ControlQueuedDownloadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ControlQueuedDownloadsResponse from a JSON string
control_queued_downloads_response_instance = ControlQueuedDownloadsResponse.from_json(json)
# print the JSON string representation of the object
print(ControlQueuedDownloadsResponse.to_json())

# convert the object into a dict
control_queued_downloads_response_dict = control_queued_downloads_response_instance.to_dict()
# create an instance of ControlQueuedDownloadsResponse from a dict
control_queued_downloads_response_from_dict = ControlQueuedDownloadsResponse.from_dict(control_queued_downloads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


