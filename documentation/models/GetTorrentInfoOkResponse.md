# GetTorrentInfoOkResponse

**Properties**

| Name    | Type                         | Required | Description |
| :------ | :--------------------------- | :------- | :---------- |
| data    | GetTorrentInfoOkResponseData | ❌       |             |
| detail  | str                          | ❌       |             |
| error   | any                          | ❌       |             |
| success | bool                         | ❌       |             |

# GetTorrentInfoOkResponseData

**Properties**

| Name     | Type             | Required | Description |
| :------- | :--------------- | :------- | :---------- |
| files    | List[DataFiles2] | ❌       |             |
| hash     | str              | ❌       |             |
| name     | str              | ❌       |             |
| peers    | float            | ❌       |             |
| seeds    | float            | ❌       |             |
| size     | float            | ❌       |             |
| trackers | List[any]        | ❌       |             |

# DataFiles_2

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| name | str   | ❌       |             |
| size | float | ❌       |             |
