from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class RssFeedsService(BaseService):

    @cast_models
    def add_rss_feed(self, api_version: str, request_body: any = None) -> Any:
        """### Overview

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
                f"{self.base_url}/{{api_version}}/api/rss/addrss",
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
    def control_rss_feed(self, api_version: str, request_body: any = None) -> Any:
        """### Overview

        Controls an RSS Feed. By sending the RSS feed's ID and the type of operation you want to perform, it will perform said action on the RSS feed checker.

        Operations are either:

        - **Update** `forces an update on the rss feed`
        - **Delete** `deletes the rss feed from your account permanently`

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
                f"{self.base_url}/{{api_version}}/api/rss/controlrss",
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
    def modify_rss_feed(self, api_version: str, request_body: any = None) -> Any:
        """### Overview

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
                f"{self.base_url}/{{api_version}}/api/rss/modifyrss",
                self.get_default_headers(),
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return response
