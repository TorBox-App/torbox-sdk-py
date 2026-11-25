# ControlWebDownloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.control_web_download_response import ControlWebDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ControlWebDownloadResponse from a JSON string
control_web_download_response_instance = ControlWebDownloadResponse.from_json(json)
# print the JSON string representation of the object
print(ControlWebDownloadResponse.to_json())

# convert the object into a dict
control_web_download_response_dict = control_web_download_response_instance.to_dict()
# create an instance of ControlWebDownloadResponse from a dict
control_web_download_response_from_dict = ControlWebDownloadResponse.from_dict(control_web_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


