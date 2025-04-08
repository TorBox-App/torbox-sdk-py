from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    CreateUsenetDownloadOkResponse,
    CreateUsenetDownloadRequest,
    GetUsenetListOkResponse,
)


class UsenetService(BaseService):

    @cast_models
    def create_usenet_download(
        self, api_version: str, request_body: CreateUsenetDownloadRequest = None
    ) -> CreateUsenetDownloadOkResponse:
        """### Overview

        Creates a usenet download under your account. Simply send **either** a link, or an nzb file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large.

        #### Post Processing Options:

        All post processing options that the Usenet client will perform before TorBox's own processing to make the files available. It is recommended you either don't send this parameter, or keep it at `-1` for default, which will give only the wanted files.

        - `-1`, Default. This runs repairs, and extractions as well as deletes the source files leaving only the wanted downloaded files.

        - `0`, None. No post-processing at all. Just download all the files (including all PAR2). TorBox will still do its normal processing to make the download available, but no repairs, or extraction will take place.

        - `1`, Repair. Download files and do a PAR2 verification. If the verification fails, download more PAR2 files and attempt to repair the files.

        - `2`, Repair and Unpack. Download all files, do a PAR2 verification and unpack the files. The final folder will also include the RAR and ZIP files.

        - `3`, Repair, Unpack and Delete. Download all files, do a PAR2 verification, unpack the files to the final folder and delete the source files.


        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param request_body: The request body., defaults to None
        :type request_body: CreateUsenetDownloadRequest, optional
        :param api_version: api_version
        :type api_version: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: CreateUsenetDownloadOkResponse
        """

        Validator(CreateUsenetDownloadRequest).is_optional().validate(request_body)
        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/createusenetdownload",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return CreateUsenetDownloadOkResponse._unmap(response)

    @cast_models
    def control_usenet_download(
        self, api_version: str, request_body: any = None
    ) -> None:
        """### Overview

        Controls a usenet download. By sending the usenet download's ID and the type of operation you want to perform, it will send that request to the usenet client.

        Operations are either:

        - **Delete** `deletes the nzb from the client and your account permanently`

        - **Pause** `pauses a nzb's download`

        - **Resume** `resumes a paused usenet download`


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
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/controlusenetdownload",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)

    @cast_models
    def request_download_link1(
        self,
        api_version: str,
        token: str = SENTINEL,
        usenet_id: str = SENTINEL,
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
        :param usenet_id: The usenet download's ID that you want to download, defaults to None
        :type usenet_id: str, optional
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
        Validator(str).is_optional().validate(usenet_id)
        Validator(str).is_optional().validate(file_id)
        Validator(str).is_optional().validate(zip_link)
        Validator(str).is_optional().validate(torrent_file)
        Validator(str).is_optional().validate(user_ip)
        Validator(str).is_optional().validate(redirect)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/requestdl",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("token", token)
            .add_query("usenet_id", usenet_id)
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
    def get_usenet_list(
        self,
        api_version: str,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
        offset: str = SENTINEL,
        limit: str = SENTINEL,
    ) -> GetUsenetListOkResponse:
        """### Overview

        Gets the user's usenet download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live usenet downloads.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param bypass_cache: Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls., defaults to None
        :type bypass_cache: str, optional
        :param id_: Determines the usenet download requested, will return an object rather than list. Optional., defaults to None
        :type id_: str, optional
        :param offset: Determines the offset of items to get from the database. Default is 0. Optional., defaults to None
        :type offset: str, optional
        :param limit: Determines the number of items to recieve per request. Default is 1000. Optional., defaults to None
        :type limit: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetUsenetListOkResponse
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(bypass_cache)
        Validator(str).is_optional().validate(id_)
        Validator(str).is_optional().validate(offset)
        Validator(str).is_optional().validate(limit)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/mylist",
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
        return GetUsenetListOkResponse._unmap(response)

    @cast_models
    def get_usenet_cached_availability(
        self, api_version: str, hash: str = SENTINEL, format: str = SENTINEL
    ) -> None:
        """### Overview

        Takes in a list of comma separated usenet hashes and checks if the usenet download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as:
        `?hash=XXXX&hash=XXXX&hash=XXXX`

        or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX`
        and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour.

        You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below.

        To get the hash of a usenet download, pass the link or file through an md5 hash algo and it will return the proper hash for it.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

        :param api_version: api_version
        :type api_version: str
        :param hash: The list of usenet hashes you want to check. Comma seperated. To find the hash, md5 the link of the usenet link or file., defaults to None
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
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/usenet/checkcached",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("hash", hash)
            .add_query("format", format)
            .serialize()
            .set_method("GET")
        )

        self.send_request(serialized_request)
