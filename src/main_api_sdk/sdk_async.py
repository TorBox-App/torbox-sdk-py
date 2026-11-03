import requests
import logging
from typing import Optional, Union
from .net.environment import Environment
from .sdk import MainApiSdk
from .services.async_.main_api_sdk import MainApiSdkServiceAsync


class MainApiSdkAsync(MainApiSdk):
    """
    MainApiSdkAsync is the asynchronous version of the MainApiSdk SDK Client.
    """

    def __init__(
        self,
        *,
        access_token: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: float = None,
        timeout_ms: int = None,
        http_client: Optional[requests.Session] = None,
        follow_redirects: bool = True,
        logger: Optional[logging.Logger] = None,
        retry: "RetryConfig" = None,
    ):
        super().__init__(
            access_token=access_token,
            base_url=base_url,
            timeout=timeout,
            timeout_ms=timeout_ms,
            http_client=http_client,
            follow_redirects=follow_redirects,
            logger=logger,
            retry=retry,
        )

        self.main_api_sdk = MainApiSdkServiceAsync(
            base_url=self._base_url,
            http_client=http_client,
            follow_redirects=follow_redirects,
            logger=logger,
        )
        if retry is not None:
            self.set_retry(retry)
