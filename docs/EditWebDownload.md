# EditWebDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webdl_id** | **int** |  | 
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**alternative_hashes** | **List[str]** |  | [optional] 
**airlocked** | **bool** |  | [optional] 

## Example

```python
from torbox.models.edit_web_download import EditWebDownload

# TODO update the JSON string below
json = "{}"
# create an instance of EditWebDownload from a JSON string
edit_web_download_instance = EditWebDownload.from_json(json)
# print the JSON string representation of the object
print(EditWebDownload.to_json())

# convert the object into a dict
edit_web_download_dict = edit_web_download_instance.to_dict()
# create an instance of EditWebDownload from a dict
edit_web_download_from_dict = EditWebDownload.from_dict(edit_web_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


