# GetSpeedtestFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetSpeedtestFilesResponseDataInner]**](GetSpeedtestFilesResponseDataInner.md) |  | [optional] 

## Example

```python
from torbox.models.get_speedtest_files_response import GetSpeedtestFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpeedtestFilesResponse from a JSON string
get_speedtest_files_response_instance = GetSpeedtestFilesResponse.from_json(json)
# print the JSON string representation of the object
print(GetSpeedtestFilesResponse.to_json())

# convert the object into a dict
get_speedtest_files_response_dict = get_speedtest_files_response_instance.to_dict()
# create an instance of GetSpeedtestFilesResponse from a dict
get_speedtest_files_response_from_dict = GetSpeedtestFilesResponse.from_dict(get_speedtest_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


