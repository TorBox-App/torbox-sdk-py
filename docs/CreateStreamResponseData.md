# CreateStreamResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**file_id** | **int** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**created_at** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**s3_path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**mimetype** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**open_subtitles_hash** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**user_token** | **str** |  | [optional] 
**webdav_url** | **str** |  | [optional] 
**intro_information** | [**CreateStreamResponseDataIntroInformation**](CreateStreamResponseDataIntroInformation.md) |  | [optional] 
**scrobbling_enabled** | **bool** |  | [optional] 
**hls_url** | **str** |  | [optional] 
**presigned_token** | **str** |  | [optional] 
**subtitle_index** | **int** |  | [optional] 
**audio_index** | **int** |  | [optional] 
**resolution_index** | **int** |  | [optional] 
**is_transcoding** | **bool** |  | [optional] 
**needs_transcoding** | **bool** |  | [optional] 
**metadata** | [**CreateStreamResponseDataMetadata**](CreateStreamResponseDataMetadata.md) |  | [optional] 
**search_metadata** | [**CreateStreamResponseDataSearchMetadata**](CreateStreamResponseDataSearchMetadata.md) |  | [optional] 

## Example

```python
from torbox.models.create_stream_response_data import CreateStreamResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStreamResponseData from a JSON string
create_stream_response_data_instance = CreateStreamResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateStreamResponseData.to_json())

# convert the object into a dict
create_stream_response_data_dict = create_stream_response_data_instance.to_dict()
# create an instance of CreateStreamResponseData from a dict
create_stream_response_data_from_dict = CreateStreamResponseData.from_dict(create_stream_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


