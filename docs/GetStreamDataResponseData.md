# GetStreamDataResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hls_url** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**presigned_token** | **str** |  | [optional] 
**subtitle_index** | **int** |  | [optional] 
**audio_index** | **int** |  | [optional] 
**resolution_index** | **int** |  | [optional] 
**file_token** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**is_transcoding** | **bool** |  | [optional] 
**needs_transcoding** | **bool** |  | [optional] 
**metadata** | [**CreateStreamResponseDataMetadata**](CreateStreamResponseDataMetadata.md) |  | [optional] 
**search_metadata** | [**CreateStreamResponseDataSearchMetadata**](CreateStreamResponseDataSearchMetadata.md) |  | [optional] 

## Example

```python
from torbox.models.get_stream_data_response_data import GetStreamDataResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetStreamDataResponseData from a JSON string
get_stream_data_response_data_instance = GetStreamDataResponseData.from_json(json)
# print the JSON string representation of the object
print(GetStreamDataResponseData.to_json())

# convert the object into a dict
get_stream_data_response_data_dict = get_stream_data_response_data_instance.to_dict()
# create an instance of GetStreamDataResponseData from a dict
get_stream_data_response_data_from_dict = GetStreamDataResponseData.from_dict(get_stream_data_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


