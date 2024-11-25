# GetStatsOkResponse

**Properties**

| Name    | Type                   | Required | Description |
| :------ | :--------------------- | :------- | :---------- |
| data    | GetStatsOkResponseData | ❌       |             |
| detail  | str                    | ❌       |             |
| error   | bool                   | ❌       |             |
| success | bool                   | ❌       |             |

# GetStatsOkResponseData

**Properties**

| Name                    | Type  | Required | Description |
| :---------------------- | :---- | :------- | :---------- |
| active_torrents         | float | ❌       |             |
| active_usenet_downloads | float | ❌       |             |
| active_web_downloads    | float | ❌       |             |
| total_bytes_downloaded  | float | ❌       |             |
| total_bytes_uploaded    | float | ❌       |             |
| total_downloads         | float | ❌       |             |
| total_servers           | float | ❌       |             |
| total_torrent_downloads | float | ❌       |             |
| total_usenet_downloads  | float | ❌       |             |
| total_users             | float | ❌       |             |
| total_web_downloads     | float | ❌       |             |
