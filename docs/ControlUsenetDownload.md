# ControlUsenetDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | the operation you want to perform on the usenet download. Can be \&quot;delete\&quot;, \&quot;pause\&quot; or \&quot;resume\&quot;. | 
**usenet_id** | **int** | the usenet download&#39;s id, optional if using the \&quot;all\&quot; parameter. | [optional] 
**all** | **bool** | if you want to do this operation to all usenet downloads in your account, optional if using the \&quot;usenet_id\&quot; parameter | [optional] [default to False]

## Example

```python
from torbox.models.control_usenet_download import ControlUsenetDownload

# TODO update the JSON string below
json = "{}"
# create an instance of ControlUsenetDownload from a JSON string
control_usenet_download_instance = ControlUsenetDownload.from_json(json)
# print the JSON string representation of the object
print(ControlUsenetDownload.to_json())

# convert the object into a dict
control_usenet_download_dict = control_usenet_download_instance.to_dict()
# create an instance of ControlUsenetDownload from a dict
control_usenet_download_from_dict = ControlUsenetDownload.from_dict(control_usenet_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


