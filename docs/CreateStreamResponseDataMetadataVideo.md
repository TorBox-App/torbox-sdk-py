# CreateStreamResponseDataMetadataVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**codec_type** | **str** |  | [optional] 
**codec** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **float** |  | [optional] 
**frame_rate** | **str** |  | [optional] 
**pixel_format** | **str** |  | [optional] 
**bitrate** | **str** |  | [optional] 
**duration** | **str** |  | [optional] 
**total_chunks** | **int** |  | [optional] 
**file_name** | **str** |  | [optional] 
**opensubtitles_hash** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**title_data** | **object** |  | [optional] 

## Example

```python
from torbox.models.create_stream_response_data_metadata_video import CreateStreamResponseDataMetadataVideo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStreamResponseDataMetadataVideo from a JSON string
create_stream_response_data_metadata_video_instance = CreateStreamResponseDataMetadataVideo.from_json(json)
# print the JSON string representation of the object
print(CreateStreamResponseDataMetadataVideo.to_json())

# convert the object into a dict
create_stream_response_data_metadata_video_dict = create_stream_response_data_metadata_video_instance.to_dict()
# create an instance of CreateStreamResponseDataMetadataVideo from a dict
create_stream_response_data_metadata_video_from_dict = CreateStreamResponseDataMetadataVideo.from_dict(create_stream_response_data_metadata_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


