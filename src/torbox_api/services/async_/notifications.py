from typing import Awaitable
from .utils.to_async import to_async
from ..notifications import NotificationsService
from ...models.utils.sentinel import SENTINEL
from ...models import GetNotificationFeedOkResponse


class NotificationsServiceAsync(NotificationsService):
    """
    Async Wrapper for NotificationsServiceAsync
    """

    def get_rss_notification_feed(
        self, api_version: str, token: str = SENTINEL
    ) -> Awaitable[str]:
        return to_async(super().get_rss_notification_feed)(api_version, token)

    def get_notification_feed(
        self, api_version: str
    ) -> Awaitable[GetNotificationFeedOkResponse]:
        return to_async(super().get_notification_feed)(api_version)

    def clear_all_notifications(self, api_version: str) -> Awaitable[None]:
        return to_async(super().clear_all_notifications)(api_version)

    def clear_single_notification(
        self, api_version: str, notification_id: str
    ) -> Awaitable[None]:
        return to_async(super().clear_single_notification)(api_version, notification_id)

    def send_test_notification(self, api_version: str) -> Awaitable[None]:
        return to_async(super().send_test_notification)(api_version)
