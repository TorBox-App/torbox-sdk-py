from typing import Any, Dict, TypedDict, Optional, Union

from ..net.environment import Environment


class RetryConfig(TypedDict, total=False):
    """
    Configuration for retry behavior.

    :ivar int attempts: Maximum number of retry attempts.
    :ivar int delay_ms: Delay in milliseconds between retries.
    :ivar int max_delay_ms: Maximum delay in milliseconds between retries (caps exponential backoff).
    :ivar float backoff_factor: Multiplier for exponential backoff (e.g., 2.0 for doubling delay each retry).
    :ivar int jitter_ms: Maximum random jitter in milliseconds to add to retry delays.
    :ivar list[int] status_codes_to_retry: Specific HTTP status codes to retry (overrides default 5xx + 408, 429).
    :ivar list[str] http_methods_to_retry: HTTP methods to retry (e.g., ['GET', 'POST']).
    :ivar int max_retry_after_delay_ms: Upper bound (ms) for a server-directed retry delay parsed from Retry-After / X-RateLimit-Reset response headers.
    """

    attempts: int
    delay_ms: int
    max_delay_ms: int
    backoff_factor: float
    jitter_ms: int
    status_codes_to_retry: list[int]
    http_methods_to_retry: list[str]
    max_retry_after_delay_ms: int


class ValidationConfig(TypedDict, total=False):
    """
    Configuration for response validation.

    :ivar bool response_validation: Whether to validate responses against schemas.
    """

    response_validation: bool


# What the SDK was generated with (`validateResponses`). Only the DEFAULT: `response_validation`
# is a documented runtime key, so a caller must be able to move it in either direction.
RESPONSE_VALIDATION_DEFAULT = True


def should_validate_response(resolved_config: Optional["SdkConfig"] = None) -> bool:
    """
    Whether a response should be validated against its declared schema.

    Lives next to the ``ValidationConfig`` declaration so the key's only reader sits with its
    definition. Turning validation off is the standard mitigation when a server drifts from its
    spec -- an extra enum member, a widened range -- because otherwise every response fails
    client-side and the SDK is unusable until the spec is corrected.

    An absent key falls back to the generated default rather than being read as False, so a
    partial ``validation`` dict does not silently disable validation.

    :param SdkConfig resolved_config: The configuration resolved for this request.
    :return: True when the response should be validated.
    :rtype: bool
    """
    validation = (resolved_config or {}).get("validation") or {}
    configured = validation.get("response_validation")
    return RESPONSE_VALIDATION_DEFAULT if configured is None else bool(configured)


class SdkConfig(TypedDict, total=False):
    """
    Configuration dictionary for SDK, service, method, and request-level overrides.

    Hierarchy (highest to lowest priority):
    - Request config (passed directly to method call)
    - Method config (set via set_<method_name>_config())
    - Service config (set via set_config())
    - SDK config (set at initialization)

    :ivar Union[Environment, str] base_url: Base URL for API requests. Can be a string URL or Environment enum. Wins over ``environment`` when both are set.
    :ivar Union[Environment, str] environment: Base URL for API requests, expressed as an Environment enum member. Used only when ``base_url`` is not set at this or a higher-priority scope.
    :ivar float timeout: Request timeout in seconds.
    :ivar Dict[str, str] additional_headers: Extra headers merged into every request in scope. They override headers the SDK already set for the request (authentication, User-Agent, spec-declared header parameters) but not the body's Content-Type.
    :ivar str token: Bearer token for authentication.
    :ivar str access_token: Access token for authentication (alias for token).
    :ivar RetryConfig retry: Retry configuration.
    :ivar ValidationConfig validation: Validation configuration.
    """

    base_url: Union[Environment, str]
    environment: Union[Environment, str]
    timeout: float
    additional_headers: Dict[str, str]
    token: str
    access_token: str
    retry: RetryConfig
    validation: ValidationConfig
