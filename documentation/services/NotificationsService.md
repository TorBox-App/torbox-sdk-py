# NotificationsService

A list of all methods in the `NotificationsService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                                                                                                                                                                                                                                                                           |
| :------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_rss_notification_feed](#get_rss_notification_feed) | ### Overview Gets your notifications in an RSS Feed which allows you to use them with RSS Feed readers or notification services that can take RSS Feeds and listen to updates. As soon as a notification goes to your account, it will be added to your feed. ### Authorization Requires an API key using as a query parameter using the `token` key. |
| [get_notification_feed](#get_notification_feed)         | ### Overview Gets your notifications in a JSON object that is easily parsable compared to the RSS Feed. Gives all the same data as the RSS Feed. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                         |
| [clear_all_notifications](#clear_all_notifications)     | ### Overview Marks all of your notifications as read and deletes them permanently. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                       |
| [clear_single_notification](#clear_single_notification) | ### Overview Marks a single notification as read and permanently deletes it from your notifications. Requires a `notification_id` which can be found by getting your notification feed. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                  |
| [send_test_notification](#send_test_notification)       | ### Overview Sends a test notification to all enabled notification types. This can be useful for validating setups. No need for any body in this request. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                |

## get_rss_notification_feed

### Overview Gets your notifications in an RSS Feed which allows you to use them with RSS Feed readers or notification services that can take RSS Feeds and listen to updates. As soon as a notification goes to your account, it will be added to your feed. ### Authorization Requires an API key using as a query parameter using the `token` key.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/notifications/rss`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| token       | str  | ❌       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.notifications.get_rss_notification_feed(
    api_version="api_version",
    token="{{api_key}}"
)

print(result)
```

## get_notification_feed

### Overview Gets your notifications in a JSON object that is easily parsable compared to the RSS Feed. Gives all the same data as the RSS Feed. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/notifications/mynotifications`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`GetNotificationFeedOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.notifications.get_notification_feed(api_version="api_version")

print(result)
```

## clear_all_notifications

### Overview Marks all of your notifications as read and deletes them permanently. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/notifications/clear`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.notifications.clear_all_notifications(api_version="api_version")

print(result)
```

## clear_single_notification

### Overview Marks a single notification as read and permanently deletes it from your notifications. Requires a `notification_id` which can be found by getting your notification feed. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/notifications/clear/{notification_id}`

**Parameters**

| Name            | Type | Required | Description |
| :-------------- | :--- | :------- | :---------- |
| api_version     | str  | ✅       |             |
| notification_id | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.notifications.clear_single_notification(
    api_version="api_version",
    notification_id="notification_id"
)

print(result)
```

## send_test_notification

### Overview Sends a test notification to all enabled notification types. This can be useful for validating setups. No need for any body in this request. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/notifications/test`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.notifications.send_test_notification(api_version="api_version")

print(result)
```
