# GetUsenetListOkResponse

**Properties**

| Name    | Type                              | Required | Description |
| :------ | :-------------------------------- | :------- | :---------- |
| data    | List[GetUsenetListOkResponseData] | ❌       |             |
| detail  | str                               | ❌       |             |
| error   | any                               | ❌       |             |
| success | bool                              | ❌       |             |

# GetUsenetListOkResponseData

**Properties**

| Name              | Type             | Required | Description |
| :---------------- | :--------------- | :------- | :---------- |
| active            | bool             | ❌       |             |
| auth_id           | str              | ❌       |             |
| availability      | float            | ❌       |             |
| created_at        | str              | ❌       |             |
| download_finished | bool             | ❌       |             |
| download_present  | bool             | ❌       |             |
| download_speed    | float            | ❌       |             |
| download_state    | str              | ❌       |             |
| eta               | float            | ❌       |             |
| expires_at        | str              | ❌       |             |
| files             | List[DataFiles3] | ❌       |             |
| hash              | str              | ❌       |             |
| id\_              | float            | ❌       |             |
| inactive_check    | float            | ❌       |             |
| name              | str              | ❌       |             |
| progress          | float            | ❌       |             |
| server            | float            | ❌       |             |
| size              | float            | ❌       |             |
| torrent_file      | bool             | ❌       |             |
| updated_at        | str              | ❌       |             |
| upload_speed      | float            | ❌       |             |

# DataFiles_3

**Properties**

| Name       | Type  | Required | Description |
| :--------- | :---- | :------- | :---------- |
| id\_       | float | ❌       |             |
| md5        | str   | ❌       |             |
| mimetype   | str   | ❌       |             |
| name       | str   | ❌       |             |
| s3_path    | str   | ❌       |             |
| short_name | str   | ❌       |             |
| size       | float | ❌       |             |
