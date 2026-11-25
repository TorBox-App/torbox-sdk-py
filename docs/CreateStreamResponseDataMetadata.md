# CreateStreamResponseDataMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video** | [**CreateStreamResponseDataMetadataVideo**](CreateStreamResponseDataMetadataVideo.md) |  | [optional] 
**audios** | [**List[CreateStreamResponseDataMetadataAudiosInner]**](CreateStreamResponseDataMetadataAudiosInner.md) |  | [optional] 
**subtitles** | **List[object]** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**chapters** | **str** |  | [optional] 

## Example

```python
from torbox.models.create_stream_response_data_metadata import CreateStreamResponseDataMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStreamResponseDataMetadata from a JSON string
create_stream_response_data_metadata_instance = CreateStreamResponseDataMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateStreamResponseDataMetadata.to_json())

# convert the object into a dict
create_stream_response_data_metadata_dict = create_stream_response_data_metadata_instance.to_dict()
# create an instance of CreateStreamResponseDataMetadata from a dict
create_stream_response_data_metadata_from_dict = CreateStreamResponseDataMetadata.from_dict(create_stream_response_data_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


