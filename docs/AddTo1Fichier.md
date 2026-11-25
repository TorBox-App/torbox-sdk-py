# AddTo1Fichier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the torrent, usenet download or web download to upload. It has to be one of your own downloads. Required. | 
**file_id** | **int** | Id of the file to upload, from the download&#39;s files. Leave out when &#x60;zip&#x60; is true. | [optional] 
**zip** | **bool** | Upload the whole download as one zip instead of a single file. Takes precedence over &#x60;file_id&#x60;. Optional, default false. | [optional] [default to False]
**type** | **str** | Which kind of download &#x60;id&#x60; refers to. One of &#x60;torrent&#x60;, &#x60;usenet&#x60; or &#x60;webdownload&#x60;. Optional, default &#x60;torrent&#x60;. | [optional] [default to 'torrent']
**onefichier_token** | **str** | 1Fichier API token of the account to upload to. It is issued by 1Fichier, not by TorBox. Optional. | [optional] 

## Example

```python
from torbox.models.add_to1_fichier import AddTo1Fichier

# TODO update the JSON string below
json = "{}"
# create an instance of AddTo1Fichier from a JSON string
add_to1_fichier_instance = AddTo1Fichier.from_json(json)
# print the JSON string representation of the object
print(AddTo1Fichier.to_json())

# convert the object into a dict
add_to1_fichier_dict = add_to1_fichier_instance.to_dict()
# create an instance of AddTo1Fichier from a dict
add_to1_fichier_from_dict = AddTo1Fichier.from_dict(add_to1_fichier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


