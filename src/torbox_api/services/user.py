from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import AddReferralToAccountOkResponse, GetUserDataOkResponse


class UserService(BaseService):

    @cast_models
    def refresh_api_token(self, api_version: str, request_body: any = None) -> Any:
        """### Overview

        If you want a new API token, or your old one has been compromised, you may request a new one. If you happen to forget the token, go the [TorBox settings page ](https://torbox.app/settings) and copy the current one. If this still doesn't work, you may contact us at our support email for a new one.

        ### Authorization

        Requires an API key using the Authorization Bearer Header as well as passing the `session_token` from the website to be passed in the body. You can find the `session_token` in the localStorage of your browser on any TorBox.app page under the key `torbox_session_token`. This is a temporary token that only lasts for 1 hour, which is why it is used here to verify the identity of a user as well as their API token.

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
                f"{self.base_url}/{{api_version}}/api/user/refreshtoken",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def get_user_data(
        self, api_version: str, settings: str = None
    ) -> GetUserDataOkResponse:
        """### Overview

        Gets a users account data and information.

        ### Plans

        `0` is Free plan

        `1` is Essential plan (_$3 plan_)

        `2` is Pro plan (_$10 plan_)

        `3` is Standard plan (_$5 plan_)

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param settings: Allows you to retrieve user settings., defaults to None
        :type settings: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Get User Data Success / Get User Data Settings Success
        :rtype: GetUserDataOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(settings)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/user/me",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .add_query("settings", settings)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return GetUserDataOkResponse._unmap(response)

    @cast_models
    def add_referral_to_account(
        self, api_version: str, referral: str = None
    ) -> AddReferralToAccountOkResponse:
        """Add Referral To Account

        :param api_version: api_version
        :type api_version: str
        :param referral: A referral code. Must be UUID., defaults to None
        :type referral: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Add Referral To Account Success
        :rtype: AddReferralToAccountOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(referral)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/user/addreferral",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .add_query("referral", referral)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return AddReferralToAccountOkResponse._unmap(response)