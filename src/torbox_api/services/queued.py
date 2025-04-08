from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models


class QueuedService(BaseService):

    @cast_models
    def get_queued_downloads(
        self,
        api_version: str,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
        offset: str = SENTINEL,
        limit: str = SENTINEL,
        type_: str = SENTINEL,
    ) -> None:
        """### Overview

        Retrieves all of a user's queued downloads by type. If you want to get all 3 types, "torrent", "usenet" and "webdl" then you will need to run this request 3 times, each with the different type.

        ### Authorization

        Requires an API key using the Authorization Bearer Header.

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
        """

        Validator(str).validate(api_version)
        Validator(str).is_optional().validate(bypass_cache)
        Validator(str).is_optional().validate(id_)
        Validator(str).is_optional().validate(offset)
        Validator(str).is_optional().validate(limit)
        Validator(str).is_optional().validate(type_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/queued/getqueued",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .add_query("bypass_cache", bypass_cache)
            .add_query("id", id_)
            .add_query("offset", offset)
            .add_query("limit", limit)
            .add_query("type", type_)
            .serialize()
            .set_method("GET")
        )

        self.send_request(serialized_request)

    @cast_models
    def control_queued_downloads(
        self, api_version: str, request_body: any = None
    ) -> None:
        """### Overview

        Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent.

        Operations are either:

        - **Delete** `deletes the queued download from your account`

        - **Start** `starts a queued download, cannot be used with the "all" parameter`


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
                f"{self.base_url or Environment.DEFAULT.url}/{{api_version}}/api/queued/controlqueued",
                [self.get_access_token()],
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        self.send_request(serialized_request)
