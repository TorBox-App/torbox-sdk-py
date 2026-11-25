# GetReferralDataResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referred_accounts** | **int** |  | [optional] 
**referral_code** | **str** |  | [optional] 
**purchases_referred** | **float** |  | [optional] 

## Example

```python
from torbox.models.get_referral_data_response_data import GetReferralDataResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferralDataResponseData from a JSON string
get_referral_data_response_data_instance = GetReferralDataResponseData.from_json(json)
# print the JSON string representation of the object
print(GetReferralDataResponseData.to_json())

# convert the object into a dict
get_referral_data_response_data_dict = get_referral_data_response_data_instance.to_dict()
# create an instance of GetReferralDataResponseData from a dict
get_referral_data_response_data_from_dict = GetReferralDataResponseData.from_dict(get_referral_data_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


