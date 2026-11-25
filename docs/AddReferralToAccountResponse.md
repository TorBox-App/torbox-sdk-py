# AddReferralToAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from torbox.models.add_referral_to_account_response import AddReferralToAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddReferralToAccountResponse from a JSON string
add_referral_to_account_response_instance = AddReferralToAccountResponse.from_json(json)
# print the JSON string representation of the object
print(AddReferralToAccountResponse.to_json())

# convert the object into a dict
add_referral_to_account_response_dict = add_referral_to_account_response_instance.to_dict()
# create an instance of AddReferralToAccountResponse from a dict
add_referral_to_account_response_from_dict = AddReferralToAccountResponse.from_dict(add_referral_to_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


