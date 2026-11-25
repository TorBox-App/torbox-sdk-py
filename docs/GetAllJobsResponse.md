# GetAllJobsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetSpecificJobResponseData]**](GetSpecificJobResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_all_jobs_response import GetAllJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllJobsResponse from a JSON string
get_all_jobs_response_instance = GetAllJobsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllJobsResponse.to_json())

# convert the object into a dict
get_all_jobs_response_dict = get_all_jobs_response_instance.to_dict()
# create an instance of GetAllJobsResponse from a dict
get_all_jobs_response_from_dict = GetAllJobsResponse.from_dict(get_all_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


