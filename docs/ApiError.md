# ApiError

The envelope every error is answered with. `error` is the stable code to branch on, `detail` the message for people.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | False when the request failed. A list with nothing to return answers &#x60;ITEM_NOT_FOUND&#x60; with &#x60;success&#x60; true: the request worked, there is no data. | 
**error** | **str** | The error code, such as &#x60;BAD_TOKEN&#x60;. Listed in the introduction. | 
**detail** | **str** | What went wrong, in words. | 
**data** | **object** | Extra data for some errors, usually null. | [optional] 

## Example

```python
from torbox.models.api_error import ApiError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiError from a JSON string
api_error_instance = ApiError.from_json(json)
# print the JSON string representation of the object
print(ApiError.to_json())

# convert the object into a dict
api_error_dict = api_error_instance.to_dict()
# create an instance of ApiError from a dict
api_error_from_dict = ApiError.from_dict(api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


