# GetWebDownloadCachedAvailabilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.get_web_download_cached_availability_response import GetWebDownloadCachedAvailabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebDownloadCachedAvailabilityResponse from a JSON string
get_web_download_cached_availability_response_instance = GetWebDownloadCachedAvailabilityResponse.from_json(json)
# print the JSON string representation of the object
print(GetWebDownloadCachedAvailabilityResponse.to_json())

# convert the object into a dict
get_web_download_cached_availability_response_dict = get_web_download_cached_availability_response_instance.to_dict()
# create an instance of GetWebDownloadCachedAvailabilityResponse from a dict
get_web_download_cached_availability_response_from_dict = GetWebDownloadCachedAvailabilityResponse.from_dict(get_web_download_cached_availability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


