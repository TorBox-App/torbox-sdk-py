# GetSpeedtestFilesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**closest** | **bool** |  | [optional] 
**coordinates** | [**GetSpeedtestFilesResponseDataInnerCoordinates**](GetSpeedtestFilesResponseDataInnerCoordinates.md) |  | [optional] 

## Example

```python
from torbox.models.get_speedtest_files_response_data_inner import GetSpeedtestFilesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpeedtestFilesResponseDataInner from a JSON string
get_speedtest_files_response_data_inner_instance = GetSpeedtestFilesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetSpeedtestFilesResponseDataInner.to_json())

# convert the object into a dict
get_speedtest_files_response_data_inner_dict = get_speedtest_files_response_data_inner_instance.to_dict()
# create an instance of GetSpeedtestFilesResponseDataInner from a dict
get_speedtest_files_response_data_inner_from_dict = GetSpeedtestFilesResponseDataInner.from_dict(get_speedtest_files_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


