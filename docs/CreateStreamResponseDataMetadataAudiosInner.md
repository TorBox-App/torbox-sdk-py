# CreateStreamResponseDataMetadataAudiosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**codec_type** | **str** |  | [optional] 
**codec** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**sample_rate** | **str** |  | [optional] 
**channels** | **float** |  | [optional] 
**channel_layout** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**language_full** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from torbox.models.create_stream_response_data_metadata_audios_inner import CreateStreamResponseDataMetadataAudiosInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStreamResponseDataMetadataAudiosInner from a JSON string
create_stream_response_data_metadata_audios_inner_instance = CreateStreamResponseDataMetadataAudiosInner.from_json(json)
# print the JSON string representation of the object
print(CreateStreamResponseDataMetadataAudiosInner.to_json())

# convert the object into a dict
create_stream_response_data_metadata_audios_inner_dict = create_stream_response_data_metadata_audios_inner_instance.to_dict()
# create an instance of CreateStreamResponseDataMetadataAudiosInner from a dict
create_stream_response_data_metadata_audios_inner_from_dict = CreateStreamResponseDataMetadataAudiosInner.from_dict(create_stream_response_data_metadata_audios_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


