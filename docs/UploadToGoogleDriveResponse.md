# UploadToGoogleDriveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**UploadToGoogleDriveResponseData**](UploadToGoogleDriveResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.upload_to_google_drive_response import UploadToGoogleDriveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadToGoogleDriveResponse from a JSON string
upload_to_google_drive_response_instance = UploadToGoogleDriveResponse.from_json(json)
# print the JSON string representation of the object
print(UploadToGoogleDriveResponse.to_json())

# convert the object into a dict
upload_to_google_drive_response_dict = upload_to_google_drive_response_instance.to_dict()
# create an instance of UploadToGoogleDriveResponse from a dict
upload_to_google_drive_response_from_dict = UploadToGoogleDriveResponse.from_dict(upload_to_google_drive_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


