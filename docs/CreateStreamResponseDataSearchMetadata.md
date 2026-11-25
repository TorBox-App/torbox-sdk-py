# CreateStreamResponseDataSearchMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**titles** | **List[str]** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**actors** | **List[str]** |  | [optional] 
**release_years** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**characters** | **List[str]** |  | [optional] 
**global_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**rating** | **float** |  | [optional] 
**languages** | **List[str]** |  | [optional] 
**content_rating** | **str** |  | [optional] 
**trailer** | **object** |  | [optional] 
**image** | **str** |  | [optional] 
**is_adult** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**released_date** | **str** |  | [optional] 
**episodes_number** | **int** |  | [optional] 
**runtime** | **str** |  | [optional] 
**titles_full** | [**List[CreateStreamResponseDataSearchMetadataTitlesFullInner]**](CreateStreamResponseDataSearchMetadataTitlesFullInner.md) |  | [optional] 
**backdrop** | **str** |  | [optional] 

## Example

```python
from torbox.models.create_stream_response_data_search_metadata import CreateStreamResponseDataSearchMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStreamResponseDataSearchMetadata from a JSON string
create_stream_response_data_search_metadata_instance = CreateStreamResponseDataSearchMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateStreamResponseDataSearchMetadata.to_json())

# convert the object into a dict
create_stream_response_data_search_metadata_dict = create_stream_response_data_search_metadata_instance.to_dict()
# create an instance of CreateStreamResponseDataSearchMetadata from a dict
create_stream_response_data_search_metadata_from_dict = CreateStreamResponseDataSearchMetadata.from_dict(create_stream_response_data_search_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


