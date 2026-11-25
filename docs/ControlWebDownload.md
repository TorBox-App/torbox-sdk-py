# ControlWebDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | the operation you want to perform on the web download. Can be \&quot;delete\&quot;. | 
**webdl_id** | **int** | the web download&#39;s id, optional if using the \&quot;all\&quot; parameter. | [optional] 
**all** | **bool** | if you want to do this operation to all web downloads in your account, optional if using the \&quot;webdl_id\&quot; parameter | [optional] [default to False]

## Example

```python
from torbox.models.control_web_download import ControlWebDownload

# TODO update the JSON string below
json = "{}"
# create an instance of ControlWebDownload from a JSON string
control_web_download_instance = ControlWebDownload.from_json(json)
# print the JSON string representation of the object
print(ControlWebDownload.to_json())

# convert the object into a dict
control_web_download_dict = control_web_download_instance.to_dict()
# create an instance of ControlWebDownload from a dict
control_web_download_from_dict = ControlWebDownload.from_dict(control_web_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


