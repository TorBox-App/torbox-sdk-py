# GetReferralDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | [**GetReferralDataResponseData**](GetReferralDataResponseData.md) |  | [optional] 

## Example

```python
from torbox.models.get_referral_data_response import GetReferralDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferralDataResponse from a JSON string
get_referral_data_response_instance = GetReferralDataResponse.from_json(json)
# print the JSON string representation of the object
print(GetReferralDataResponse.to_json())

# convert the object into a dict
get_referral_data_response_dict = get_referral_data_response_instance.to_dict()
# create an instance of GetReferralDataResponse from a dict
get_referral_data_response_from_dict = GetReferralDataResponse.from_dict(get_referral_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


