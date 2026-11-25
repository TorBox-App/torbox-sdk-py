# GetUsenetCachedAvailabilityBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.get_usenet_cached_availability_batch_response import GetUsenetCachedAvailabilityBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsenetCachedAvailabilityBatchResponse from a JSON string
get_usenet_cached_availability_batch_response_instance = GetUsenetCachedAvailabilityBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetUsenetCachedAvailabilityBatchResponse.to_json())

# convert the object into a dict
get_usenet_cached_availability_batch_response_dict = get_usenet_cached_availability_batch_response_instance.to_dict()
# create an instance of GetUsenetCachedAvailabilityBatchResponse from a dict
get_usenet_cached_availability_batch_response_from_dict = GetUsenetCachedAvailabilityBatchResponse.from_dict(get_usenet_cached_availability_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


