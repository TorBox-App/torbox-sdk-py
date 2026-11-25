# GetStreamDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetStreamDataResponseData**](GetStreamDataResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_stream_data_response import GetStreamDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStreamDataResponse from a JSON string
get_stream_data_response_instance = GetStreamDataResponse.from_json(json)
# print the JSON string representation of the object
print(GetStreamDataResponse.to_json())

# convert the object into a dict
get_stream_data_response_dict = get_stream_data_response_instance.to_dict()
# create an instance of GetStreamDataResponse from a dict
get_stream_data_response_from_dict = GetStreamDataResponse.from_dict(get_stream_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


