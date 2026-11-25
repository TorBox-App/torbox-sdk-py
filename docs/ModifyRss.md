# ModifyRss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rss_feed_id** | **int** | The ID of the RSS feed you want to modify. | 
**name** | **str** | Display name of the rss feed you want to add. | [optional] 
**do_regex** | **str** | Regex of items you want to make sure are added. Optional. | [optional] 
**dont_regex** | **str** | Regex of items you dont want added. Optional. | [optional] 
**scan_interval** | **int** | Time in minutes with the minimum being 10 which you want the api to scan in interval. Optional. Default is 60. | [optional] [default to 60]
**dont_older_than** | **int** | Time in days that tells the parser to skip if the torrent is older than that many days. Optional. | [optional] 
**rss_type** | **str** | The type of downloads inside of this RSS feed. Optional. Default is torrent. Options are \&quot;torrent\&quot;, \&quot;usenet\&quot;, \&quot;webdl\&quot; | [optional] [default to 'torrent']
**torrent_seeding** | **int** | Determines if torrents inside of this RSS feed will seed or not. Optional. Default is 1, for auto. Options are 1 for auto, 2 for always, and 3 for never. | [optional] [default to 1]

## Example

```python
from torbox.models.modify_rss import ModifyRss

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyRss from a JSON string
modify_rss_instance = ModifyRss.from_json(json)
# print the JSON string representation of the object
print(ModifyRss.to_json())

# convert the object into a dict
modify_rss_dict = modify_rss_instance.to_dict()
# create an instance of ModifyRss from a dict
modify_rss_from_dict = ModifyRss.from_dict(modify_rss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


