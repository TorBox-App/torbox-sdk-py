# AddToDropbox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the torrent, usenet download or web download. Still required by the route, but no longer used. | 
**file_id** | **int** | Id of the file inside the download. No longer used. | [optional] 
**zip** | **bool** | Whether to upload the whole download as one zip. No longer used. | [optional] [default to False]
**type** | **str** | Which kind of download &#x60;id&#x60; refers to. One of &#x60;torrent&#x60;, &#x60;usenet&#x60; or &#x60;webdownload&#x60;. Optional, default &#x60;torrent&#x60;. Still checked before the route answers. | [optional] [default to 'torrent']
**dropbox_token** | **str** | Dropbox OAuth access token. Still required by the route, but no longer used. | 

## Example

```python
from torbox.models.add_to_dropbox import AddToDropbox

# TODO update the JSON string below
json = "{}"
# create an instance of AddToDropbox from a JSON string
add_to_dropbox_instance = AddToDropbox.from_json(json)
# print the JSON string representation of the object
print(AddToDropbox.to_json())

# convert the object into a dict
add_to_dropbox_dict = add_to_dropbox_instance.to_dict()
# create an instance of AddToDropbox from a dict
add_to_dropbox_from_dict = AddToDropbox.from_dict(add_to_dropbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


