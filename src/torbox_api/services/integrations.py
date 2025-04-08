from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import GetAllJobsByHashOkResponse, GetAllJobsOkResponse


class IntegrationsService(BaseService):

    @cast_models
    def authenticate_oauth(self, api_version: str, provider: str) -> None:
        """### Overview

        Allows you to get an authorization token for using the user's account. Callback is located at `/oauth/{provider}/callback` which will verify the token recieved from the OAuth, then redirect you finally to `https://torbox.app/{provider}/success?token={token}&expires_in={expires_in}&expires_at={expires_at}`

        #### Providers:

        - "google" -> Google Drive

        - "dropbox" -> Dropbox

        - "discord" -> Discord

        - "onedrive" -> Azure AD/Microsoft/Onedrive


        ### Authorization

        No authorization needed. This is a whitelabel OAuth solution.

        :param api_version: api_version
        :type api_version: str
        :param provider: provider
        :type provider: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)
        Validator(str).validate(provider)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/oauth/{{provider}}",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_path("provider", provider)
            .serialize()
            .set_method("GET")
        )

        self.send_request(serialized_request)

    @cast_models
    def queue_google_drive(self, api_version: str, request_body: any = None) -> None:
        """### Overview

        Queues a job to upload the specified file or zip to the Google Drive account sent with the `google_token` key. To get this key, either get an OAuth2 token using `/oauth/google` or your own solution. Make sure when creating the OAuth link, you add the scope `https://www.googleapis.com/auth/drive.file` so TorBox has access to the user's Drive.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: any, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/googledrive",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def queue_onedrive(self, api_version: str, request_body: any = None) -> None:
        """### Overview

        Queues a job to upload the specified file or zip to the OneDrive sent with the `onedrive_token` key. To get this key, either get an OAuth2 token using `/oauth/onedrive` or your own solution. Make sure when creating the OAuth link you use the scope `files.readwrite.all`. This is compatible with all different types of Microsoft accounts.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: any, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/onedrive",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def queue_gofile(self, api_version: str, request_body: any = None) -> None:
        """### Overview

        Queues a job to upload the specified file or zip to the GoFile account sent with the `gofile_token` _(optional)_. To get this key, login to your GoFile account and go [here](https://gofile.io/myProfile). Copy the **Account API Token**. This is what you will use as the `gofile_token`, if you choose to use it. If you don't use an Account API Token, GoFile will simply create an anonymous file. This file will expire after inactivity.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: any, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/gofile",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def queue1fichier(self, api_version: str, request_body: any = None) -> None:
        """### Overview

        Queues a job to upload the specified file or zip to the 1Fichier account sent with the `onefichier_token` key (optional). To get this key you must be a Premium or Premium Gold member at 1Fichier. If you are upgraded, [go to the parameters page](https://1fichier.com/console/params.pl), and get an **API Key**. This is what you will use as the `onefichier_token`, if you choose to use it. If you don't use an API Key, 1Fichier will simply create an anonymous file.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: any, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/1fichier",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def get_all_jobs(self, api_version: str) -> GetAllJobsOkResponse:
        """### Overview

        Gets all the jobs attached to a user account. This is good for an overall view of the jobs, such as on a dashboard, or something similar.

        ### Statuses

        - "pending" -> Upload is still waiting in the queue. Waiting for spot to upload.
        - "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues.
        - "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated.

        - "failed" -> The upload has failed. Check the Detail key for information.


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetAllJobsOkResponse
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/jobs",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GetAllJobsOkResponse._unmap(response)

    @cast_models
    def get_specific_job(self, api_version: str, job_id: str) -> str:
        """### Overview

        Gets a specifc job using the Job's ID. To get the ID, you will have to Get All Jobs, and get the ID you want.

        ### Statuses

        - "pending" -> Upload is still waiting in the queue. Waiting for spot to upload.
        - "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues.
        - "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated.
        - "failed" -> The upload has failed. Check the Detail key for information.


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param job_id: job_id
        :type job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: str
        """

        Validator(str).validate(api_version)
        Validator(str).validate(job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/job/{{job_id}}",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_path("job_id", job_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def cancel_specific_job(self, api_version: str, job_id: str) -> None:
        """### Overview

        Cancels a job or deletes the job. Cancels while in progess (pending, uploading), or deletes the job any other time. It will delete it from the database completely.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param job_id: job_id
        :type job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)
        Validator(str).validate(job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/job/{{job_id}}",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_path("job_id", job_id)
            .serialize()
            .set_method("DELETE")
        )

        self.send_request(serialized_request)

    @cast_models
    def get_all_jobs_by_hash(
        self, api_version: str, hash: str
    ) -> GetAllJobsByHashOkResponse:
        """### Overview

        Gets all jobs that match a specific hash. Good for checking on specific downloads such as a download page, that could contain a lot of jobs.

        ### Statuses

        - "pending" -> Upload is still waiting in the queue. Waiting for spot to upload.
        - "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues.
        - "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated.
        - "failed" -> The upload has failed. Check the Detail key for information.


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param hash: hash
        :type hash: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetAllJobsByHashOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).validate(hash)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/integration/jobs/{{hash}}",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_path("hash", hash)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GetAllJobsByHashOkResponse._unmap(response)
