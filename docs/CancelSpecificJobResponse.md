# CancelSpecificJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.cancel_specific_job_response import CancelSpecificJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelSpecificJobResponse from a JSON string
cancel_specific_job_response_instance = CancelSpecificJobResponse.from_json(json)
# print the JSON string representation of the object
print(CancelSpecificJobResponse.to_json())

# convert the object into a dict
cancel_specific_job_response_dict = cancel_specific_job_response_instance.to_dict()
# create an instance of CancelSpecificJobResponse from a dict
cancel_specific_job_response_from_dict = CancelSpecificJobResponse.from_dict(cancel_specific_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


