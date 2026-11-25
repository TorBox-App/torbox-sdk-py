# GetSpecificJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetSpecificJobResponseData**](GetSpecificJobResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_specific_job_response import GetSpecificJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpecificJobResponse from a JSON string
get_specific_job_response_instance = GetSpecificJobResponse.from_json(json)
# print the JSON string representation of the object
print(GetSpecificJobResponse.to_json())

# convert the object into a dict
get_specific_job_response_dict = get_specific_job_response_instance.to_dict()
# create an instance of GetSpecificJobResponse from a dict
get_specific_job_response_from_dict = GetSpecificJobResponse.from_dict(get_specific_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


