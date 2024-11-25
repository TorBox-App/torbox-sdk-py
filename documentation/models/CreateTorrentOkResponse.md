# CreateTorrentOkResponse

**Properties**

| Name    | Type                        | Required | Description |
| :------ | :-------------------------- | :------- | :---------- |
| data    | CreateTorrentOkResponseData | ❌       |             |
| detail  | str                         | ❌       |             |
| error   | any                         | ❌       |             |
| success | bool                        | ❌       |             |

# CreateTorrentOkResponseData

**Properties**

| Name                     | Type  | Required | Description |
| :----------------------- | :---- | :------- | :---------- |
| active_limit             | float | ❌       |             |
| current_active_downloads | float | ❌       |             |
| hash                     | str   | ❌       |             |
| name                     | str   | ❌       |             |
| queued_id                | float | ❌       |             |
| torrent_id               | float | ❌       |             |
