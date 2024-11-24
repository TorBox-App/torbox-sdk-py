from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import GetStatsOkResponse, GetUpStatusOkResponse


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
        :return: Get Up Status Success
        :rtype: GetUpStatusOkResponse
        """

        serialized_request = (
            Serializer(f"{self.base_url}/", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
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
        :return: Get Stats Success
        :rtype: GetStatsOkResponse
        """

        Validator(str).validate(api_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{api_version}}/api/stats", self.get_default_headers()
            )
            .add_path("api_version", api_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return GetStatsOkResponse._unmap(response)
