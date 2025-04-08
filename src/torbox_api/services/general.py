from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    GetChangelogsJsonOkResponse,
    GetStatsOkResponse,
    GetUpStatusOkResponse,
)


class GeneralService(BaseService):

    @cast_models
    def get_up_status(self) -> GetUpStatusOkResponse:
        """### Overview

        Simply gets if the TorBox API is available for use or not. Also might include information about downtimes.

        ### Authorization

        None needed.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetUpStatusOkResponse
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/",
                [self.get_access_token()],
            )
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GetUpStatusOkResponse._unmap(response)

    @cast_models
    def get_stats(self, api_version: str) -> GetStatsOkResponse:
        """### Overview

        Simply gets general stats about the TorBox service.

        ### Authorization

        None needed.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetStatsOkResponse
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/stats",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GetStatsOkResponse._unmap(response)

    @cast_models
    def get_changelogs_rss_feed(self, api_version: str) -> str:
        """### Overview

        Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for people who want updates on the TorBox changelog. Includes all the necessary items to make this compatible with RSS feed viewers for notifications, and proper HTML viewing.

        ### Authorization

        None needed.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: str
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/changelogs/rss",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_changelogs_json(self, api_version: str) -> GetChangelogsJsonOkResponse:
        """### Overview

        Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for developers who want to integrate the changelog into their apps for their users to see. Includes content in HTML and markdown for developers to easily render the text in a fancy yet simple way.

        ### Authorization

        None needed.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetChangelogsJsonOkResponse
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/changelogs/json",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GetChangelogsJsonOkResponse._unmap(response)
