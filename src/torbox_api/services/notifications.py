from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import GetNotificationFeedOkResponse


class NotificationsService(BaseService):

    @cast_models
    def get_rss_notification_feed(self, api_version: str, token: str = SENTINEL) -> str:
        """### Overview

        Gets your notifications in an RSS Feed which allows you to use them with RSS Feed readers or notification services that can take RSS Feeds and listen to updates. As soon as a notification goes to your account, it will be added to your feed.

        ### Authorization

        Requires an API key using as a query parameter using the `token` key.

        :param api_version: api_version
        :type api_version: str
        :param token: token, defaults to None
        :type token: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: str
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/rss",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("token", token)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_notification_feed(self, api_version: str) -> GetNotificationFeedOkResponse:
        """### Overview

        Gets your notifications in a JSON object that is easily parsable compared to the RSS Feed. Gives all the same data as the RSS Feed.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetNotificationFeedOkResponse
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/mynotifications",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GetNotificationFeedOkResponse._unmap(response)

    @cast_models
    def clear_all_notifications(self, api_version: str) -> None:
        """### Overview

        Marks all of your notifications as read and deletes them permanently.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/clear",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
        )

        self.send_request(serialized_request)

    @cast_models
    def clear_single_notification(self, api_version: str, notification_id: str) -> None:
        """### Overview

        Marks a single notification as read and permanently deletes it from your notifications. Requires a `notification_id` which can be found by getting your notification feed.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param notification_id: notification_id
        :type notification_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)
        Validator(str).validate(notification_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/clear/{{notification_id}}",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_path("notification_id", notification_id)
            .serialize()
            .set_method("POST")
        )

        self.send_request(serialized_request)

    @cast_models
    def send_test_notification(self, api_version: str) -> None:
        """### Overview

        Sends a test notification to all enabled notification types. This can be useful for validating setups. No need for any body in this request.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/test",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
        )

        self.send_request(serialized_request)
