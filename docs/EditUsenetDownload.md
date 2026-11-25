# EditUsenetDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usenet_download_id** | **int** |  | 
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**alternative_hashes** | **List[str]** |  | [optional] 
**airlocked** | **bool** |  | [optional] 

## Example

```python
from torbox.models.edit_usenet_download import EditUsenetDownload

# TODO update the JSON string below
json = "{}"
# create an instance of EditUsenetDownload from a JSON string
edit_usenet_download_instance = EditUsenetDownload.from_json(json)
# print the JSON string representation of the object
print(EditUsenetDownload.to_json())

# convert the object into a dict
edit_usenet_download_dict = edit_usenet_download_instance.to_dict()
# create an instance of EditUsenetDownload from a dict
edit_usenet_download_from_dict = EditUsenetDownload.from_dict(edit_usenet_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


