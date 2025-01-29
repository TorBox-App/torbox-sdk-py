from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class AddReferralToAccountOkResponse(BaseModel):
    """AddReferralToAccountOkResponse

    :param data: data, defaults to None
    :type data: any, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: any = None,
        detail: str = None,
        error: any = None,
        success: bool = None,
        **kwargs
    ):
        """AddReferralToAccountOkResponse

        :param data: data, defaults to None
        :type data: any, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = data
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if success is not None:
            self.success = success
        self._kwargs = kwargs
