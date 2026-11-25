# AddRss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the rss feed you want to add. | 
**name** | **str** | Display name of the rss feed you want to add. | 
**do_regex** | **str** | Regex of items you want to make sure are added. Optional. | [optional] 
**dont_regex** | **str** | Regex of items you dont want added. Optional. | [optional] 
**dont_older_than** | **int** | Time in days that tells the parser to skip if the torrent is older than that many days. Optional. | [optional] 
**pass_check** | **bool** | Boolean which tells to allow multiple of the same url if it already exists on your account | [optional] [default to False]
**scan_interval** | **int** | Time in minutes with the minimum being 10 which you want the api to scan in interval. Optional. Default is 60. | [optional] [default to 60]
**rss_type** | **str** | The type of downloads inside of this RSS feed. Optional. Default is torrent. Options are \&quot;torrent\&quot;, \&quot;usenet\&quot;, \&quot;webdl\&quot; | [optional] [default to 'torrent']
**torrent_seeding** | **int** | Determines if torrents inside of this RSS feed will seed or not. Optional. Default is 1, for auto. Options are 1 for auto, 2 for always, and 3 for never. | [optional] [default to 1]

## Example

```python
from torbox.models.add_rss import AddRss

# TODO update the JSON string below
json = "{}"
# create an instance of AddRss from a JSON string
add_rss_instance = AddRss.from_json(json)
# print the JSON string representation of the object
print(AddRss.to_json())

# convert the object into a dict
add_rss_dict = add_rss_instance.to_dict()
# create an instance of AddRss from a dict
add_rss_from_dict = AddRss.from_dict(add_rss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


