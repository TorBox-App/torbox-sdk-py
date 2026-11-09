from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    AsyncCreateTorrentRequest,
    CreateTorrentRequest,
    CreateUsenetDownloadRequest,
    CreateWebDownloadRequest,
    EditTorrentItemRequest,
    EditUsenetItemRequest,
    EditWebDownloadItemRequest,
    GetTokenFromDeviceCodeProcessRequest,
    GetTorrentCachedAvailabilityBatchRequest,
    GetTorrentInfoRequest,
    GetUsenetCachedAvailabilityBatchRequest,
    GetWebDownloadCachedAvailabilityBatchRequest,
    MagnetToFileRequest,
    MainApiSdkRequestDownloadLinksPostRequest1,
    MainApiSdkRequestDownloadLinksPostRequest2,
    MainApiSdkRequestDownloadLinksPostRequest3,
)


class MainApiSdkService(BaseService):
    """
    Service class for MainApiSdkService operations.
    Provides methods to interact with MainApiSdkService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._create_torrent_config: SdkConfig = {"environment": Environment.API_BASE}
        self._async_create_torrent_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._control_torrent_config: SdkConfig = {"environment": Environment.API_BASE}
        self._request_download_link_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._request_download_links_get_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._request_download_links_post_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_torrent_list_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_torrent_cached_availability_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_torrent_cached_availability_batch_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._export_torrent_data_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_torrent_info_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_torrent_info_1_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._edit_torrent_item_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._magnet_to_file_config: SdkConfig = {"environment": Environment.API_BASE}
        self._create_usenet_download_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._control_usenet_download_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._request_download_link_1_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._request_download_links_get_1_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._request_download_links_post_1_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_usenet_list_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_usenet_cached_availability_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_usenet_cached_availability_batch_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._edit_usenet_item_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_news_server_connection_information_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_news_server_account_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._reset_news_server_account_password_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._create_web_download_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._control_web_download_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._request_download_link_2_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._request_download_links_get_2_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._request_download_links_post_2_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_web_download_list_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_web_download_cached_availability_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_web_download_cached_availability_batch_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_hoster_list_config: SdkConfig = {"environment": Environment.API_BASE}
        self._edit_web_download_item_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_up_status_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_stats_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_changelogs_rss_feed_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_changelogs_json_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_speedtest_files_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_rss_notification_feed_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_notification_feed_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._clear_all_notifications_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._clear_single_notification_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._send_test_notification_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._refresh_api_token_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_user_data_config: SdkConfig = {"environment": Environment.API_BASE}
        self._add_referral_to_account_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_confirmation_code_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._start_device_code_authorization_process_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_token_from_device_code_process_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_referral_data_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_subscriptions_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_transactions_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_transaction_pdf_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._edit_user_settings_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_user_stats_config: SdkConfig = {"environment": Environment.API_BASE}
        self._add_rss_feed_config: SdkConfig = {"environment": Environment.API_BASE}
        self._control_rss_feed_config: SdkConfig = {"environment": Environment.API_BASE}
        self._edit_rss_feed_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_user_rss_feeds_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_rss_feed_items_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_all_jobs_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_specific_job_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_all_jobs_by_hash_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._cancel_specific_job_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._get_queued_downloads_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._control_queued_downloads_config: SdkConfig = {
            "environment": Environment.API_BASE
        }
        self._create_stream_config: SdkConfig = {"environment": Environment.API_BASE}
        self._get_stream_data_config: SdkConfig = {"environment": Environment.API_BASE}

    def set_create_torrent_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_torrent.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_torrent_config = config
        return self

    def set_async_create_torrent_config(self, config: SdkConfig):
        """
        Sets method-level configuration for async_create_torrent.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._async_create_torrent_config = config
        return self

    def set_control_torrent_config(self, config: SdkConfig):
        """
        Sets method-level configuration for control_torrent.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._control_torrent_config = config
        return self

    def set_request_download_link_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_link.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_link_config = config
        return self

    def set_request_download_links_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_links_get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_links_get_config = config
        return self

    def set_request_download_links_post_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_links_post.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_links_post_config = config
        return self

    def set_get_torrent_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_torrent_list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_torrent_list_config = config
        return self

    def set_get_torrent_cached_availability_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_torrent_cached_availability.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_torrent_cached_availability_config = config
        return self

    def set_get_torrent_cached_availability_batch_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_torrent_cached_availability_batch.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_torrent_cached_availability_batch_config = config
        return self

    def set_export_torrent_data_config(self, config: SdkConfig):
        """
        Sets method-level configuration for export_torrent_data.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._export_torrent_data_config = config
        return self

    def set_get_torrent_info_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_torrent_info.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_torrent_info_config = config
        return self

    def set_get_torrent_info_1_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_torrent_info_1.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_torrent_info_1_config = config
        return self

    def set_edit_torrent_item_config(self, config: SdkConfig):
        """
        Sets method-level configuration for edit_torrent_item.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._edit_torrent_item_config = config
        return self

    def set_magnet_to_file_config(self, config: SdkConfig):
        """
        Sets method-level configuration for magnet_to_file.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._magnet_to_file_config = config
        return self

    def set_create_usenet_download_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_usenet_download.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_usenet_download_config = config
        return self

    def set_control_usenet_download_config(self, config: SdkConfig):
        """
        Sets method-level configuration for control_usenet_download.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._control_usenet_download_config = config
        return self

    def set_request_download_link_1_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_link_1.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_link_1_config = config
        return self

    def set_request_download_links_get_1_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_links_get_1.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_links_get_1_config = config
        return self

    def set_request_download_links_post_1_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_links_post_1.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_links_post_1_config = config
        return self

    def set_get_usenet_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_usenet_list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_usenet_list_config = config
        return self

    def set_get_usenet_cached_availability_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_usenet_cached_availability.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_usenet_cached_availability_config = config
        return self

    def set_get_usenet_cached_availability_batch_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_usenet_cached_availability_batch.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_usenet_cached_availability_batch_config = config
        return self

    def set_edit_usenet_item_config(self, config: SdkConfig):
        """
        Sets method-level configuration for edit_usenet_item.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._edit_usenet_item_config = config
        return self

    def set_get_news_server_connection_information_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_news_server_connection_information.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_news_server_connection_information_config = config
        return self

    def set_get_news_server_account_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_news_server_account.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_news_server_account_config = config
        return self

    def set_reset_news_server_account_password_config(self, config: SdkConfig):
        """
        Sets method-level configuration for reset_news_server_account_password.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._reset_news_server_account_password_config = config
        return self

    def set_create_web_download_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_web_download.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_web_download_config = config
        return self

    def set_control_web_download_config(self, config: SdkConfig):
        """
        Sets method-level configuration for control_web_download.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._control_web_download_config = config
        return self

    def set_request_download_link_2_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_link_2.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_link_2_config = config
        return self

    def set_request_download_links_get_2_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_links_get_2.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_links_get_2_config = config
        return self

    def set_request_download_links_post_2_config(self, config: SdkConfig):
        """
        Sets method-level configuration for request_download_links_post_2.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._request_download_links_post_2_config = config
        return self

    def set_get_web_download_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_web_download_list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_web_download_list_config = config
        return self

    def set_get_web_download_cached_availability_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_web_download_cached_availability.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_web_download_cached_availability_config = config
        return self

    def set_get_web_download_cached_availability_batch_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_web_download_cached_availability_batch.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_web_download_cached_availability_batch_config = config
        return self

    def set_get_hoster_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_hoster_list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_hoster_list_config = config
        return self

    def set_edit_web_download_item_config(self, config: SdkConfig):
        """
        Sets method-level configuration for edit_web_download_item.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._edit_web_download_item_config = config
        return self

    def set_get_up_status_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_up_status.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_up_status_config = config
        return self

    def set_get_stats_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_stats.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_stats_config = config
        return self

    def set_get_changelogs_rss_feed_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_changelogs_rss_feed.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_changelogs_rss_feed_config = config
        return self

    def set_get_changelogs_json_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_changelogs_json.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_changelogs_json_config = config
        return self

    def set_get_speedtest_files_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_speedtest_files.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_speedtest_files_config = config
        return self

    def set_get_rss_notification_feed_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_rss_notification_feed.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_rss_notification_feed_config = config
        return self

    def set_get_notification_feed_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_notification_feed.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_notification_feed_config = config
        return self

    def set_clear_all_notifications_config(self, config: SdkConfig):
        """
        Sets method-level configuration for clear_all_notifications.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._clear_all_notifications_config = config
        return self

    def set_clear_single_notification_config(self, config: SdkConfig):
        """
        Sets method-level configuration for clear_single_notification.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._clear_single_notification_config = config
        return self

    def set_send_test_notification_config(self, config: SdkConfig):
        """
        Sets method-level configuration for send_test_notification.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._send_test_notification_config = config
        return self

    def set_refresh_api_token_config(self, config: SdkConfig):
        """
        Sets method-level configuration for refresh_api_token.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._refresh_api_token_config = config
        return self

    def set_get_user_data_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_user_data.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_user_data_config = config
        return self

    def set_add_referral_to_account_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_referral_to_account.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_referral_to_account_config = config
        return self

    def set_get_confirmation_code_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_confirmation_code.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_confirmation_code_config = config
        return self

    def set_start_device_code_authorization_process_config(self, config: SdkConfig):
        """
        Sets method-level configuration for start_device_code_authorization_process.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._start_device_code_authorization_process_config = config
        return self

    def set_get_token_from_device_code_process_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_token_from_device_code_process.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_token_from_device_code_process_config = config
        return self

    def set_get_referral_data_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_referral_data.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_referral_data_config = config
        return self

    def set_get_subscriptions_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_subscriptions.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_subscriptions_config = config
        return self

    def set_get_transactions_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_transactions.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_transactions_config = config
        return self

    def set_get_transaction_pdf_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_transaction_pdf.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_transaction_pdf_config = config
        return self

    def set_edit_user_settings_config(self, config: SdkConfig):
        """
        Sets method-level configuration for edit_user_settings.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._edit_user_settings_config = config
        return self

    def set_get_user_stats_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_user_stats.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_user_stats_config = config
        return self

    def set_add_rss_feed_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_rss_feed.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_rss_feed_config = config
        return self

    def set_control_rss_feed_config(self, config: SdkConfig):
        """
        Sets method-level configuration for control_rss_feed.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._control_rss_feed_config = config
        return self

    def set_edit_rss_feed_config(self, config: SdkConfig):
        """
        Sets method-level configuration for edit_rss_feed.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._edit_rss_feed_config = config
        return self

    def set_get_user_rss_feeds_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_user_rss_feeds.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_user_rss_feeds_config = config
        return self

    def set_get_rss_feed_items_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_rss_feed_items.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_rss_feed_items_config = config
        return self

    def set_get_all_jobs_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_all_jobs.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_all_jobs_config = config
        return self

    def set_get_specific_job_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_specific_job.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_specific_job_config = config
        return self

    def set_get_all_jobs_by_hash_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_all_jobs_by_hash.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_all_jobs_by_hash_config = config
        return self

    def set_cancel_specific_job_config(self, config: SdkConfig):
        """
        Sets method-level configuration for cancel_specific_job.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._cancel_specific_job_config = config
        return self

    def set_get_queued_downloads_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_queued_downloads.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_queued_downloads_config = config
        return self

    def set_control_queued_downloads_config(self, config: SdkConfig):
        """
        Sets method-level configuration for control_queued_downloads.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._control_queued_downloads_config = config
        return self

    def set_create_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_stream_config = config
        return self

    def set_get_stream_data_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_stream_data.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_stream_data_config = config
        return self

    @cast_models
    def create_torrent(
        self,
        request_body: CreateTorrentRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Creates a torrent under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. ### Rate Limits This endpoint has two limits that apply at the same time: - **300 requests per minute:** a shared ceiling that _every_ request counts against, whether the torrent is cached or uncached. - **60 uncached torrents per hour:** an additional, stricter limit that only uncached torrents count against. The important thing is that cached and uncached requests both draw from the same 300/min pool, but uncached requests _also_ draw from their own separate 60/hour pool. An uncached request therefore counts twice: once against the per-minute limit, and once against the per-hour uncached limit. **Example:** In a single minute you add 250 cached + 50 uncached torrents. That's 300 total, so you've hit the per-minute limit for that minute. But those 50 uncached torrents also came out of your 60/hour uncached budget, leaving only **10 uncached torrents** for the remaining 59 minutes of that hour. (You could still add plenty more _cached_ torrents during that hour, since cached requests aren't capped hourly: only by the 300/min ceiling.) ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: CreateTorrentRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(CreateTorrentRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._create_torrent_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/createtorrent",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def async_create_torrent(
        self,
        request_body: AsyncCreateTorrentRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Creates a torrent asynchrously under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. The request will return instantly, not returning any data other than a success message. This is the same for failures, as they will return the error in the background, rather than immediately. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: AsyncCreateTorrentRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(AsyncCreateTorrentRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._async_create_torrent_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/asynccreatetorrent",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def control_torrent(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Controls a torrent. By sending the torrent's ID and the type of operation you want to perform, it will send that request to the torrent client. Operations are either: - **Reannounce** `reannounces the torrent to get new peers` - **Delete** `deletes the torrent from the client and your account permanently` - **Resume** `resumes a paused torrent` ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._control_torrent_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/controltorrent",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_link(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        torrent_id: Union[str, None] = SENTINEL,
        file_id: Union[str, None] = SENTINEL,
        zip_link: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        redirect: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param torrent_id: The torrent's ID that you want to download, defaults to None
        :type torrent_id: str, optional
        :param file_id: The files's ID that you want to download, defaults to None
        :type file_id: str, optional
        :param zip_link: If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given., defaults to None
        :type zip_link: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param redirect: If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link., defaults to None
        :type redirect: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(torrent_id, "torrent_id")
        Validator(str).is_optional().is_nullable().validate(file_id, "file_id")
        Validator(str).is_optional().is_nullable().validate(zip_link, "zip_link")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(redirect, "redirect")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_link_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/requestdl",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("torrent_id", torrent_id, nullable=True)
            .add_query("file_id", file_id, nullable=True)
            .add_query("zip_link", zip_link, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("redirect", redirect, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_links_get(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        torrent_id: Union[str, None] = SENTINEL,
        file_ids: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param torrent_id: The torrent's ID that you want to download, defaults to None
        :type torrent_id: str, optional
        :param file_ids: The files's ID that you want to download, defaults to None
        :type file_ids: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(torrent_id, "torrent_id")
        Validator(str).is_optional().is_nullable().validate(file_ids, "file_ids")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_links_get_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/requestdl/batch",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("torrent_id", torrent_id, nullable=True)
            .add_query("file_ids", file_ids, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_links_post(
        self,
        request_body: MainApiSdkRequestDownloadLinksPostRequest1,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        torrent_id: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param request_body: The request body.
        :type request_body: MainApiSdkRequestDownloadLinksPostRequest1
        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param torrent_id: The torrent's ID that you want to download, defaults to None
        :type torrent_id: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(MainApiSdkRequestDownloadLinksPostRequest1).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(torrent_id, "torrent_id")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_links_post_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/requestdl/batch",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("torrent_id", torrent_id, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_torrent_list(
        self,
        api_version: str,
        bypass_cache: Union[str, None] = SENTINEL,
        id_: Union[str, None] = SENTINEL,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        active: Union[str, None] = SENTINEL,
        files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets the user's torrent list. This gives you the needed information to perform other torrent actions. This information only gets updated every 600 seconds, or when the _Request Update On Torrent_ request is sent to the _relay API_. #### Download States: - "downloading" -> The torrent is currently downloading. - "uploading" -> The torrent is currently seeding. - "stalled (no seeds)" -> The torrent is trying to download, but there are no seeds connected to download from. - "paused" -> The torrent is paused. - "completed" -> The torrent is completely downloaded. Do not use this for download completion status. - "cached" -> The torrent is cached from the server. - "metaDL" -> The torrent is downloading metadata from the hoard. - "checkingResumeData" -> The torrent is checking resumable data. All other statuses are basic qBittorrent states. [Check out here for the full list](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management). ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param bypass_cache: Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls., defaults to None
        :type bypass_cache: str, optional
        :param id_: Determines the torrent requested, will return an object rather than list. Optional., defaults to None
        :type id_: str, optional
        :param offset: Determines the offset of items to get from the database. Default is 0. Optional., defaults to None
        :type offset: str, optional
        :param limit: Determines the number of items to recieve per request. Default is 1000. Optional., defaults to None
        :type limit: str, optional
        :param active: Shows only active downloads. Optional, defaults to None
        :type active: str, optional
        :param files: Exclude files from response. Optional, defaults to None
        :type files: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(
            bypass_cache, "bypass_cache"
        )
        Validator(str).is_optional().is_nullable().validate(id_, "id_")
        Validator(str).is_optional().is_nullable().validate(offset, "offset")
        Validator(str).is_optional().is_nullable().validate(limit, "limit")
        Validator(str).is_optional().is_nullable().validate(active, "active")
        Validator(str).is_optional().is_nullable().validate(files, "files")

        resolved_config = self._get_resolved_config(
            self._get_torrent_list_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/mylist",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("bypass_cache", bypass_cache, nullable=True)
            .add_query("id", id_, nullable=True)
            .add_query("offset", offset, nullable=True)
            .add_query("limit", limit, nullable=True)
            .add_query("active", active, nullable=True)
            .add_query("files", files, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_torrent_cached_availability(
        self,
        api_version: str,
        hash: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
        list_files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Takes in a list of comma separated torrent hashes and checks if the torrent is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param hash: The list of torrent hashes you want to check. Comma seperated., defaults to None
        :type hash: str, optional
        :param format: Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list., defaults to None
        :type format: str, optional
        :param list_files: Allows you to list the files found inside the cached data., defaults to None
        :type list_files: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(hash, "hash")
        Validator(str).is_optional().is_nullable().validate(format, "format")
        Validator(str).is_optional().is_nullable().validate(list_files, "list_files")

        resolved_config = self._get_resolved_config(
            self._get_torrent_cached_availability_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/checkcached",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("hash", hash, nullable=True)
            .add_query("format", format, nullable=True)
            .add_query("list_files", list_files, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_torrent_cached_availability_batch(
        self,
        request_body: GetTorrentCachedAvailabilityBatchRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Takes in a list of comma separated torrent hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: GetTorrentCachedAvailabilityBatchRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(GetTorrentCachedAvailabilityBatchRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_torrent_cached_availability_batch_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/checkcached",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def export_torrent_data(
        self,
        api_version: str,
        torrent_id: Union[str, None] = SENTINEL,
        type_: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Exports the magnet or torrent file. Requires a type to be passed. If type is **magnet**, it will return a JSON response with the magnet as a string in the _data_ key. If type is **file**, it will return a bittorrent file as a download. Not compatible with cached downloads. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param torrent_id: The torrent's ID., defaults to None
        :type torrent_id: str, optional
        :param type_: Either "magnet" or "file". Tells how the API what to get, and what to respond as. If magnet, it returns a JSON response with the magnet as a string in the data key. If file, it responds with a torrent file download., defaults to None
        :type type_: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(torrent_id, "torrent_id")
        Validator(str).is_optional().is_nullable().validate(type_, "type_")

        resolved_config = self._get_resolved_config(
            self._export_torrent_data_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/exportdata",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("torrent_id", torrent_id, nullable=True)
            .add_query("type", type_, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_torrent_info(
        self,
        api_version: str,
        hash: Union[str, None] = SENTINEL,
        timeout: Union[str, None] = SENTINEL,
        use_cache_lookup: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant. **It is not recommended to use this for checking TorBox's cache. Please use the GET /checkcache endpoint instead.** ### Authorization None required.

        :param api_version: api_version
        :type api_version: str
        :param hash: Hash of the torrent you want to get info for. This is required., defaults to None
        :type hash: str, optional
        :param timeout: The amount of time you want TorBox to search for the torrent on the Bittorrent network. If the number of seeders is low or even zero, this value may be helpful to move up. Default is 10. Optional., defaults to None
        :type timeout: str, optional
        :param use_cache_lookup: If you want to use a pre-cached request if sent before. This can save a lot of time. Default false., defaults to None
        :type use_cache_lookup: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(hash, "hash")
        Validator(str).is_optional().is_nullable().validate(timeout, "timeout")
        Validator(str).is_optional().is_nullable().validate(
            use_cache_lookup, "use_cache_lookup"
        )

        resolved_config = self._get_resolved_config(
            self._get_torrent_info_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/torrentinfo",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("hash", hash, nullable=True)
            .add_query("timeout", timeout, nullable=True)
            .add_query("use_cache_lookup", use_cache_lookup, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_torrent_info_1(
        self,
        request_body: GetTorrentInfoRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Same as the GET route, but allows posting data such as magnet, and torrent files. Hashes will have precedence over magnets, and magnets will have precedence over torrent files. Only proper torrent files are accepted. At least one of hash, magnet, or torrent file is required. A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant. **It is not recommended to use this for checking TorBox's cache. Please use the GET /checkcache endpoint instead.** ### Authorization None required.

        :param request_body: The request body.
        :type request_body: GetTorrentInfoRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(GetTorrentInfoRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_torrent_info_1_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/torrentinfo",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def edit_torrent_item(
        self,
        request_body: EditTorrentItemRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: EditTorrentItemRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(EditTorrentItemRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._edit_torrent_item_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/edittorrent",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def magnet_to_file(
        self,
        request_body: MagnetToFileRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Converts any magnet to a torrent file. Does not require the magnet to be on your TorBox account or in the TorBox cache. Free endpoint for public use. ### Authorization None required.

        :param request_body: The request body.
        :type request_body: MagnetToFileRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(MagnetToFileRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._magnet_to_file_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/torrents/magnettofile",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def create_usenet_download(
        self,
        request_body: CreateUsenetDownloadRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Creates a usenet download under your account. Simply send **either** a link, or an nzb file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. #### Post Processing Options: All post processing options that the Usenet client will perform before TorBox's own processing to make the files available. It is recommended you either don't send this parameter, or keep it at `-1` for default, which will give only the wanted files. - `-1`, Default. This runs repairs, and extractions as well as deletes the source files leaving only the wanted downloaded files. - `0`, None. No post-processing at all. Just download all the files (including all PAR2). TorBox will still do its normal processing to make the download available, but no repairs, or extraction will take place. - `1`, Repair. Download files and do a PAR2 verification. If the verification fails, download more PAR2 files and attempt to repair the files. - `2`, Repair and Unpack. Download all files, do a PAR2 verification and unpack the files. The final folder will also include the RAR and ZIP files. - `3`, Repair, Unpack and Delete. Download all files, do a PAR2 verification, unpack the files to the final folder and delete the source files. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: CreateUsenetDownloadRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(CreateUsenetDownloadRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._create_usenet_download_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/createusenetdownload",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def control_usenet_download(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Controls a usenet download. By sending the usenet download's ID and the type of operation you want to perform, it will send that request to the usenet client. Operations are either: - **Delete** `deletes the nzb from the client and your account permanently` ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._control_usenet_download_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/controlusenetdownload",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_link_1(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        usenet_id: Union[str, None] = SENTINEL,
        file_id: Union[str, None] = SENTINEL,
        zip_link: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        redirect: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param usenet_id: The usenet download's ID that you want to download, defaults to None
        :type usenet_id: str, optional
        :param file_id: The files's ID that you want to download. Optional if using "zip_link"., defaults to None
        :type file_id: str, optional
        :param zip_link: If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given., defaults to None
        :type zip_link: str, optional
        :param user_ip: The user's IPv4 to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param redirect: If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link., defaults to None
        :type redirect: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(usenet_id, "usenet_id")
        Validator(str).is_optional().is_nullable().validate(file_id, "file_id")
        Validator(str).is_optional().is_nullable().validate(zip_link, "zip_link")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(redirect, "redirect")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_link_1_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/requestdl",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("usenet_id", usenet_id, nullable=True)
            .add_query("file_id", file_id, nullable=True)
            .add_query("zip_link", zip_link, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("redirect", redirect, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_links_get_1(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        usenet_id: Union[str, None] = SENTINEL,
        file_ids: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param usenet_id: The usenet download's ID that you want to download, defaults to None
        :type usenet_id: str, optional
        :param file_ids: The files's ID that you want to download, defaults to None
        :type file_ids: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(usenet_id, "usenet_id")
        Validator(str).is_optional().is_nullable().validate(file_ids, "file_ids")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_links_get_1_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/requestdl/batch",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("usenet_id", usenet_id, nullable=True)
            .add_query("file_ids", file_ids, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_links_post_1(
        self,
        request_body: MainApiSdkRequestDownloadLinksPostRequest2,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        usenet_id: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param request_body: The request body.
        :type request_body: MainApiSdkRequestDownloadLinksPostRequest2
        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param usenet_id: The usenet downloads' ID that you want to download, defaults to None
        :type usenet_id: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(MainApiSdkRequestDownloadLinksPostRequest2).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(usenet_id, "usenet_id")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_links_post_1_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/requestdl/batch",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("usenet_id", usenet_id, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_usenet_list(
        self,
        api_version: str,
        bypass_cache: Union[str, None] = SENTINEL,
        id_: Union[str, None] = SENTINEL,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        active: Union[str, None] = SENTINEL,
        files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets the user's usenet download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live usenet downloads. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param bypass_cache: Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls., defaults to None
        :type bypass_cache: str, optional
        :param id_: Determines the usenet download requested, will return an object rather than list. Optional., defaults to None
        :type id_: str, optional
        :param offset: Determines the offset of items to get from the database. Default is 0. Optional., defaults to None
        :type offset: str, optional
        :param limit: Determines the number of items to recieve per request. Default is 1000. Optional., defaults to None
        :type limit: str, optional
        :param active: Shows only active downloads. Optional, defaults to None
        :type active: str, optional
        :param files: Exclude files from response. Optional, defaults to None
        :type files: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(
            bypass_cache, "bypass_cache"
        )
        Validator(str).is_optional().is_nullable().validate(id_, "id_")
        Validator(str).is_optional().is_nullable().validate(offset, "offset")
        Validator(str).is_optional().is_nullable().validate(limit, "limit")
        Validator(str).is_optional().is_nullable().validate(active, "active")
        Validator(str).is_optional().is_nullable().validate(files, "files")

        resolved_config = self._get_resolved_config(
            self._get_usenet_list_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/mylist",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("bypass_cache", bypass_cache, nullable=True)
            .add_query("id", id_, nullable=True)
            .add_query("offset", offset, nullable=True)
            .add_query("limit", limit, nullable=True)
            .add_query("active", active, nullable=True)
            .add_query("files", files, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_usenet_cached_availability(
        self,
        api_version: str,
        hash: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
        list_files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Takes in a list of comma separated usenet hashes and checks if the usenet download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. To get the hash of a usenet download, you can read [this document](https://support.torbox.app/en/articles/13681109-technical-getting-hashes-for-searches) for all of the strategies. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param hash: The list of usenet hashes you want to check. Comma seperated. To find the hash, md5 the link of the usenet link or file., defaults to None
        :type hash: str, optional
        :param format: Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list., defaults to None
        :type format: str, optional
        :param list_files: Allows you to list the files found inside the cached data. Optional., defaults to None
        :type list_files: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(hash, "hash")
        Validator(str).is_optional().is_nullable().validate(format, "format")
        Validator(str).is_optional().is_nullable().validate(list_files, "list_files")

        resolved_config = self._get_resolved_config(
            self._get_usenet_cached_availability_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/checkcached",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("hash", hash, nullable=True)
            .add_query("format", format, nullable=True)
            .add_query("list_files", list_files, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_usenet_cached_availability_batch(
        self,
        request_body: GetUsenetCachedAvailabilityBatchRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Takes in a list of comma separated hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: GetUsenetCachedAvailabilityBatchRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(GetUsenetCachedAvailabilityBatchRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_usenet_cached_availability_batch_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/checkcached",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def edit_usenet_item(
        self,
        request_body: EditUsenetItemRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: EditUsenetItemRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(EditUsenetItemRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._edit_usenet_item_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/editusenetdownload",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_news_server_connection_information(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Gets the TorBox News Server Connection information. This is a static path, and is not dynamic. ### Authorization No authentication required.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_news_server_connection_information_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/provider/connection",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_news_server_account(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Gets the user's TorBox News Server Account with authentication details. Does not show password if not creating the account. Account creation happens on the first request. If you need to get the password, or reset the password, use the `/usenet/provider/account/resetpw` `POST` endpoint. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_news_server_account_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/provider/account",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def reset_news_server_account_password(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Resets the user's TorBox News Server account password. This password is automatically generated, and is not saved, it is only shown once. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._reset_news_server_account_password_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/provider/account/resetpw",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def create_web_download(
        self,
        request_body: CreateWebDownloadRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Creates a web download under your account. Simply send a link to any file on the internet. Once it has been checked, it will begin downloading assuming your account has available active download slots, and they aren't too large. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: CreateWebDownloadRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(CreateWebDownloadRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._create_web_download_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/createwebdownload",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def control_web_download(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Controls a web download. By sending the web download's ID and the type of operation you want to perform, it will send that request to the debrid client. Operations are either: - **Delete** `deletes the download from the client and your account permanently` ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._control_web_download_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/controlwebdownload",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_link_2(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        web_id: Union[str, None] = SENTINEL,
        file_id: Union[str, None] = SENTINEL,
        zip_link: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        redirect: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param web_id: The web download's ID that you want to download, defaults to None
        :type web_id: str, optional
        :param file_id: The files's ID that you want to download, defaults to None
        :type file_id: str, optional
        :param zip_link: If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given., defaults to None
        :type zip_link: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param redirect: If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link., defaults to None
        :type redirect: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(web_id, "web_id")
        Validator(str).is_optional().is_nullable().validate(file_id, "file_id")
        Validator(str).is_optional().is_nullable().validate(zip_link, "zip_link")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(redirect, "redirect")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_link_2_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/requestdl",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("web_id", web_id, nullable=True)
            .add_query("file_id", file_id, nullable=True)
            .add_query("zip_link", zip_link, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("redirect", redirect, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_links_get_2(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        web_id: Union[str, None] = SENTINEL,
        file_ids: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param web_id: The web download's ID that you want to download, defaults to None
        :type web_id: str, optional
        :param file_ids: The files's ID that you want to download, defaults to None
        :type file_ids: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(web_id, "web_id")
        Validator(str).is_optional().is_nullable().validate(file_ids, "file_ids")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_links_get_2_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/requestdl/batch",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("web_id", web_id, nullable=True)
            .add_query("file_ids", file_ids, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def request_download_links_post_2(
        self,
        request_body: MainApiSdkRequestDownloadLinksPostRequest3,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        web_id: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

        :param request_body: The request body.
        :type request_body: MainApiSdkRequestDownloadLinksPostRequest3
        :param api_version: api_version
        :type api_version: str
        :param token: Your API Key, defaults to None
        :type token: str, optional
        :param web_id: The web downloads' ID that you want to download, defaults to None
        :type web_id: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param append_name: If you want to add the "filename" parameter to the returned CDN link. Optional. Default false., defaults to None
        :type append_name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(MainApiSdkRequestDownloadLinksPostRequest3).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(web_id, "web_id")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")
        Validator(str).is_optional().is_nullable().validate(append_name, "append_name")

        resolved_config = self._get_resolved_config(
            self._request_download_links_post_2_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/requestdl/batch",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .add_query("web_id", web_id, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .add_query("append_name", append_name, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_web_download_list(
        self,
        api_version: str,
        bypass_cache: Union[str, None] = SENTINEL,
        id_: Union[str, None] = SENTINEL,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        active: Union[str, None] = SENTINEL,
        files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets the user's web download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live web downloads. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param bypass_cache: Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls., defaults to None
        :type bypass_cache: str, optional
        :param id_: Determines the torrent requested, will return an object rather than list. Optional., defaults to None
        :type id_: str, optional
        :param offset: Determines the offset of items to get from the database. Default is 0. Optional., defaults to None
        :type offset: str, optional
        :param limit: Determines the number of items to recieve per request. Default is 1000. Optional., defaults to None
        :type limit: str, optional
        :param active: Shows only active downloads. Optional, defaults to None
        :type active: str, optional
        :param files: Exclude files from response. Optional, defaults to None
        :type files: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(
            bypass_cache, "bypass_cache"
        )
        Validator(str).is_optional().is_nullable().validate(id_, "id_")
        Validator(str).is_optional().is_nullable().validate(offset, "offset")
        Validator(str).is_optional().is_nullable().validate(limit, "limit")
        Validator(str).is_optional().is_nullable().validate(active, "active")
        Validator(str).is_optional().is_nullable().validate(files, "files")

        resolved_config = self._get_resolved_config(
            self._get_web_download_list_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/mylist",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("bypass_cache", bypass_cache, nullable=True)
            .add_query("id", id_, nullable=True)
            .add_query("offset", offset, nullable=True)
            .add_query("limit", limit, nullable=True)
            .add_query("active", active, nullable=True)
            .add_query("files", files, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_web_download_cached_availability(
        self,
        api_version: str,
        hash: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
        list_files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Takes in a list of comma separated usenet hashes and checks if the web download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. To get the hash of a web download you can read [this document](https://support.torbox.app/en/articles/13681109-technical-getting-hashes-for-searches) for all of the strategies. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param hash: The list of web hashes you want to check. Comma seperated. To find the hash, md5 the link., defaults to None
        :type hash: str, optional
        :param format: Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list., defaults to None
        :type format: str, optional
        :param list_files: Allows you to list the files found inside the cached data., defaults to None
        :type list_files: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(hash, "hash")
        Validator(str).is_optional().is_nullable().validate(format, "format")
        Validator(str).is_optional().is_nullable().validate(list_files, "list_files")

        resolved_config = self._get_resolved_config(
            self._get_web_download_cached_availability_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/checkcached",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("hash", hash, nullable=True)
            .add_query("format", format, nullable=True)
            .add_query("list_files", list_files, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_web_download_cached_availability_batch(
        self,
        request_body: GetWebDownloadCachedAvailabilityBatchRequest,
        api_version: str,
        format: Union[str, None] = SENTINEL,
        list_files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Takes in a list of comma separated hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: GetWebDownloadCachedAvailabilityBatchRequest
        :param api_version: api_version
        :type api_version: str
        :param format: Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list., defaults to None
        :type format: str, optional
        :param list_files: Allows you to list the files found inside the cached data., defaults to None
        :type list_files: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(GetWebDownloadCachedAvailabilityBatchRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(format, "format")
        Validator(str).is_optional().is_nullable().validate(list_files, "list_files")

        resolved_config = self._get_resolved_config(
            self._get_web_download_cached_availability_batch_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/checkcached",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("format", format, nullable=True)
            .add_query("list_files", list_files, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_hoster_list(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview A dynamic list of hosters that TorBox is capable of downloading through its paid service. - **Name** - a clean name for display use, the well known name of the service, should be recognizable to users. - **Domains** - an array of known domains that the hoster uses. While each may serve a different purpose it is still included. - **URL** - the main url of the service. This should take you to the home page or a service page of the hoster. - **Icon** - a square image, usually a favicon or logo, that represents the service, should be recognizable as the hoster's icon. - **Status** - whether this hoster can be used on TorBox or not at the current time. It is usually a good idea to check this value before submitting a download to TorBox's servers for download. - **Type** - values are either "hoster" or "stream". Both do the same thing, but is good to differentiate services used for different things. - **Note** - a string value (or null) that may give helpful information about the current status or state of a hoster. This can and should be shown to end users. - **Daily Link Limit** - the number of downloads a user can use per day. As a user submits links, once they hit this number, the API will deny them from adding anymore of this type of link. A zero value means that it is unlimited. - **Daily Link Used** - the number of downloads a user has already used. Usually zero unless you send authentication to the endpoint. This will return accurate values. - **Daily Bandwidth Limit** - the value in bytes that a user is allowed to download from this hoster. A zero value means that it is unlimited. It is recommended to use the Daily Link Limit instead. - **Daily Bandwidth Used** - the value in bytes that a user has already used to download from this hoster. Usually zero unless you send authentication to the endpoint. This will return accurate values. ### Authorization Optional authorization. Authorization is not required in this endpoint unless you want to get the user's live data. Requires an API key using the Authorization Bearer Header to get the live and accurate data for **Daily Link Used** and **Daily Bandwidth Used**.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_hoster_list_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/hosters",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def edit_web_download_item(
        self,
        request_body: EditWebDownloadItemRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: EditWebDownloadItemRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(EditWebDownloadItemRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._edit_web_download_item_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/editwebdownload",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_up_status(self, *, request_config: Optional[SdkConfig] = None) -> Any:
        """### Overview Simply gets if the TorBox API is available for use or not. Also might include information about downtimes. ### Authorization None needed.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        resolved_config = self._get_resolved_config(
            self._get_up_status_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_stats(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Simply gets general stats about the TorBox service. ### Authorization None needed.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_stats_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/stats",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_changelogs_rss_feed(
        self,
        api_version: str,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> str:
        """### Overview Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for people who want updates on the TorBox changelog. Includes all the necessary items to make this compatible with RSS feed viewers for notifications, and proper HTML viewing. ### Authorization None needed.

        :param api_version: api_version
        :type api_version: str
        :param offset: offset, defaults to None
        :type offset: str, optional
        :param limit: limit, defaults to None
        :type limit: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: str
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(offset, "offset")
        Validator(str).is_optional().is_nullable().validate(limit, "limit")

        resolved_config = self._get_resolved_config(
            self._get_changelogs_rss_feed_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/changelogs/rss",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("offset", offset, nullable=True)
            .add_query("limit", limit, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_changelogs_json(
        self,
        api_version: str,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets most recent changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for developers who want to integrate the changelog into their apps for their users to see. Includes content in HTML for developers to easily render the text in a fancy yet simple way. ### Authorization None needed.

        :param api_version: api_version
        :type api_version: str
        :param offset: offset, defaults to None
        :type offset: str, optional
        :param limit: limit, defaults to None
        :type limit: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(offset, "offset")
        Validator(str).is_optional().is_nullable().validate(limit, "limit")

        resolved_config = self._get_resolved_config(
            self._get_changelogs_json_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/changelogs/json",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("offset", offset, nullable=True)
            .add_query("limit", limit, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_speedtest_files(
        self,
        api_version: str,
        test_length: Union[str, None] = SENTINEL,
        region: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets CDN speedtest files. This can be used for speedtesting TorBox for users or other usages, such as checking download speeds for verification. Provides all necessary data such as region, server name, and even coordinates. Uses the requesting IP to determine if the server is the closest to the user. You also have the ability to choose between long tests or short tests via the "test_length" parameter. You may also force the region selection by passing the "region" as a specific region. ### Authorization None needed.

        :param api_version: api_version
        :type api_version: str
        :param test_length: Determines the size of the file used for the speedtest. May be "long" or "short". Optional., defaults to None
        :type test_length: str, optional
        :param region: Determines what cdns are returned. May be any region that TorBox is located in. To get this value, send a request without this value to determine all of the available regions that are available., defaults to None
        :type region: str, optional
        :param user_ip: Pass a user's IP to get the closest server to them, otherwise will use the calling IP for location., defaults to None
        :type user_ip: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(test_length, "test_length")
        Validator(str).is_optional().is_nullable().validate(region, "region")
        Validator(str).is_optional().is_nullable().validate(user_ip, "user_ip")

        resolved_config = self._get_resolved_config(
            self._get_speedtest_files_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/speedtest",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("test_length", test_length, nullable=True)
            .add_query("region", region, nullable=True)
            .add_query("user_ip", user_ip, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_rss_notification_feed(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> str:
        """### Overview Gets your notifications in an RSS Feed which allows you to use them with RSS Feed readers or notification services that can take RSS Feeds and listen to updates. As soon as a notification goes to your account, it will be added to your feed. ### Authorization Requires an API key using as a query parameter using the `token` key.

        :param api_version: api_version
        :type api_version: str
        :param token: The user's API key., defaults to None
        :type token: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: str
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(token, "token")

        resolved_config = self._get_resolved_config(
            self._get_rss_notification_feed_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/rss",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("token", token, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_notification_feed(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Gets your notifications in a JSON object that is easily parsable compared to the RSS Feed. Gives all the same data as the RSS Feed. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_notification_feed_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/mynotifications",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def clear_all_notifications(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Marks all of your notifications as read and deletes them permanently. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._clear_all_notifications_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/clear",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def clear_single_notification(
        self,
        api_version: str,
        notification_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Marks a single notification as read and permanently deletes it from your notifications. Requires a `notification_id` which can be found by getting your notification feed. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param notification_id: notification_id
        :type notification_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).validate(notification_id, "notification_id")

        resolved_config = self._get_resolved_config(
            self._clear_single_notification_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/clear/{{notification_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_path("notification_id", notification_id)
            .serialize()
            .set_method("POST")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def send_test_notification(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Sends a test notification to all enabled notification types. This can be useful for validating setups. No need for any body in this request. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._send_test_notification_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/notifications/test",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def refresh_api_token(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview If you want a new API token, or your old one has been compromised, you may request a new one. If you happen to forget the token, go the [TorBox settings page ](https://torbox.app/settings) and copy the current one. If this still doesn't work, you may contact us at our support email for a new one. ### Authorization Requires an API key using the Authorization Bearer Header as well as passing the `session_token` from the website to be passed in the body. You can find the `session_token` in the localStorage of your browser on any TorBox.app page under the key `torbox_session_token`. This is a temporary token that only lasts for 1 hour, which is why it is used here to verify the identity of a user as well as their API token.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._refresh_api_token_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/refreshtoken",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_user_data(
        self,
        api_version: str,
        settings: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets a users account data and information. ### Plans `0` is Free plan `1` is Essential plan (_$3 plan_) `2` is Pro plan (_$10 plan_) `3` is Standard plan (_$5 plan_) ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param settings: Allows you to retrieve user settings., defaults to None
        :type settings: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(settings, "settings")

        resolved_config = self._get_resolved_config(
            self._get_user_data_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/me",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("settings", settings, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def add_referral_to_account(
        self,
        api_version: str,
        referral: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Automatically adds a referral code to the user's account. This can be used for developers to automatically add their referral to user's accounts who use their service. This will not override any referral a user already has. If they already have one, then it cannot be changed using this endpoint. It can only be done by the user on the [website](https://torbox.app/subscription). ### Authorization Requires an API key using the Authorization Bearer Header. Use the user's API key, not your own.

        :param api_version: api_version
        :type api_version: str
        :param referral: A referral code. Must be UUID., defaults to None
        :type referral: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(referral, "referral")

        resolved_config = self._get_resolved_config(
            self._add_referral_to_account_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/addreferral",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("referral", referral, nullable=True)
            .serialize()
            .set_method("POST")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_confirmation_code(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Requests a 6 digit code to be sent to the user's email for verification. Used to verify a user actually wants to perform a potentially dangerous action. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_confirmation_code_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/getconfirmation",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def start_device_code_authorization_process(
        self,
        api_version: str,
        app: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Starts the device code authorization process. Returns all the necessary information to complete the rest of the flow. This includes the following: - `device_code` - The code your app will use for consecutive requests for getting the user token. - `code` - This is the 6 digit code that you show to the user to be entered at the following verification_url. - `verification_url` - This url which you will show as a QR code. - `friendly_verification_url` - The friendly short url which you can show as plain text to user if they cannot use the QR code method. You may also submit the `app` parameter to this request to show your app name on the `verification_url` page. This concretes user trust in authorizing your application to use their TorBox account. This is not required, but is a good idea. Default is "Third Party App". This name is also only allowed to be alpha-numeric characters (_A-Z,0-9_). Anything else will be filtered our when being shown to the user. The `friendly_verification_url` will always show "Third Party App" to keep the URL short. The device_code is only valid for 10 minutes. Make sure the user is aware of this time limit so they submit and login before this time limit is over. ### Authorization None required.

        :param api_version: api_version
        :type api_version: str
        :param app: The app name that the user will see when verifying the code. This should be the name of your app., defaults to None
        :type app: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(app, "app")

        resolved_config = self._get_resolved_config(
            self._start_device_code_authorization_process_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/auth/device/start",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("app", app, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_token_from_device_code_process(
        self,
        request_body: GetTokenFromDeviceCodeProcessRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets the user's API token from the device code authorization process. This endpoint is expected to be polled in interval until it returns success, or until the expiry has passed. All data you need for this request is in the [original request](https://www.postman.com/wamy-dev/workspace/torbox/request/29572726-744bc274-88b7-4faf-a833-e30573c8c1e0?action=share&creator=29572726&ctx=documentation), which includes the interval to be polled by, the expiry time to stop at, and `device_code` to be sent to the API to get the correct data. ### Authorization None required.

        :param request_body: The request body.
        :type request_body: GetTokenFromDeviceCodeProcessRequest
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(GetTokenFromDeviceCodeProcessRequest).is_nullable().validate(
            request_body, "request_body"
        )
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_token_from_device_code_process_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/auth/device/token",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_referral_data(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Use this endpoint to get the user's referral data. This includes information such as how many referrals they have made, and their referral code. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_referral_data_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/referraldata",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_subscriptions(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Gets a users subscriptions. This includes active and inactive subscriptions for all payment processors. It should be noted that "plan_code" is not normalized to the standard plan codes such as 1, 2, or 3. These "plan_code"s are payment processor specific and used internally. If you want to display these subscriptions, use the "plan_name". For displaying information to users, use the "status", "gateway", and "plan_name". No other information is relevant to the user, and the rest is used for TorBox internally. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_subscriptions_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/subscriptions",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_transactions(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Use this endpoint to get the user's list of transactions. This data isn't exactly relevant to a third party developer, unless you want to build full parity with TorBox's dashboard, or simply want to show this information. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_transactions_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/transactions",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_transaction_pdf(
        self,
        api_version: str,
        transaction_id: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Generates a PDF of the transaction information. Requires the transaction ID from the "Get Transactions" request. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param transaction_id: The transaction ID that you want to generate the PDF for., defaults to None
        :type transaction_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(
            transaction_id, "transaction_id"
        )

        resolved_config = self._get_resolved_config(
            self._get_transaction_pdf_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/transaction/pdf",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("transaction_id", transaction_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def edit_user_settings(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Edits a user's TorBox settings. These values take effect immediately. Please view the body to read about allowed options and parameters. To get the user settings, simply use the "[Get User Data](https://www.postman.com/torbox/workspace/torbox-api/request/29572726-a3775d9b-f3ee-49cd-98a4-fc909ed2923b?action=share&source=copy-link&creator=29572726)" endpoint, while sending the "?settings=true" parameter ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._edit_user_settings_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/settings/editsettings",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_user_stats(
        self,
        api_version: str,
        general: Union[str, None] = SENTINEL,
        bandwidth: Union[str, None] = SENTINEL,
        bandwidth_grouping: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets a users stats. This data is currently split into two sections, "general" and "bandwidth". General shows general data, such as "Total Data Downloaded", "Total Data Egress", "Overall Ratio", and "Total Downloaded". Bandwidth shows the amount of bandwidth a user has downloaded within the past 30 days. We don't store this data for longer than 30 days, and it can be made more or less granular. Makes cool graphs! ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param general: Retrieve general stats., defaults to None
        :type general: str, optional
        :param bandwidth: Retrieve bandwidth stats., defaults to None
        :type bandwidth: str, optional
        :param bandwidth_grouping: If the "bandwidth" query parameter is sent, this value is used. Allowed is "hour", "day", "week", and "month", this narrates how bandwidth is grouped. More granular shows more information., defaults to None
        :type bandwidth_grouping: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(general, "general")
        Validator(str).is_optional().is_nullable().validate(bandwidth, "bandwidth")
        Validator(str).is_optional().is_nullable().validate(
            bandwidth_grouping, "bandwidth_grouping"
        )

        resolved_config = self._get_resolved_config(
            self._get_user_stats_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/user/stats",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("general", general, nullable=True)
            .add_query("bandwidth", bandwidth, nullable=True)
            .add_query("bandwidth_grouping", bandwidth_grouping, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def add_rss_feed(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Allows adding an RSS feed to your account. This API gives you a lot of customization options, but is best used with the UI on the website. This endpoint only works for Pro users (plan: 2). ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._add_rss_feed_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/rss/addrss",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def control_rss_feed(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Controls an RSS Feed. By sending the RSS feed's ID and the type of operation you want to perform, it will perform said action on the RSS feed checker. Operations are either: - **Update** `forces an update on the rss feed` - **Delete** `deletes the rss feed from your account permanently. This also deletes all associated RSS feed items. This does not remove queued items spawned from the RSS feed.` - **Pause** `pauses checking the rss feed on the scan interval` - **Resume** `resumes a paused rss feed` ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._control_rss_feed_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/rss/controlrss",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def edit_rss_feed(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Allows you to edit the RSS feed based on the RSS feed ID passed. Allows you to change everything about an RSS feed, except for the URL. When updating the "rss_type" or the "torrent_seeding" options, it will update all of the RSS items associated with the RSS feed, including all previous items. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._edit_rss_feed_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/rss/modifyrss",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_user_rss_feeds(
        self,
        api_version: str,
        id_: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets all of a user's RSS feeds located on their account. Can only be accessed on a Pro (plan: 2) account. Also allows you to get a specific by passing an "id" in the parameters. ##### Type Key The "type" key in the response is used for showing what type of downloads are spawned from this RSS feed. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct. - **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.` - "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.` - "webdl" `uses generic links and adds as a web download when downloaded.` ##### Status Key The "status" key tells the user selected status of the RSS feed. These statuses are **not** the same as the status key for the RSS items associated with the RSS feed. Each feed also includes a "status_message" key which gives a user friendly message about anything about the RSS feed, such as errors and explainations. - "active" `the RSS feed is set to be scraped.` - "paused" `the RSS feed will not be scraped as it is paused by the user.` - "error" `the RSS feed had an error while scraping, and cannot continue.` ##### State Key The "state" key tells you exactly in real time, what the RSS feed is doing. This is useful for realtime status updates. - "idle" `the RSS feed is idle, and is currently not doing anything in the current moment.` - "scraping" `the RSS feed is currently scraping new RSS items.` - "downloading" `the RSS feed is currently downloading the newly scraped RSS items.` ##### Torrent Seeding Key The "torrent_seeding" key is returned with every response, regardless of the type of the RSS feed. This controls what seeding setting the RSS feed is using when it adds new torrents. These are the same options as when adding a torrent using the /torrent/createtorrent endpoint. > Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings. - 1 `auto, the torrent will seed based on what the user has in their settings.` - 2 `always, TorBox will be instructed to seed this torrent regardless of any other settings.` - 3 `never, TorBox will not seed this torrent.` ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param id_: A specific RSS feed ID that you want to retrieve. Optional., defaults to None
        :type id_: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(id_, "id_")

        resolved_config = self._get_resolved_config(
            self._get_user_rss_feeds_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/rss/getfeeds",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("id", id_, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_rss_feed_items(
        self,
        api_version: str,
        rss_feed_id: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets the first 10,000 RSS feed items associated with an RSS feed. RSS feed items are scraped items from the RSS feed. They contain a direct download link as well as the content name, and additional information. ##### Type Key The "type" key in the response is used for showing what type of downloads this RSS feed item is. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct. When the parent RSS feed's type is changed, it changes all of the items types as well. - **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.` - "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.` - "webdl" `uses generic links and adds as a web download when downloaded.` ##### Status Key The "status" key tells the status of the RSS feed item. This is useful for seeing what the item is doing, and what it will do next. Each item also includes a "status_message" key which gives a user friendly message about anything about the RSS feed item, such as errors and explainations. - "new" `the RSS feed item is set to be downloaded.` - "ignored" `the RSS feed item has been ignored due to the parents RSS feed settings, as it doesn't match the chosen settings. The item will not be downloaded.` - "error" `the RSS feed item had an error while attempting to download. The item will be retried on the next scrape.` - "downloaded" `the RSS feed item has already been downloaded to the user's account. It will not be downloaded again.` ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param rss_feed_id: The RSS Feed ID of the RSS Feed you want to retrieve the scraped items of., defaults to None
        :type rss_feed_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(rss_feed_id, "rss_feed_id")

        resolved_config = self._get_resolved_config(
            self._get_rss_feed_items_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/rss/getfeeditems",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("rss_feed_id", rss_feed_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_all_jobs(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Gets all the jobs attached to a user account. This is good for an overall view of the jobs, such as on a dashboard, or something similar. ### Statuses - "pending" -> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._get_all_jobs_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/integration/jobs",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_specific_job(
        self,
        api_version: str,
        job_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets a specifc job using the Job's ID. To get the ID, you will have to Get All Jobs, and get the ID you want. ### Statuses - "pending" -> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param job_id: job_id
        :type job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).validate(job_id, "job_id")

        resolved_config = self._get_resolved_config(
            self._get_specific_job_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/integration/job/{{job_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_path("job_id", job_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_all_jobs_by_hash(
        self, api_version: str, hash: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """### Overview Gets all jobs that match a specific hash. Good for checking on specific downloads such as a download page, that could contain a lot of jobs. ### Statuses - "pending" -> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param hash: hash
        :type hash: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).validate(hash, "hash")

        resolved_config = self._get_resolved_config(
            self._get_all_jobs_by_hash_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/integration/jobs/{{hash}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_path("hash", hash)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def cancel_specific_job(
        self,
        api_version: str,
        job_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Cancels a job or deletes the job. Cancels while in progess (pending, uploading), or deletes the job any other time. It will delete it from the database completely. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param job_id: job_id
        :type job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).validate(job_id, "job_id")

        resolved_config = self._get_resolved_config(
            self._cancel_specific_job_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/integration/job/{{job_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_path("job_id", job_id)
            .serialize()
            .set_method("DELETE")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_queued_downloads(
        self,
        api_version: str,
        bypass_cache: Union[str, None] = SENTINEL,
        id_: Union[str, None] = SENTINEL,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        type_: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Retrieves all of a user's queued downloads by type. If you want to get all 3 types, "torrent", "usenet" and "webdl" then you will need to run this request 3 times, each with the different type. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param bypass_cache: Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls., defaults to None
        :type bypass_cache: str, optional
        :param id_: Determines the queued download requested, will return an object rather than list. Optional., defaults to None
        :type id_: str, optional
        :param offset: Determines the offset of items to get from the database. Default is 0. Optional., defaults to None
        :type offset: str, optional
        :param limit: Determines the number of items to recieve per request. Default is 1000. Optional., defaults to None
        :type limit: str, optional
        :param type_: The type of the queued download you want to retrieve. Can be "torrent", "usenet" or "webdl". Optional. Default is "torrent"., defaults to None
        :type type_: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(
            bypass_cache, "bypass_cache"
        )
        Validator(str).is_optional().is_nullable().validate(id_, "id_")
        Validator(str).is_optional().is_nullable().validate(offset, "offset")
        Validator(str).is_optional().is_nullable().validate(limit, "limit")
        Validator(str).is_optional().is_nullable().validate(type_, "type_")

        resolved_config = self._get_resolved_config(
            self._get_queued_downloads_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/queued/getqueued",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("bypass_cache", bypass_cache, nullable=True)
            .add_query("id", id_, nullable=True)
            .add_query("offset", offset, nullable=True)
            .add_query("limit", limit, nullable=True)
            .add_query("type", type_, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def control_queued_downloads(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent. Operations are either: - **Delete** `deletes the queued download from your account` - **Start** `starts a queued download, cannot be used with the "all" parameter` ### Authorization Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body.
        :type request_body: dict
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(dict).is_nullable().validate(request_body, "request_body")
        Validator(str).validate(api_version, "api_version")

        resolved_config = self._get_resolved_config(
            self._control_queued_downloads_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/queued/controlqueued",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def create_stream(
        self,
        api_version: str,
        id_: Union[str, None] = SENTINEL,
        file_id: Union[str, None] = SENTINEL,
        type_: Union[str, None] = SENTINEL,
        chosen_subtitle_index: Union[str, None] = SENTINEL,
        chosen_audio_index: Union[str, None] = SENTINEL,
        chosen_resolution_index: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Creates a new stream based off of the data provided. #### Selecting Subtitles and Audios We use indexes to determine which audio and subtitle you would like to select. To view all available indexes, you must request this endpoint intially with "null" or 0, for the chosen indexes. This will return a metadata dictionary in the response, which will contain the list of audios and subtitles available for this stream. When choosing a subtitle or audio stream, use the **relative index**, starting from 0, rather than the "index" value. This is important for selecting the correct index. Once your user gets a selection of audios and subtitles available, you can submit this to the endpoint again to get the chosen stream. - **null** - Selecting no subtitle. Not available for audio as one must always be selected. - **0** - Selecting first subtitle or audio #### Selecting Resolution Similar to the subtitles and audios, we use indexes to determine the resolution chosen. Unlike the above, these are predetermined. We do not upscale video, so if for example, you pass a 1080p video, and request it with resolution, 7, it will stay at 1080p. Please see the below for options. - **null** - Original video resolution. No downscaling will take place. - **0** - 144p - **1** - 240p - **2** - 360p - **3** - 480p - **4** - 720p - **5** - 1080p - **6** - 1440p - **7** - 2160p #### Types This endpoint allows you to handle torrents, usenet and web downloads all in one. This is why the "type" parameter is available. It defaults to "torrent". - **torrent** - Torrents - **usenet** - Usenet downloads - **webdownload** - Web Downloads #### Important Notes - Only text based subtitles are supported. If a non-text based subtitle is selected, it will be ignored. - If a subtitle or audio index does not exist on the stream, it will be ignored. - There are a lot of edge-case videos, if something doesn't work, don't hesitate to report the download hash and file_id of the failing video file. - This is a **Pro** only feature. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param id_: The ID of the type of download., defaults to None
        :type id_: str, optional
        :param file_id: The file ID inside of the download you would like to stream., defaults to None
        :type file_id: str, optional
        :param type_: The type of download that this is. If choosing the incorrect one, the ID will be incorrect., defaults to None
        :type type_: str, optional
        :param chosen_subtitle_index: The relative index of the subtitle you would like to stream. This is default null for none. 0 is the first subtitle found., defaults to None
        :type chosen_subtitle_index: str, optional
        :param chosen_audio_index: The relative index of the subtitle you would like to stream. Defaults to 0 for the first audio stream found inside the file. Cannot be null., defaults to None
        :type chosen_audio_index: str, optional
        :param chosen_resolution_index: The index of the resolution you would like to stream. This is default null for original., defaults to None
        :type chosen_resolution_index: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(id_, "id_")
        Validator(str).is_optional().is_nullable().validate(file_id, "file_id")
        Validator(str).is_optional().is_nullable().validate(type_, "type_")
        Validator(str).is_optional().is_nullable().validate(
            chosen_subtitle_index, "chosen_subtitle_index"
        )
        Validator(str).is_optional().is_nullable().validate(
            chosen_audio_index, "chosen_audio_index"
        )
        Validator(str).is_optional().is_nullable().validate(
            chosen_resolution_index, "chosen_resolution_index"
        )

        resolved_config = self._get_resolved_config(
            self._create_stream_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/stream/createstream",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("id", id_, nullable=True)
            .add_query("file_id", file_id, nullable=True)
            .add_query("type", type_, nullable=True)
            .add_query("chosen_subtitle_index", chosen_subtitle_index, nullable=True)
            .add_query("chosen_audio_index", chosen_audio_index, nullable=True)
            .add_query(
                "chosen_resolution_index", chosen_resolution_index, nullable=True
            )
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_stream_data(
        self,
        api_version: str,
        presigned_token: Union[str, None] = SENTINEL,
        token: Union[str, None] = SENTINEL,
        chosen_subtitle_index: Union[str, None] = SENTINEL,
        chosen_audio_index: Union[str, None] = SENTINEL,
        chosen_resolution_index: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """### Overview Gets stream data from an already created stream. Requires the presigned token and user API token from the original request. ### Authorization Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param presigned_token: The presigned token given from the original, /createstream request., defaults to None
        :type presigned_token: str, optional
        :param token: The user's API token, can also be used from the original, /createstream request., defaults to None
        :type token: str, optional
        :param chosen_subtitle_index: The chosen subtitle index that you are requesting information about., defaults to None
        :type chosen_subtitle_index: str, optional
        :param chosen_audio_index: The chosen audio index that you are requesting information about., defaults to None
        :type chosen_audio_index: str, optional
        :param chosen_resolution_index: The index of the resolution you would like to stream. This is default null for original., defaults to None
        :type chosen_resolution_index: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(api_version, "api_version")
        Validator(str).is_optional().is_nullable().validate(
            presigned_token, "presigned_token"
        )
        Validator(str).is_optional().is_nullable().validate(token, "token")
        Validator(str).is_optional().is_nullable().validate(
            chosen_subtitle_index, "chosen_subtitle_index"
        )
        Validator(str).is_optional().is_nullable().validate(
            chosen_audio_index, "chosen_audio_index"
        )
        Validator(str).is_optional().is_nullable().validate(
            chosen_resolution_index, "chosen_resolution_index"
        )

        resolved_config = self._get_resolved_config(
            self._get_stream_data_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.API_BASE.url or Environment.DEFAULT.url}/{{api_version}}/api/stream/getstreamdata",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("api_version", api_version)
            .add_query("presigned_token", presigned_token, nullable=True)
            .add_query("token", token, nullable=True)
            .add_query("chosen_subtitle_index", chosen_subtitle_index, nullable=True)
            .add_query("chosen_audio_index", chosen_audio_index, nullable=True)
            .add_query(
                "chosen_resolution_index", chosen_resolution_index, nullable=True
            )
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response
