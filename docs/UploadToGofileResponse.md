# UploadToGofileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**UploadToGoogleDriveResponseData**](UploadToGoogleDriveResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.upload_to_gofile_response import UploadToGofileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadToGofileResponse from a JSON string
upload_to_gofile_response_instance = UploadToGofileResponse.from_json(json)
# print the JSON string representation of the object
print(UploadToGofileResponse.to_json())

# convert the object into a dict
upload_to_gofile_response_dict = upload_to_gofile_response_instance.to_dict()
# create an instance of UploadToGofileResponse from a dict
upload_to_gofile_response_from_dict = UploadToGofileResponse.from_dict(upload_to_gofile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


