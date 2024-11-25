# IntegrationsService

A list of all methods in the `IntegrationsService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [authenticate_oauth](#authenticate_oauth)     | ### Overview Allows you to get an authorization token for using the user's account. Callback is located at `/oauth/{provider}/callback` which will verify the token recieved from the OAuth, then redirect you finally to `https://torbox.app/{provider}/success?token={token}&expires_in={expires_in}&expires_at={expires_at}` #### Providers: - "google" -\> Google Drive - "dropbox" -\> Dropbox - "discord" -\> Discord - "onedrive" -\> Azure AD/Microsoft/Onedrive ### Authorization No authorization needed. This is a whitelabel OAuth solution.                                                                                            |
| [queue_google_drive](#queue_google_drive)     | ### Overview Queues a job to upload the specified file or zip to the Google Drive account sent with the `google_token` key. To get this key, either get an OAuth2 token using `/oauth/google` or your own solution. Make sure when creating the OAuth link, you add the scope `https://www.googleapis.com/auth/drive.file` so TorBox has access to the user's Drive. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                   |
| [queue_onedrive](#queue_onedrive)             | ### Overview Queues a job to upload the specified file or zip to the OneDrive sent with the `onedrive_token` key. To get this key, either get an OAuth2 token using `/oauth/onedrive` or your own solution. Make sure when creating the OAuth link you use the scope `files.readwrite.all`. This is compatible with all different types of Microsoft accounts. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                         |
| [queue_gofile](#queue_gofile)                 | ### Overview Queues a job to upload the specified file or zip to the GoFile account sent with the `gofile_token` _(optional)_. To get this key, login to your GoFile account and go [here](https://gofile.io/myProfile). Copy the **Account API Token**. This is what you will use as the `gofile_token`, if you choose to use it. If you don't use an Account API Token, GoFile will simply create an anonymous file. This file will expire after inactivity. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                         |
| [queue1fichier](#queue1fichier)               | ### Overview Queues a job to upload the specified file or zip to the 1Fichier account sent with the `onefichier_token` key (optional). To get this key you must be a Premium or Premium Gold member at 1Fichier. If you are upgraded, [go to the parameters page](https://1fichier.com/console/params.pl), and get an **API Key**. This is what you will use as the `onefichier_token`, if you choose to use it. If you don't use an API Key, 1Fichier will simply create an anonymous file. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                           |
| [get_all_jobs](#get_all_jobs)                 | ### Overview Gets all the jobs attached to a user account. This is good for an overall view of the jobs, such as on a dashboard, or something similar. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.    |
| [get_specific_job](#get_specific_job)         | ### Overview Gets a specifc job using the Job's ID. To get the ID, you will have to Get All Jobs, and get the ID you want. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.                                |
| [get_all_jobs_by_hash](#get_all_jobs_by_hash) | ### Overview Gets all jobs that match a specific hash. Good for checking on specific downloads such as a download page, that could contain a lot of jobs. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header. |

## authenticate_oauth

### Overview Allows you to get an authorization token for using the user's account. Callback is located at `/oauth/{provider}/callback` which will verify the token recieved from the OAuth, then redirect you finally to `https://torbox.app/{provider}/success?token={token}&expires_in={expires_in}&expires_at={expires_at}` #### Providers: - "google" -\> Google Drive - "dropbox" -\> Dropbox - "discord" -\> Discord - "onedrive" -\> Azure AD/Microsoft/Onedrive ### Authorization No authorization needed. This is a whitelabel OAuth solution.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/integration/oauth/{provider}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| provider    | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.integrations.authenticate_oauth(
    api_version="api_version",
    provider="provider"
)

print(result)
```

## queue_google_drive

### Overview Queues a job to upload the specified file or zip to the Google Drive account sent with the `google_token` key. To get this key, either get an OAuth2 token using `/oauth/google` or your own solution. Make sure when creating the OAuth link, you add the scope `https://www.googleapis.com/auth/drive.file` so TorBox has access to the user's Drive. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/integration/googledrive`

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

result = sdk.integrations.queue_google_drive(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## queue_onedrive

### Overview Queues a job to upload the specified file or zip to the OneDrive sent with the `onedrive_token` key. To get this key, either get an OAuth2 token using `/oauth/onedrive` or your own solution. Make sure when creating the OAuth link you use the scope `files.readwrite.all`. This is compatible with all different types of Microsoft accounts. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/integration/onedrive`

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

result = sdk.integrations.queue_onedrive(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## queue_gofile

### Overview Queues a job to upload the specified file or zip to the GoFile account sent with the `gofile_token` _(optional)_. To get this key, login to your GoFile account and go [here](https://gofile.io/myProfile). Copy the **Account API Token**. This is what you will use as the `gofile_token`, if you choose to use it. If you don't use an Account API Token, GoFile will simply create an anonymous file. This file will expire after inactivity. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/integration/gofile`

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

result = sdk.integrations.queue_gofile(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## queue1fichier

### Overview Queues a job to upload the specified file or zip to the 1Fichier account sent with the `onefichier_token` key (optional). To get this key you must be a Premium or Premium Gold member at 1Fichier. If you are upgraded, [go to the parameters page](https://1fichier.com/console/params.pl), and get an **API Key**. This is what you will use as the `onefichier_token`, if you choose to use it. If you don't use an API Key, 1Fichier will simply create an anonymous file. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/integration/1fichier`

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

result = sdk.integrations.queue1fichier(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## get_all_jobs

### Overview Gets all the jobs attached to a user account. This is good for an overall view of the jobs, such as on a dashboard, or something similar. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/integration/jobs`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`GetAllJobsOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.integrations.get_all_jobs(api_version="api_version")

print(result)
```

## get_specific_job

### Overview Gets a specifc job using the Job's ID. To get the ID, you will have to Get All Jobs, and get the ID you want. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/integration/job/{job_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| job_id      | str  | ✅       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.integrations.get_specific_job(
    api_version="api_version",
    job_id="job_id"
)

print(result)
```

## get_all_jobs_by_hash

### Overview Gets all jobs that match a specific hash. Good for checking on specific downloads such as a download page, that could contain a lot of jobs. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/integration/jobs/{hash}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| hash        | str  | ✅       |             |

**Return Type**

`GetAllJobsByHashOkResponse`

**Example Usage Code Snippet**

```python
from torbox_api import TorboxApi

sdk = TorboxApi(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.integrations.get_all_jobs_by_hash(
    api_version="api_version",
    hash="hash"
)

print(result)
```
