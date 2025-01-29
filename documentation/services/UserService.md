# UserService

A list of all methods in the `UserService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [refresh_api_token](#refresh_api_token)             | ### Overview If you want a new API token, or your old one has been compromised, you may request a new one. If you happen to forget the token, go the [TorBox settings page ](https://torbox.app/settings) and copy the current one. If this still doesn't work, you may contact us at our support email for a new one. ### Authorization Requires an API key using the Authorization Bearer Header as well as passing the `session_token` from the website to be passed in the body. You can find the `session_token` in the localStorage of your browser on any TorBox.app page under the key `torbox_session_token`. This is a temporary token that only lasts for 1 hour, which is why it is used here to verify the identity of a user as well as their API token. |
| [get_user_data](#get_user_data)                     | ### Overview Gets a users account data and information. ### Plans `0` is Free plan `1` is Essential plan (_$3 plan_) `2` is Pro plan (_$10 plan_) `3` is Standard plan (_$5 plan_) ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [add_referral_to_account](#add_referral_to_account) | ### Overview Automatically adds a referral code to the user's account. This can be used for developers to automatically add their referral to user's accounts who use their service. This will not override any referral a user already has. If they already have one, then it cannot be changed using this endpoint. It can only be done by the user on the [website](https://torbox.app/subscription). ### Authorization Requires an API key using the Authorization Bearer Header. Use the user's API key, not your own.                                                                                                                                                                                                                                            |
| [get_confirmation_code](#get_confirmation_code)     | ### Overview Requests a 6 digit code to be sent to the user's email for verification. Used to verify a user actually wants to perform a potentially dangerous action. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## refresh_api_token

### Overview If you want a new API token, or your old one has been compromised, you may request a new one. If you happen to forget the token, go the [TorBox settings page ](https://torbox.app/settings) and copy the current one. If this still doesn't work, you may contact us at our support email for a new one. ### Authorization Requires an API key using the Authorization Bearer Header as well as passing the `session_token` from the website to be passed in the body. You can find the `session_token` in the localStorage of your browser on any TorBox.app page under the key `torbox_session_token`. This is a temporary token that only lasts for 1 hour, which is why it is used here to verify the identity of a user as well as their API token.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/user/refreshtoken`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | any  | ❌       | The request body. |
| api_version  | str  | ✅       |                   |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi
from torbox_api.models import any

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

request_body = ""

result = sdk.user.refresh_api_token(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## get_user_data

### Overview Gets a users account data and information. ### Plans `0` is Free plan `1` is Essential plan (_$3 plan_) `2` is Pro plan (_$10 plan_) `3` is Standard plan (_$5 plan_) ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/me`

**Parameters**

| Name        | Type | Required | Description                           |
| :---------- | :--- | :------- | :------------------------------------ |
| api_version | str  | ✅       |                                       |
| settings    | str  | ❌       | Allows you to retrieve user settings. |

**Return Type**

`GetUserDataOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.user.get_user_data(
    api_version="api_version",
    settings="boolean"
)

print(result)
```

## add_referral_to_account

### Overview Automatically adds a referral code to the user's account. This can be used for developers to automatically add their referral to user's accounts who use their service. This will not override any referral a user already has. If they already have one, then it cannot be changed using this endpoint. It can only be done by the user on the [website](https://torbox.app/subscription). ### Authorization Requires an API key using the Authorization Bearer Header. Use the user's API key, not your own.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/user/addreferral`

**Parameters**

| Name        | Type | Required | Description                    |
| :---------- | :--- | :------- | :----------------------------- |
| api_version | str  | ✅       |                                |
| referral    | str  | ❌       | A referral code. Must be UUID. |

**Return Type**

`AddReferralToAccountOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.user.add_referral_to_account(
    api_version="api_version",
    referral="{{referral_code}}"
)

print(result)
```

## get_confirmation_code

### Overview Requests a 6 digit code to be sent to the user's email for verification. Used to verify a user actually wants to perform a potentially dangerous action. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/getconfirmation`

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

result = sdk.user.get_confirmation_code(api_version="api_version")

print(result)
```
