# AddToGoogleDrive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the torrent, usenet download or web download to upload. It has to be one of your own downloads. Required. | 
**file_id** | **int** | Id of the file to upload, from the download&#39;s files. Leave out when &#x60;zip&#x60; is true. | [optional] 
**zip** | **bool** | Upload the whole download as one zip instead of a single file. Takes precedence over &#x60;file_id&#x60;. Optional, default false. | [optional] [default to False]
**type** | **str** | Which kind of download &#x60;id&#x60; refers to. One of &#x60;torrent&#x60;, &#x60;usenet&#x60; or &#x60;webdownload&#x60;. Optional, default &#x60;torrent&#x60;. | [optional] [default to 'torrent']
**google_token** | **str** | Google OAuth access token for the Drive to upload to. It is issued by Google, not by TorBox. Required. | 

## Example

```python
from torbox.models.add_to_google_drive import AddToGoogleDrive

# TODO update the JSON string below
json = "{}"
# create an instance of AddToGoogleDrive from a JSON string
add_to_google_drive_instance = AddToGoogleDrive.from_json(json)
# print the JSON string representation of the object
print(AddToGoogleDrive.to_json())

# convert the object into a dict
add_to_google_drive_dict = add_to_google_drive_instance.to_dict()
# create an instance of AddToGoogleDrive from a dict
add_to_google_drive_from_dict = AddToGoogleDrive.from_dict(add_to_google_drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


