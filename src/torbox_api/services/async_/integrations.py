from typing import Awaitable
from .utils.to_async import to_async
from ..integrations import IntegrationsService
from ...models import GetAllJobsOkResponse, GetAllJobsByHashOkResponse


class IntegrationsServiceAsync(IntegrationsService):
    """
    Async Wrapper for IntegrationsServiceAsync
    """

    def authenticate_oauth(self, api_version: str, provider: str) -> Awaitable[None]:
        return to_async(super().authenticate_oauth)(api_version, provider)

    def queue_google_drive(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().queue_google_drive)(api_version, request_body)

    def queue_onedrive(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().queue_onedrive)(api_version, request_body)

    def queue_gofile(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().queue_gofile)(api_version, request_body)

    def queue1fichier(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().queue1fichier)(api_version, request_body)

    def get_all_jobs(self, api_version: str) -> Awaitable[GetAllJobsOkResponse]:
        return to_async(super().get_all_jobs)(api_version)

    def get_specific_job(self, api_version: str, job_id: str) -> Awaitable[str]:
        return to_async(super().get_specific_job)(api_version, job_id)

    def cancel_specific_job(self, api_version: str, job_id: str) -> Awaitable[None]:
        return to_async(super().cancel_specific_job)(api_version, job_id)

    def get_all_jobs_by_hash(
        self, api_version: str, hash: str
    ) -> Awaitable[GetAllJobsByHashOkResponse]:
        return to_async(super().get_all_jobs_by_hash)(api_version, hash)
