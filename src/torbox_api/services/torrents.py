from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    ControlQueuedTorrentOkResponse,
    ControlTorrentOkResponse,
    CreateTorrentOkResponse,
    CreateTorrentRequest,
    ExportTorrentDataOkResponse,
    GetTorrentCachedAvailabilityOkResponse,
    GetTorrentInfoOkResponse,
    GetTorrentListOkResponse,
    RequestDownloadLinkOkResponse,
    SearchAllTorrentsFromScraperOkResponse,
)


class TorrentsService(BaseService):

    @cast_models
    def create_torrent(
        self, api_version: str, request_body: CreateTorrentRequest = None
    ) -> CreateTorrentOkResponse:
        """### Overview

        Creates a torrent under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large.


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: CreateTorrentRequest, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Create Torrent Success / Create Torrent Queued / Create Torrent Active Limit Fail
        :rtype: CreateTorrentOkResponse
        """

        Validator(CreateTorrentRequest).is_optional().validate(request_body)
        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/createtorrent",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response = self.send_request(serialized_request)
        return CreateTorrentOkResponse._unmap(response)

    @cast_models
    def control_torrent(
        self, api_version: str, request_body: any = None
    ) -> ControlTorrentOkResponse:
        """### Overview

        Controls a torrent. By sending the torrent's ID and the type of operation you want to perform, it will send that request to the torrent client.

        Operations are either:

        - **Reannounce** `reannounces the torrent to get new peers`

        - **Delete** `deletes the torrent from the client and your account permanently`

        - **Resume** `resumes a paused torrent`


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: any, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Control Torrent Success
        :rtype: ControlTorrentOkResponse
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/controltorrent",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return ControlTorrentOkResponse._unmap(response)

    @cast_models
    def control_queued_torrent(
        self, api_version: str, request_body: any = None
    ) -> ControlQueuedTorrentOkResponse:
        """### Overview

        Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent.

        Operations are either:

        - **Delete** `deletes the queued torrent from your account`


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: any, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Control Torrent Success
        :rtype: ControlQueuedTorrentOkResponse
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/controlqueued",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return ControlQueuedTorrentOkResponse._unmap(response)

    @cast_models
    def request_download_link(
        self,
        api_version: str,
        token: str = None,
        torrent_id: str = None,
        file_id: str = None,
        zip_link: str = None,
        torrent_file: str = None,
    ) -> RequestDownloadLinkOkResponse:
        """### Overview

        Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 1 hour for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

        ### Authorization

        Requires an API key as a parameter for the `token` parameter.

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
        :param torrent_file: If you want a .torrent file to be downloaded. Does not work with the zip_link option. Optional., defaults to None
        :type torrent_file: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Request Download Link Success
        :rtype: RequestDownloadLinkOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(token)
        Validator(str).is_optional().validate(torrent_id)
        Validator(str).is_optional().validate(file_id)
        Validator(str).is_optional().validate(zip_link)
        Validator(str).is_optional().validate(torrent_file)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/requestdl",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .add_query("token", token)
            .add_query("torrent_id", torrent_id)
            .add_query("file_id", file_id)
            .add_query("zip_link", zip_link)
            .add_query("torrent_file", torrent_file)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return RequestDownloadLinkOkResponse._unmap(response)

    @cast_models
    def get_torrent_list(
        self,
        api_version: str,
        bypass_cache: str = None,
        id_: str = None,
        offset: str = None,
        limit: str = None,
    ) -> GetTorrentListOkResponse:
        """### Overview

        Gets the user's torrent list. This gives you the needed information to perform other torrent actions. This information only gets updated every 600 seconds, or when the _Request Update On Torrent_ request is sent to the _relay API_.

        #### Download States:

        - "downloading" -> The torrent is currently downloading.

        - "uploading" -> The torrent is currently seeding.

        - "stalled (no seeds)" -> The torrent is trying to download, but there are no seeds connected to download from.

        - "paused" -> The torrent is paused.

        - "completed" -> The torrent is completely downloaded. Do not use this for download completion status.

        - "cached" -> The torrent is cached from the server.

        - "metaDL" -> The torrent is downloading metadata from the hoard.

        - "checkingResumeData" -> The torrent is checking resumable data.


        All other statuses are basic qBittorrent states. [Check out here for the full list](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management).

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

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
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Get Torrent List Success
        :rtype: GetTorrentListOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(bypass_cache)
        Validator(str).is_optional().validate(id_)
        Validator(str).is_optional().validate(offset)
        Validator(str).is_optional().validate(limit)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/mylist",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .add_query("bypass_cache", bypass_cache)
            .add_query("id", id_)
            .add_query("offset", offset)
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return GetTorrentListOkResponse._unmap(response)

    @cast_models
    def get_torrent_cached_availability(
        self,
        api_version: str,
        hash: str = None,
        format: str = None,
        list_files: str = None,
    ) -> GetTorrentCachedAvailabilityOkResponse:
        """### Overview

        Takes in a list of comma separated torrent hashes and checks if the torrent is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as:
        `?hash=XXXX&hash=XXXX&hash=XXXX`

        or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX`
        and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour.

        You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

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
        :return: Get Torrent Cached Availability List With FIles Success / Get Torrent Cached Availability List Success / Get Torrent Cached Availability Object Success / Get Torrent Cached Availability Success Uncached
        :rtype: GetTorrentCachedAvailabilityOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(hash)
        Validator(str).is_optional().validate(format)
        Validator(str).is_optional().validate(list_files)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/checkcached",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .add_query("hash", hash)
            .add_query("format", format)
            .add_query("list_files", list_files)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return GetTorrentCachedAvailabilityOkResponse._unmap(response)

    @cast_models
    def search_all_torrents_from_scraper(
        self, api_version: str, query: str = None
    ) -> SearchAllTorrentsFromScraperOkResponse:
        """### Overview

        Uses Meilisearch to search for scraped torrents. This is a basic torrent aggregator system and has no real relation to TorBox. It is simply a tool you can use. It does not have cache information, or anything special like that, and will not have any of that information. This is simply a torrent search, nothing more.

        You may use this for anything. TorBox uses it in the website to make it easy for users to find torrents without having to go and find them on sketchy websites.

        ### Authorization

        None required.

        :param api_version: api_version
        :type api_version: str
        :param query: The query you want to search for., defaults to None
        :type query: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Search All Torrents From Scraper Success
        :rtype: SearchAllTorrentsFromScraperOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(query)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/search",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .add_query("query", query)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return SearchAllTorrentsFromScraperOkResponse._unmap(response)

    @cast_models
    def export_torrent_data(
        self, api_version: str, torrent_id: str = None, type_: str = None
    ) -> ExportTorrentDataOkResponse:
        """### Overview

        Exports the magnet or torrent file. Requires a type to be passed. If type is **magnet**, it will return a JSON response with the magnet as a string in the _data_ key. If type is **file**, it will return a bittorrent file as a download. Not compatible with cached downloads.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param torrent_id: The torrent's ID., defaults to None
        :type torrent_id: str, optional
        :param type_: Either "magnet" or "file". Tells how the API what to get, and what to respond as. If magnet, it returns a JSON response with the magnet as a string in the data key. If file, it responds with a torrent file download., defaults to None
        :type type_: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Export Torrent Data Magnet / Export Torrent Data File Success
        :rtype: ExportTorrentDataOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(torrent_id)
        Validator(str).is_optional().validate(type_)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/exportdata",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .add_query("torrent_id", torrent_id)
            .add_query("type", type_)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return ExportTorrentDataOkResponse._unmap(response)

    @cast_models
    def get_torrent_info(
        self, api_version: str, hash: str = None, timeout: str = None
    ) -> GetTorrentInfoOkResponse:
        """### Overview

        A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant.

        ### Authorization

        None required.

        :param api_version: api_version
        :type api_version: str
        :param hash: Hash of the torrent you want to get info for. This is required., defaults to None
        :type hash: str, optional
        :param timeout: The amount of time you want TorBox to search for the torrent on the Bittorrent network. If the number of seeders is low or even zero, this value may be helpful to move up. Default is 10. Optional., defaults to None
        :type timeout: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Get Torrent Info Success
        :rtype: GetTorrentInfoOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(hash)
        Validator(str).is_optional().validate(timeout)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/torrents/torrentinfo",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .add_query("hash", hash)
            .add_query("timeout", timeout)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return GetTorrentInfoOkResponse._unmap(response)

    @cast_models
    def get_queued_torrents(self, api_version: str) -> Any:
        """### Overview

        Retrieves all of a user's queued torrents.

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
                f"{self.base_url}/{{api_version}}/api/torrents/getqueued",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response
