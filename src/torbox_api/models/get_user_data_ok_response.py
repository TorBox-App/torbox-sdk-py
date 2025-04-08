from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class Settings(BaseModel):
    """Settings

    :param anothersetting: anothersetting, defaults to None
    :type anothersetting: str, optional
    :param setting: setting, defaults to None
    :type setting: str, optional
    """

    def __init__(
        self, anothersetting: str = SENTINEL, setting: str = SENTINEL, **kwargs
    ):
        """Settings

        :param anothersetting: anothersetting, defaults to None
        :type anothersetting: str, optional
        :param setting: setting, defaults to None
        :type setting: str, optional
        """
        if anothersetting is not SENTINEL:
            self.anothersetting = anothersetting
        if setting is not SENTINEL:
            self.setting = setting
        self._kwargs = kwargs


@JsonMap({"id_": "id"})
class GetUserDataOkResponseData(BaseModel):
    """GetUserDataOkResponseData

    :param auth_id: auth_id, defaults to None
    :type auth_id: str, optional
    :param base_email: base_email, defaults to None
    :type base_email: str, optional
    :param cooldown_until: cooldown_until, defaults to None
    :type cooldown_until: str, optional
    :param created_at: created_at, defaults to None
    :type created_at: str, optional
    :param customer: customer, defaults to None
    :type customer: str, optional
    :param email: email, defaults to None
    :type email: str, optional
    :param id_: id_, defaults to None
    :type id_: float, optional
    :param is_subscribed: is_subscribed, defaults to None
    :type is_subscribed: bool, optional
    :param plan: plan, defaults to None
    :type plan: float, optional
    :param premium_expires_at: premium_expires_at, defaults to None
    :type premium_expires_at: str, optional
    :param server: server, defaults to None
    :type server: float, optional
    :param settings: settings, defaults to None
    :type settings: Settings, optional
    :param total_downloaded: total_downloaded, defaults to None
    :type total_downloaded: float, optional
    :param updated_at: updated_at, defaults to None
    :type updated_at: str, optional
    :param user_referral: user_referral, defaults to None
    :type user_referral: str, optional
    """

    def __init__(
        self,
        auth_id: str = SENTINEL,
        base_email: str = SENTINEL,
        cooldown_until: str = SENTINEL,
        created_at: str = SENTINEL,
        customer: str = SENTINEL,
        email: str = SENTINEL,
        id_: float = SENTINEL,
        is_subscribed: bool = SENTINEL,
        plan: float = SENTINEL,
        premium_expires_at: str = SENTINEL,
        server: float = SENTINEL,
        settings: Settings = SENTINEL,
        total_downloaded: float = SENTINEL,
        updated_at: str = SENTINEL,
        user_referral: str = SENTINEL,
        **kwargs
    ):
        """GetUserDataOkResponseData

        :param auth_id: auth_id, defaults to None
        :type auth_id: str, optional
        :param base_email: base_email, defaults to None
        :type base_email: str, optional
        :param cooldown_until: cooldown_until, defaults to None
        :type cooldown_until: str, optional
        :param created_at: created_at, defaults to None
        :type created_at: str, optional
        :param customer: customer, defaults to None
        :type customer: str, optional
        :param email: email, defaults to None
        :type email: str, optional
        :param id_: id_, defaults to None
        :type id_: float, optional
        :param is_subscribed: is_subscribed, defaults to None
        :type is_subscribed: bool, optional
        :param plan: plan, defaults to None
        :type plan: float, optional
        :param premium_expires_at: premium_expires_at, defaults to None
        :type premium_expires_at: str, optional
        :param server: server, defaults to None
        :type server: float, optional
        :param settings: settings, defaults to None
        :type settings: Settings, optional
        :param total_downloaded: total_downloaded, defaults to None
        :type total_downloaded: float, optional
        :param updated_at: updated_at, defaults to None
        :type updated_at: str, optional
        :param user_referral: user_referral, defaults to None
        :type user_referral: str, optional
        """
        if auth_id is not SENTINEL:
            self.auth_id = auth_id
        if base_email is not SENTINEL:
            self.base_email = base_email
        if cooldown_until is not SENTINEL:
            self.cooldown_until = cooldown_until
        if created_at is not SENTINEL:
            self.created_at = created_at
        if customer is not SENTINEL:
            self.customer = customer
        if email is not SENTINEL:
            self.email = email
        if id_ is not SENTINEL:
            self.id_ = id_
        if is_subscribed is not SENTINEL:
            self.is_subscribed = is_subscribed
        if plan is not SENTINEL:
            self.plan = plan
        if premium_expires_at is not SENTINEL:
            self.premium_expires_at = premium_expires_at
        if server is not SENTINEL:
            self.server = server
        if settings is not SENTINEL:
            self.settings = self._define_object(settings, Settings)
        if total_downloaded is not SENTINEL:
            self.total_downloaded = total_downloaded
        if updated_at is not SENTINEL:
            self.updated_at = updated_at
        if user_referral is not SENTINEL:
            self.user_referral = user_referral
        self._kwargs = kwargs


@JsonMap({})
class GetUserDataOkResponse(BaseModel):
    """GetUserDataOkResponse

    :param data: data, defaults to None
    :type data: GetUserDataOkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: GetUserDataOkResponseData = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """GetUserDataOkResponse

        :param data: data, defaults to None
        :type data: GetUserDataOkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = self._define_object(data, GetUserDataOkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs
