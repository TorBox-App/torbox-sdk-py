# BaseSettingsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_notifications** | **bool** | When the user recieves a notification, send to registered email | [optional] 
**web_notifications** | **bool** | When the user recieves a notification, send to web (if browser is open, otherwise it will be in their notifications panel) | [optional] 
**mobile_notifications** | **bool** | When the user recieves a notification, send to TorBox mobile app (deprecated) | [optional] 
**rss_notifications** | **bool** | When the user recieves a notification, add to user&#39;s RSS feed | [optional] 
**download_speed_in_tab** | **bool** | Shows download speed in tab name in browser when using the TorBox dashboard. Third party apps may still use this setting. | [optional] 
**show_tracker_in_torrent** | **bool** | Shows active tracker in torrents on the TorBox dashboard. Third party apps may still use this setting. | [optional] 
**stremio_quality** | **List[int]** | Determines what qualities are shown to the user when using the TorBox Stremio addon. It is always recommended to include 0 (Unknown). Third party apps may still use this setting.  - &#x60;0&#x60;: Unknown Quality - &#x60;1&#x60;: Cam Quality - &#x60;2&#x60;: DVD-R Quality - &#x60;3&#x60;: HDTV Quality - &#x60;4&#x60;: HDRip Quality - &#x60;5&#x60;: WEB-DL Quality - &#x60;6&#x60;: WEBRip Quality - &#x60;7&#x60;: Blu-Ray/BD/BDRip Quality - &#x60;8&#x60;: HDR Quality - &#x60;9&#x60;: HDR10 Quality - &#x60;10&#x60;: HDR10+ Quality - &#x60;11&#x60;: Dolby Vision Quality  | [optional] 
**stremio_resolution** | **List[int]** | Determines what resolutions are shown to the user. It is always recommended to include 0 (Unknown). Third party apps may still use this setting.  - &#x60;0&#x60;: Unknown Resolution - &#x60;1&#x60;: SD Resolution - &#x60;2&#x60;: HD Resolution - &#x60;3&#x60;: UHD Resolution  | [optional] 
**stremio_language** | **List[int]** | Determines what languages are shown to the user. It is always recommended to include 0 (Unknown). Third party apps may still use this setting.  - &#x60;0&#x60;: Unknown - &#x60;1&#x60;: English - &#x60;2&#x60;: Spanish - &#x60;3&#x60;: French - &#x60;4&#x60;: German - &#x60;5&#x60;: Italian - &#x60;6&#x60;: Portuguese - &#x60;7&#x60;: Russian - &#x60;8&#x60;: Japanese - &#x60;9&#x60;: Korean - &#x60;10&#x60;: Chinese - &#x60;11&#x60;: Arabic - &#x60;12&#x60;: Hindi - &#x60;13&#x60;: Bengali - &#x60;14&#x60;: Ukrainian - &#x60;15&#x60;: Nordic - &#x60;16&#x60;: Czech - &#x60;17&#x60;: Polish - &#x60;18&#x60;: Tamil - &#x60;19&#x60;: Telugu - &#x60;20&#x60;: Kannada - &#x60;21&#x60;: Dutch  | [optional] 
**stremio_cache** | **List[int]** | Determines what cached status items to show to users. While this is an array, only a single value is accepted at a time to prevent issues. Still submit this as an array to the API. Third party apps may still use this setting.  - &#x60;1&#x60;: Cached and Download - &#x60;2&#x60;: Cached Only - &#x60;3&#x60;: Download Only  | [optional] 
**stremio_size_lower** | **int** | The minimum size of files that will be shown to the user in the TorBox Stremio addon. Third party apps may still use this setting. | [optional] 
**google_drive_folder_id** | **str** |  | [optional] 
**onedrive_save_path** | **str** |  | [optional] 
**discord_id** | **str** |  | [optional] 
**discord_notifications** | **bool** | When the user recieves a notification, use the official TorBox Discord Bot to DM the user the notification. Must have a Discord_ID present and must share a server with the Discord Bot. | [optional] 
**stremio_allow_adult** | **bool** | Determines whether to show adult content on the TorBox Stremio addon. Third party apps may still use this setting. | [optional] 
**stremio_seed_torrents** | **int** | 1 &#x3D; Auto, 2 &#x3D; Always, 3 &#x3D; Never | [optional] 
**seed_torrents** | **int** | 1 &#x3D; Auto, 2 &#x3D; Always, 3 &#x3D; Never | [optional] 
**allow_zipped** | **bool** |  | [optional] 
**stremio_allow_zipped** | **bool** |  | [optional] 
**onefichier_folder_id** | **str** |  | [optional] 
**gofile_folder_id** | **str** |  | [optional] 
**webhook_notifications** | **bool** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**telegram_notifications** | **bool** |  | [optional] 
**telegram_id** | **str** |  | [optional] 
**mega_email** | **str** |  | [optional] 
**mega_password** | **str** |  | [optional] 
**stremio_sort** | **str** | seeders &#x3D; Seeders/Age (highest seeders first/lowest age first), size &#x3D; Size (highest size first), resolution &#x3D; Resolution (highest resolution first) | [optional] 
**cdn_selection** | **str** | any available CDN. Can be found using test file route | [optional] 
**stremio_use_custom_search_engines** | **bool** |  | [optional] 
**stremio_result_sort** | **str** | torrents &#x3D; Torrents first, usenet &#x3D; Usenet first | [optional] 
**webdav_use_local_files** | **bool** |  | [optional] 
**stremio_legacy_your_media** | **bool** |  | [optional] 
**stremio_only_your_media_streams** | **bool** | only shows Your Media streams in Stremio addon | [optional] 
**stremio_disable_your_media_streams** | **bool** |  | [optional] 
**webdav_use_folder_view** | **bool** |  | [optional] 
**webdav_flatten** | **bool** |  | [optional] 
**stremio_limit_per_resolution_torrent** | **int** |  | [optional] 
**stremio_limit_per_resolution_usenet** | **int** |  | [optional] 
**stremio_size_upper** | **int** |  | [optional] 
**stremio_torrent_seeders_cutoff** | **int** |  | [optional] 
**pixeldrain_api_key** | **str** |  | [optional] 
**onefichier_api_key** | **str** |  | [optional] 
**gofile_api_key** | **str** |  | [optional] 
**patreon_id** | **str** |  | [optional] 
**stremio_wait_for_download_usenet** | **bool** |  | [optional] 
**stremio_wait_for_download_torrent** | **bool** |  | [optional] 
**stremio_disable_filtered_note** | **bool** |  | [optional] 
**stremio_emoji_in_description** | **bool** |  | [optional] 
**dashboard_filter** | **Dict[str, object]** | sorts the user&#39;s dashboard. Does not affect third party dashboards. This entire dict MUST be presented with all keys for any update to be given. | [optional] 
**web_player_always_transcode** | **bool** |  | [optional] 
**web_player_always_skip_intro** | **bool** |  | [optional] 
**web_player_audio_preferred_language** | **str** |  | [optional] 
**web_player_subtitle_preferred_language** | **str** |  | [optional] 
**web_player_disable_prestream_selector** | **bool** |  | [optional] 
**dashboard_sort** | **str** | default &#x3D; TorBox default sorting, name &#x3D; AZ sorting, size &#x3D; largest size first, added_date &#x3D; newest first, cached_date &#x3D; newest first, last_updated &#x3D; newest first, progress &#x3D; highest progress first, ratio &#x3D; highest ratio first, download_speed &#x3D; highest value first, upload_speed &#x3D; highest value first, eta &#x3D; smallest eta first | [optional] 
**web_player_disable_next_up_dialogue** | **bool** |  | [optional] 
**web_player_enable_scrobbling** | **bool** |  | [optional] 
**append_filename_to_links** | **bool** |  | [optional] 
**subscribed_email_segments** | **List[str]** |  | [optional] 
**disable_ai** | **bool** |  | [optional] 

## Example

```python
from torbox.models.base_settings_model import BaseSettingsModel

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSettingsModel from a JSON string
base_settings_model_instance = BaseSettingsModel.from_json(json)
# print the JSON string representation of the object
print(BaseSettingsModel.to_json())

# convert the object into a dict
base_settings_model_dict = base_settings_model_instance.to_dict()
# create an instance of BaseSettingsModel from a dict
base_settings_model_from_dict = BaseSettingsModel.from_dict(base_settings_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


