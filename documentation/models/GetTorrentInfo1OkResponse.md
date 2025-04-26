# GetTorrentInfo1OkResponse

**Properties**

| Name    | Type                          | Required | Description |
| :------ | :---------------------------- | :------- | :---------- |
| data    | GetTorrentInfo1OkResponseData | ❌       |             |
| detail  | str                           | ❌       |             |
| error   | any                           | ❌       |             |
| success | bool                          | ❌       |             |

# GetTorrentInfo1OkResponseData

**Properties**

| Name     | Type             | Required | Description |
| :------- | :--------------- | :------- | :---------- |
| files    | List[DataFiles3] | ❌       |             |
| hash     | str              | ❌       |             |
| name     | str              | ❌       |             |
| peers    | float            | ❌       |             |
| seeds    | float            | ❌       |             |
| size     | float            | ❌       |             |
| trackers | List[any]        | ❌       |             |

# DataFiles_3

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| name | str   | ❌       |             |
| size | float | ❌       |             |
