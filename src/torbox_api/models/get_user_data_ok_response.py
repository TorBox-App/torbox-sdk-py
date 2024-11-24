from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class Settings(BaseModel):
    """Settings

    :param anothersetting: anothersetting, defaults to None
    :type anothersetting: str, optional
    :param setting: setting, defaults to None
    :type setting: str, optional
    """

    def __init__(self, anothersetting: str = None, setting: str = None):
        """Settings

        :param anothersetting: anothersetting, defaults to None
        :type anothersetting: str, optional
        :param setting: setting, defaults to None
        :type setting: str, optional
        """
        if anothersetting is not None:
            self.anothersetting = anothersetting
        if setting is not None:
            self.setting = setting


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
        auth_id: str = None,
        base_email: str = None,
        cooldown_until: str = None,
        created_at: str = None,
        customer: str = None,
        email: str = None,
        id_: float = None,
        is_subscribed: bool = None,
        plan: float = None,
        premium_expires_at: str = None,
        server: float = None,
        settings: Settings = None,
        total_downloaded: float = None,
        updated_at: str = None,
        user_referral: str = None,
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
        if auth_id is not None:
            self.auth_id = auth_id
        if base_email is not None:
            self.base_email = base_email
        if cooldown_until is not None:
            self.cooldown_until = cooldown_until
        if created_at is not None:
            self.created_at = created_at
        if customer is not None:
            self.customer = customer
        if email is not None:
            self.email = email
        if id_ is not None:
            self.id_ = id_
        if is_subscribed is not None:
            self.is_subscribed = is_subscribed
        if plan is not None:
            self.plan = plan
        if premium_expires_at is not None:
            self.premium_expires_at = premium_expires_at
        if server is not None:
            self.server = server
        if settings is not None:
            self.settings = self._define_object(settings, Settings)
        if total_downloaded is not None:
            self.total_downloaded = total_downloaded
        if updated_at is not None:
            self.updated_at = updated_at
        if user_referral is not None:
            self.user_referral = user_referral


@JsonMap({})
class GetUserDataOkResponse(BaseModel):
    """GetUserDataOkResponse

    :param data: data, defaults to None
    :type data: GetUserDataOkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: GetUserDataOkResponseData = None,
        detail: str = None,
        success: bool = None,
    ):
        """GetUserDataOkResponse

        :param data: data, defaults to None
        :type data: GetUserDataOkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = self._define_object(data, GetUserDataOkResponseData)
        if detail is not None:
            self.detail = detail
        if success is not None:
            self.success = success
