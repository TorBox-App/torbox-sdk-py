# ControlRss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation you want to perform on the RSS feed. Options are &#39;update&#39;, &#39;delete&#39;, &#39;resume&#39; and &#39;pause&#39;. | 
**rss_feed_id** | **int** | The ID of the RSS feed you want to perform the operation on. | 

## Example

```python
from torbox.models.control_rss import ControlRss

# TODO update the JSON string below
json = "{}"
# create an instance of ControlRss from a JSON string
control_rss_instance = ControlRss.from_json(json)
# print the JSON string representation of the object
print(ControlRss.to_json())

# convert the object into a dict
control_rss_dict = control_rss_instance.to_dict()
# create an instance of ControlRss from a dict
control_rss_from_dict = ControlRss.from_dict(control_rss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


