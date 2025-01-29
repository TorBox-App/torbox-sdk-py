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
| auth_id                  | str   | ❌       |             |
| current_active_downloads | float | ❌       |             |
| hash                     | str   | ❌       |             |
| queued_id                | float | ❌       |             |
| torrent_id               | float | ❌       |             |
