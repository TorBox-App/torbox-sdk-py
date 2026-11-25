# GetSpecificJobResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**integration** | **str** |  | [optional] 
**file_id** | **int** |  | [optional] 
**zip** | **bool** |  | [optional] 
**progress** | **float** |  | [optional] 
**detail** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 

## Example

```python
from torbox.models.get_specific_job_response_data import GetSpecificJobResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpecificJobResponseData from a JSON string
get_specific_job_response_data_instance = GetSpecificJobResponseData.from_json(json)
# print the JSON string representation of the object
print(GetSpecificJobResponseData.to_json())

# convert the object into a dict
get_specific_job_response_data_dict = get_specific_job_response_data_instance.to_dict()
# create an instance of GetSpecificJobResponseData from a dict
get_specific_job_response_data_from_dict = GetSpecificJobResponseData.from_dict(get_specific_job_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


