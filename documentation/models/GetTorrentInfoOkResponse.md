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

| Name  | Type             | Required | Description |
| :---- | :--------------- | :------- | :---------- |
| files | List[DataFiles2] | ❌       |             |
| hash  | str              | ❌       |             |
| name  | str              | ❌       |             |
| size  | float            | ❌       |             |

# DataFiles_2

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| name | str   | ❌       |             |
| size | float | ❌       |             |
