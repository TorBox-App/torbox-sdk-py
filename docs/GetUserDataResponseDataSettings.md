# GetUserDataResponseDataSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_notifications** | **bool** |  | [optional] 
**web_notifications** | **bool** |  | [optional] 
**mobile_notifications** | **bool** |  | [optional] 
**rss_notifications** | **bool** |  | [optional] 
**download_speed_in_tab** | **bool** |  | [optional] 
**show_tracker_in_torrent** | **bool** |  | [optional] 
**stremio_quality** | **List[float]** |  | [optional] 
**stremio_resolution** | **List[float]** |  | [optional] 
**stremio_language** | **List[float]** |  | [optional] 
**stremio_cache** | **List[float]** |  | [optional] 
**stremio_size_lower** | **int** |  | [optional] 
**stremio_size_upper** | **int** |  | [optional] 
**google_drive_folder_id** | **str** |  | [optional] 
**onedrive_save_path** | **str** |  | [optional] 
**discord_id** | **str** |  | [optional] 
**discord_notifications** | **bool** |  | [optional] 
**stremio_allow_adult** | **bool** |  | [optional] 
**webdav_flatten** | **bool** |  | [optional] 
**stremio_seed_torrents** | **float** |  | [optional] 
**seed_torrents** | **float** |  | [optional] 
**allow_zipped** | **bool** |  | [optional] 
**stremio_allow_zipped** | **bool** |  | [optional] 
**gofile_folder_id** | **str** |  | [optional] 
**onefichier_folder_id** | **str** |  | [optional] 
**jdownloader_notifications** | **bool** |  | [optional] 
**webhook_notifications** | **bool** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**telegram_id** | **str** |  | [optional] 
**telegram_notifications** | **bool** |  | [optional] 
**mega_email** | **str** |  | [optional] 
**mega_password** | **str** |  | [optional] 
**stremio_sort** | **str** |  | [optional] 
**dashboard_filter** | [**GetUserDataResponseDataSettingsDashboardFilter**](GetUserDataResponseDataSettingsDashboardFilter.md) |  | [optional] 
**dashboard_sort** | **str** |  | [optional] 
**cdn_selection** | **str** |  | [optional] 
**stremio_use_custom_search_engines** | **bool** |  | [optional] 
**stremio_result_sort** | **str** |  | [optional] 
**stremio_legacy_your_media** | **bool** |  | [optional] 
**webdav_use_local_files** | **bool** |  | [optional] 
**stremio_disable_your_media_streams** | **bool** |  | [optional] 
**stremio_only_your_media_streams** | **bool** |  | [optional] 
**webdav_use_folder_view** | **bool** |  | [optional] 
**stremio_limit_per_resolution_torrent** | **int** |  | [optional] 
**stremio_limit_per_resolution_usenet** | **int** |  | [optional] 
**stremio_torrent_seeders_cutoff** | **float** |  | [optional] 
**pixeldrain_api_key** | **str** |  | [optional] 
**onefichier_api_key** | **str** |  | [optional] 
**gofile_api_key** | **str** |  | [optional] 
**patreon_id** | **str** |  | [optional] 
**stremio_wait_for_download_usenet** | **bool** |  | [optional] 
**stremio_wait_for_download_torrent** | **bool** |  | [optional] 
**stremio_disable_filtered_note** | **bool** |  | [optional] 
**stremio_emoji_in_description** | **bool** |  | [optional] 
**web_player_always_transcode** | **bool** |  | [optional] 
**web_player_always_skip_intro** | **bool** |  | [optional] 
**web_player_audio_preferred_language** | **str** |  | [optional] 
**web_player_subtitle_preferred_language** | **str** |  | [optional] 
**web_player_disable_prestream_selector** | **bool** |  | [optional] 
**web_player_disable_next_up_dialogue** | **bool** |  | [optional] 
**web_player_enable_scrobbling** | **bool** |  | [optional] 
**append_filename_to_links** | **bool** |  | [optional] 
**disable_ai** | **bool** |  | [optional] 
**subscribed_email_segments** | **List[str]** |  | [optional] 

## Example

```python
from torbox.models.get_user_data_response_data_settings import GetUserDataResponseDataSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserDataResponseDataSettings from a JSON string
get_user_data_response_data_settings_instance = GetUserDataResponseDataSettings.from_json(json)
# print the JSON string representation of the object
print(GetUserDataResponseDataSettings.to_json())

# convert the object into a dict
get_user_data_response_data_settings_dict = get_user_data_response_data_settings_instance.to_dict()
# create an instance of GetUserDataResponseDataSettings from a dict
get_user_data_response_data_settings_from_dict = GetUserDataResponseDataSettings.from_dict(get_user_data_response_data_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


