# CreateStreamResponseDataIntroInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **float** |  | [optional] 
**end_time** | **float** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from torbox.models.create_stream_response_data_intro_information import CreateStreamResponseDataIntroInformation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStreamResponseDataIntroInformation from a JSON string
create_stream_response_data_intro_information_instance = CreateStreamResponseDataIntroInformation.from_json(json)
# print the JSON string representation of the object
print(CreateStreamResponseDataIntroInformation.to_json())

# convert the object into a dict
create_stream_response_data_intro_information_dict = create_stream_response_data_intro_information_instance.to_dict()
# create an instance of CreateStreamResponseDataIntroInformation from a dict
create_stream_response_data_intro_information_from_dict = CreateStreamResponseDataIntroInformation.from_dict(create_stream_response_data_intro_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


