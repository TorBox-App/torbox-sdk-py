# CreateStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**CreateStreamResponseData**](CreateStreamResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.create_stream_response import CreateStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStreamResponse from a JSON string
create_stream_response_instance = CreateStreamResponse.from_json(json)
# print the JSON string representation of the object
print(CreateStreamResponse.to_json())

# convert the object into a dict
create_stream_response_dict = create_stream_response_instance.to_dict()
# create an instance of CreateStreamResponse from a dict
create_stream_response_from_dict = CreateStreamResponse.from_dict(create_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


