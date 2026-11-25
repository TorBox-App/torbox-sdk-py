# GetAllJobsByHashResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetSpecificJobResponseData]**](GetSpecificJobResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_all_jobs_by_hash_response import GetAllJobsByHashResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllJobsByHashResponse from a JSON string
get_all_jobs_by_hash_response_instance = GetAllJobsByHashResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllJobsByHashResponse.to_json())

# convert the object into a dict
get_all_jobs_by_hash_response_dict = get_all_jobs_by_hash_response_instance.to_dict()
# create an instance of GetAllJobsByHashResponse from a dict
get_all_jobs_by_hash_response_from_dict = GetAllJobsByHashResponse.from_dict(get_all_jobs_by_hash_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


