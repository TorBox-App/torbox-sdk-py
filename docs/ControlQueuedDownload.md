# ControlQueuedDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | the operation you want to perform on the torrent | 
**queued_id** | **int** | the queued torrent&#39;s id, optional if using the \&quot;all\&quot; parameter | [optional] 
**all** | **bool** | if you want to do this operation to all queued torrents in your account, optional if using the \&quot;queued_id\&quot; parameter | [optional] [default to False]

## Example

```python
from torbox.models.control_queued_download import ControlQueuedDownload

# TODO update the JSON string below
json = "{}"
# create an instance of ControlQueuedDownload from a JSON string
control_queued_download_instance = ControlQueuedDownload.from_json(json)
# print the JSON string representation of the object
print(ControlQueuedDownload.to_json())

# convert the object into a dict
control_queued_download_dict = control_queued_download_instance.to_dict()
# create an instance of ControlQueuedDownload from a dict
control_queued_download_from_dict = ControlQueuedDownload.from_dict(control_queued_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


