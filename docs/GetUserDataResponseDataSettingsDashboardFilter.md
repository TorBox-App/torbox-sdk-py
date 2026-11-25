# GetUserDataResponseDataSettingsDashboardFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**cached** | **bool** |  | [optional] 
**queued** | **bool** |  | [optional] 
**private** | **bool** |  | [optional] 
**borrowed** | **bool** |  | [optional] 
**inactive** | **bool** |  | [optional] 
**torrents** | **bool** |  | [optional] 
**uncached** | **bool** |  | [optional] 
**uploading** | **bool** |  | [optional] 
**processing** | **bool** |  | [optional] 
**downloading** | **bool** |  | [optional] 
**web_downloads** | **bool** |  | [optional] 
**download_ready** | **bool** |  | [optional] 
**usenet_downloads** | **bool** |  | [optional] 

## Example

```python
from torbox.models.get_user_data_response_data_settings_dashboard_filter import GetUserDataResponseDataSettingsDashboardFilter

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserDataResponseDataSettingsDashboardFilter from a JSON string
get_user_data_response_data_settings_dashboard_filter_instance = GetUserDataResponseDataSettingsDashboardFilter.from_json(json)
# print the JSON string representation of the object
print(GetUserDataResponseDataSettingsDashboardFilter.to_json())

# convert the object into a dict
get_user_data_response_data_settings_dashboard_filter_dict = get_user_data_response_data_settings_dashboard_filter_instance.to_dict()
# create an instance of GetUserDataResponseDataSettingsDashboardFilter from a dict
get_user_data_response_data_settings_dashboard_filter_from_dict = GetUserDataResponseDataSettingsDashboardFilter.from_dict(get_user_data_response_data_settings_dashboard_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


