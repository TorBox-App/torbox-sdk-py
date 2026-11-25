# RequestDownloadBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[int]** | The files&#39;s ID that you want to download | [optional] [default to []]

## Example

```python
from torbox.models.request_download_batch import RequestDownloadBatch

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDownloadBatch from a JSON string
request_download_batch_instance = RequestDownloadBatch.from_json(json)
# print the JSON string representation of the object
print(RequestDownloadBatch.to_json())

# convert the object into a dict
request_download_batch_dict = request_download_batch_instance.to_dict()
# create an instance of RequestDownloadBatch from a dict
request_download_batch_from_dict = RequestDownloadBatch.from_dict(request_download_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


