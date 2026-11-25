# UploadTo1fichierResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**UploadToGoogleDriveResponseData**](UploadToGoogleDriveResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.upload_to1fichier_response import UploadTo1fichierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadTo1fichierResponse from a JSON string
upload_to1fichier_response_instance = UploadTo1fichierResponse.from_json(json)
# print the JSON string representation of the object
print(UploadTo1fichierResponse.to_json())

# convert the object into a dict
upload_to1fichier_response_dict = upload_to1fichier_response_instance.to_dict()
# create an instance of UploadTo1fichierResponse from a dict
upload_to1fichier_response_from_dict = UploadTo1fichierResponse.from_dict(upload_to1fichier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


