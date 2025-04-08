from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    CreateWebDownloadOkResponse,
    CreateWebDownloadRequest,
    GetHosterListOkResponse,
    GetWebDownloadListOkResponse,
)


class WebDownloadsDebridService(BaseService):

    @cast_models
    def create_web_download(
        self, api_version: str, request_body: CreateWebDownloadRequest = None
    ) -> CreateWebDownloadOkResponse:
        """### Overview

        Creates a web download under your account. Simply send a link to any file on the internet. Once it has been checked, it will begin downloading assuming your account has available active download slots, and they aren't too large.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: CreateWebDownloadRequest, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: CreateWebDownloadOkResponse
        """

        Validator(CreateWebDownloadRequest).is_optional().validate(request_body)
        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/createwebdownload",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return CreateWebDownloadOkResponse._unmap(response)

    @cast_models
    def control_web_download(
        self,
        api_version: str,
        request_body: any = None,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
    ) -> None:
        """### Overview

        Controls a web download. By sending the web download's ID and the type of operation you want to perform, it will send that request to the debrid client.

        Operations are either:

        - **Delete** `deletes the download from the client and your account permanently`


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: any, optional
        :param api_version: api_version
        :type api_version: str
        :param bypass_cache: bypass_cache, defaults to None
        :type bypass_cache: str, optional
        :param id_: Determines the web download requested, will return an object rather than list. Optional., defaults to None
        :type id_: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(bypass_cache)
        Validator(str).is_optional().validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/controlwebdownload",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("bypass_cache", bypass_cache)
            .add_query("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def request_download_link2(
        self,
        api_version: str,
        token: str = SENTINEL,
        web_id: str = SENTINEL,
        file_id: str = SENTINEL,
        zip_link: str = SENTINEL,
        torrent_file: str = SENTINEL,
        user_ip: str = SENTINEL,
        redirect: str = SENTINEL,
    ) -> None:
        """### Overview

        Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing.

        ### Permalinks

        Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard.

        ### Authorization

        Requires an API key as a parameter for the `token` parameter.

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
        :param torrent_file: If you want a .torrent file to be downloaded. Does not work with the zip_link option. Optional., defaults to None
        :type torrent_file: str, optional
        :param user_ip: The user's IP to determine the closest CDN. Optional., defaults to None
        :type user_ip: str, optional
        :param redirect: If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link., defaults to None
        :type redirect: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(token)
        Validator(str).is_optional().validate(web_id)
        Validator(str).is_optional().validate(file_id)
        Validator(str).is_optional().validate(zip_link)
        Validator(str).is_optional().validate(torrent_file)
        Validator(str).is_optional().validate(user_ip)
        Validator(str).is_optional().validate(redirect)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/requestdl",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("token", token)
            .add_query("web_id", web_id)
            .add_query("file_id", file_id)
            .add_query("zip_link", zip_link)
            .add_query("torrent_file", torrent_file)
            .add_query("user_ip", user_ip)
            .add_query("redirect", redirect)
            .serialize()
            .set_method("GET")
        )

        self.send_request(serialized_request)

    @cast_models
    def get_web_download_list(
        self,
        api_version: str,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
        offset: str = SENTINEL,
        limit: str = SENTINEL,
    ) -> GetWebDownloadListOkResponse:
        """### Overview

        Gets the user's web download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live web downloads.

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
        :return: The parsed response data.
        :rtype: GetWebDownloadListOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(bypass_cache)
        Validator(str).is_optional().validate(id_)
        Validator(str).is_optional().validate(offset)
        Validator(str).is_optional().validate(limit)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/mylist",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("bypass_cache", bypass_cache)
            .add_query("id", id_)
            .add_query("offset", offset)
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GetWebDownloadListOkResponse._unmap(response)

    @cast_models
    def get_web_download_cached_availability(
        self, api_version: str, hash: str = SENTINEL, format: str = SENTINEL
    ) -> None:
        """### Overview

        Takes in a list of comma separated usenet hashes and checks if the web download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as:
        `?hash=XXXX&hash=XXXX&hash=XXXX`

        or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX`
        and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour.

        You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below.

        To get the hash of a web download, pass the link through an md5 hash algo and it will return the proper hash for it.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param hash: The list of web hashes you want to check. Comma seperated. To find the hash, md5 the link., defaults to None
        :type hash: str, optional
        :param format: Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list., defaults to None
        :type format: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(hash)
        Validator(str).is_optional().validate(format)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/checkcached",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("hash", hash)
            .add_query("format", format)
            .serialize()
            .set_method("GET")
        )

        self.send_request(serialized_request)

    @cast_models
    def get_hoster_list(self, api_version: str) -> GetHosterListOkResponse:
        """### Overview

        A dynamic list of hosters that TorBox is capable of downloading through its paid service.

        - **Name** - a clean name for display use, the well known name of the service, should be recognizable to users.

        - **Domains** - an array of known domains that the hoster uses. While each may serve a different purpose it is still included.

        - **URL** - the main url of the service. This should take you to the home page or a service page of the hoster.

        - **Icon** - a square image, usually a favicon or logo, that represents the service, should be recognizable as the hoster's icon.

        - **Status** - whether this hoster can be used on TorBox or not at the current time. It is usually a good idea to check this value before submitting a download to TorBox's servers for download.

        - **Type** - values are either "hoster" or "stream". Both do the same thing, but is good to differentiate services used for different things.

        - **Note** - a string value (or null) that may give helpful information about the current status or state of a hoster. This can and should be shown to end users.

        - **Daily Link Limit** - the number of downloads a user can use per day. As a user submits links, once they hit this number, the API will deny them from adding anymore of this type of link. A zero value means that it is unlimited.

        - **Daily Link Used** - the number of downloads a user has already used. Usually zero unless you send authentication to the endpoint. This will return accurate values.

        - **Daily Bandwidth Limit** - the value in bytes that a user is allowed to download from this hoster. A zero value means that it is unlimited. It is recommended to use the Daily Link Limit instead.

        - **Daily Bandwidth Used** - the value in bytes that a user has already used to download from this hoster. Usually zero unless you send authentication to the endpoint. This will return accurate values.


        ### Authorization

        Optional authorization. Authorization is not required in this endpoint unless you want to get the user's live data. Requires an API key using the Authorization Bearer Header to get the live and accurate data for **Daily Link Used** and **Daily Bandwidth Used**.

        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetHosterListOkResponse
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/webdl/hosters",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GetHosterListOkResponse._unmap(response)
