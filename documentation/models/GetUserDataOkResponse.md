# GetUserDataOkResponse

**Properties**

| Name    | Type                      | Required | Description |
| :------ | :------------------------ | :------- | :---------- |
| data    | GetUserDataOkResponseData | ❌       |             |
| detail  | str                       | ❌       |             |
| success | bool                      | ❌       |             |

# GetUserDataOkResponseData

**Properties**

| Name               | Type     | Required | Description |
| :----------------- | :------- | :------- | :---------- |
| auth_id            | str      | ❌       |             |
| base_email         | str      | ❌       |             |
| cooldown_until     | str      | ❌       |             |
| created_at         | str      | ❌       |             |
| customer           | str      | ❌       |             |
| email              | str      | ❌       |             |
| id\_               | float    | ❌       |             |
| is_subscribed      | bool     | ❌       |             |
| plan               | float    | ❌       |             |
| premium_expires_at | str      | ❌       |             |
| server             | float    | ❌       |             |
| settings           | Settings | ❌       |             |
| total_downloaded   | float    | ❌       |             |
| updated_at         | str      | ❌       |             |
| user_referral      | str      | ❌       |             |

# Settings

**Properties**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| anothersetting | str  | ❌       |             |
| setting        | str  | ❌       |             |
