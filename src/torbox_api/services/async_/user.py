from typing import Awaitable
from .utils.to_async import to_async
from ..user import UserService
from ...models.utils.sentinel import SENTINEL
from ...models import GetUserDataOkResponse, AddReferralToAccountOkResponse


class UserServiceAsync(UserService):
    """
    Async Wrapper for UserServiceAsync
    """

    def refresh_api_token(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().refresh_api_token)(api_version, request_body)

    def get_user_data(
        self, api_version: str, settings: str = SENTINEL
    ) -> Awaitable[GetUserDataOkResponse]:
        return to_async(super().get_user_data)(api_version, settings)

    def add_referral_to_account(
        self, api_version: str, referral: str = SENTINEL
    ) -> Awaitable[AddReferralToAccountOkResponse]:
        return to_async(super().add_referral_to_account)(api_version, referral)

    def get_confirmation_code(self, api_version: str) -> Awaitable[None]:
        return to_async(super().get_confirmation_code)(api_version)
