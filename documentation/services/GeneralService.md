# GeneralService

A list of all methods in the `GeneralService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description                                                                                                                                            |
| :------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_up_status](#get_up_status) | ### Overview Simply gets if the TorBox API is available for use or not. Also might include information about downtimes. ### Authorization None needed. |
| [get_stats](#get_stats)         | ### Overview Simply gets general stats about the TorBox service. ### Authorization None needed.                                                        |

## get_up_status

### Overview Simply gets if the TorBox API is available for use or not. Also might include information about downtimes. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/`

**Return Type**

`GetUpStatusOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.general.get_up_status()

print(result)
```

## get_stats

### Overview Simply gets general stats about the TorBox service. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/stats`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`GetStatsOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.general.get_stats(api_version="api_version")

print(result)
```
