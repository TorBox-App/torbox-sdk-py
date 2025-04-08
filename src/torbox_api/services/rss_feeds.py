from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models


class RssFeedsService(BaseService):

    @cast_models
    def add_rss_feed(self, api_version: str, request_body: any = None) -> None:
        """### Overview

        Allows adding an RSS feed to your account. This API gives you a lot of customization options, but is best used with the UI on the website. This endpoint only works for Pro users (plan: 2).

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
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/rss/addrss",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def control_rss_feed(self, api_version: str, request_body: any = None) -> None:
        """### Overview

        Controls an RSS Feed. By sending the RSS feed's ID and the type of operation you want to perform, it will perform said action on the RSS feed checker.

        Operations are either:

        - **Update** `forces an update on the rss feed`
        - **Delete** `deletes the rss feed from your account permanently. This also deletes all associated RSS feed items. This does not remove queued items spawned from the RSS feed.`
        - **Pause** `pauses checking the rss feed on the scan interval`
        - **Resume** `resumes a paused rss feed`


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
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/rss/controlrss",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def modify_rss_feed(self, api_version: str, request_body: any = None) -> None:
        """### Overview

        Allows you to edit the RSS feed based on the RSS feed ID passed. Allows you to change everything about an RSS feed, except for the URL.

        When updating the "rss_type" or the "torrent_seeding" options, it will update all of the RSS items associated with the RSS feed, including all previous items.

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
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/rss/modifyrss",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def get_user_rss_feeds(self, api_version: str, id_: str = SENTINEL) -> None:
        """### Overview

        Gets all of a user's RSS feeds located on their account. Can only be accessed on a Pro (plan: 2) account. Also allows you to get a specific by passing an "id" in the parameters.

        ##### Type Key

        The "type" key in the response is used for showing what type of downloads are spawned from this RSS feed. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct.

        - **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.`
        - "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.`
        - "webdl" `uses generic links and adds as a web download when downloaded.`


        ##### Status Key

        The "status" key tells the user selected status of the RSS feed. These statuses are **not** the same as the status key for the RSS items associated with the RSS feed. Each feed also includes a "status_message" key which gives a user friendly message about anything about the RSS feed, such as errors and explainations.

        - "active" `the RSS feed is set to be scraped.`
        - "paused" `the RSS feed will not be scraped as it is paused by the user.`

        - "error" `the RSS feed had an error while scraping, and cannot continue.`


        ##### State Key

        The "state" key tells you exactly in real time, what the RSS feed is doing. This is useful for realtime status updates.

        - "idle" `the RSS feed is idle, and is currently not doing anything in the current moment.`
        - "scraping" `the RSS feed is currently scraping new RSS items.`
        - "downloading" `the RSS feed is currently downloading the newly scraped RSS items.`


        ##### Torrent Seeding Key

        The "torrent_seeding" key is returned with every response, regardless of the type of the RSS feed. This controls what seeding setting the RSS feed is using when it adds new torrents. These are the same options as when adding a torrent using the /torrent/createtorrent endpoint.

        > Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings.


        - 1 `auto, the torrent will seed based on what the user has in their settings.`
        - 2 `always, TorBox will be instructed to seed this torrent regardless of any other settings.`
        - 3 `never, TorBox will not seed this torrent.`


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param id_: A specific RSS feed ID that you want to retrieve. Optional., defaults to None
        :type id_: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/rss/getfeeds",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("id", id_)
            .serialize()
            .set_method("GET")
        )

        self.send_request(serialized_request)

    @cast_models
    def get_rss_feed_items(self, api_version: str, rss_feed_id: str = SENTINEL) -> None:
        """### Overview

        Gets the first 10,000 RSS feed items associated with an RSS feed. RSS feed items are scraped items from the RSS feed. They contain a direct download link as well as the content name, and additional information.

        ##### Type Key

        The "type" key in the response is used for showing what type of downloads this RSS feed item is. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct. When the parent RSS feed's type is changed, it changes all of the items types as well.

        - **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.`
        - "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.`
        - "webdl" `uses generic links and adds as a web download when downloaded.`


        ##### Status Key

        The "status" key tells the status of the RSS feed item. This is useful for seeing what the item is doing, and what it will do next. Each item also includes a "status_message" key which gives a user friendly message about anything about the RSS feed item, such as errors and explainations.

        - "new" `the RSS feed item is set to be downloaded.`
        - "ignored" `the RSS feed item has been ignored due to the parents RSS feed settings, as it doesn't match the chosen settings. The item will not be downloaded.`
        - "error" `the RSS feed item had an error while attempting to download. The item will be retried on the next scrape.`
        - "downloaded" `the RSS feed item has already been downloaded to the user's account. It will not be downloaded again.`


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param rss_feed_id: The RSS Feed ID of the RSS Feed you want to retrieve the scraped items of., defaults to None
        :type rss_feed_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(rss_feed_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/rss/getfeeditems",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("rss_feed_id", rss_feed_id)
            .serialize()
            .set_method("GET")
        )

        self.send_request(serialized_request)
