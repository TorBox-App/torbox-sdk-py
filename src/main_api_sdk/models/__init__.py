"""Lazy model exports.

Names are resolved on first attribute access via PEP 562 ``__getattr__``,
then cached in module globals. Avoids the multi-second eager-import cost
on SDKs with thousands of generated models.
"""

import importlib
import typing

import pydantic

from .utils import base_model as _base_model

# Names a model annotation can mention besides a model class. Pydantic re-evaluates an INHERITED
# annotation that needs a forward ref in the SUBCLASS's module, not the base's, so a fernMode
# `<Union>_<Variant>` subclass of a model declaring ``children: List[AstNodeInput]`` looks for
# ``List`` in the union's module -- which has no reason to import it. Supplying them through the
# rebuild namespace covers every such name at once. Module globals are layered on top, so a schema
# that happens to be named ``Field`` still wins.
_BUILTIN_NAMESPACE = {
    "typing": typing,
    "Annotated": typing.Annotated,
    "Any": typing.Any,
    "Dict": typing.Dict,
    "List": typing.List,
    "Literal": typing.Literal,
    "Optional": typing.Optional,
    "Union": typing.Union,
    "Field": pydantic.Field,
    "TypeAdapter": pydantic.TypeAdapter,
    "UniqueItems": _base_model.UniqueItems,
}

_MODEL_TO_MODULE = {
    "CreateTorrentRequest": "create_torrent_request",
    "AsyncCreateTorrentRequest": "async_create_torrent_request",
    "MainApiSdkRequestDownloadLinksPostRequest1": "main_api_sdk_request_download_links_post_request_1",
    "GetTorrentCachedAvailabilityBatchRequest": "get_torrent_cached_availability_batch_request",
    "GetTorrentInfoRequest": "get_torrent_info_request",
    "EditTorrentItemRequest": "edit_torrent_item_request",
    "MagnetToFileRequest": "magnet_to_file_request",
    "CreateUsenetDownloadRequest": "create_usenet_download_request",
    "MainApiSdkRequestDownloadLinksPostRequest2": "main_api_sdk_request_download_links_post_request_2",
    "GetUsenetCachedAvailabilityBatchRequest": "get_usenet_cached_availability_batch_request",
    "EditUsenetItemRequest": "edit_usenet_item_request",
    "CreateWebDownloadRequest": "create_web_download_request",
    "MainApiSdkRequestDownloadLinksPostRequest3": "main_api_sdk_request_download_links_post_request_3",
    "GetWebDownloadCachedAvailabilityBatchRequest": "get_web_download_cached_availability_batch_request",
    "EditWebDownloadItemRequest": "edit_web_download_item_request",
    "GetTokenFromDeviceCodeProcessRequest": "get_token_from_device_code_process_request",
}

_REBUILD_NAMES = frozenset(
    {
        "CreateTorrentRequest",
        "AsyncCreateTorrentRequest",
        "MainApiSdkRequestDownloadLinksPostRequest1",
        "GetTorrentCachedAvailabilityBatchRequest",
        "GetTorrentInfoRequest",
        "EditTorrentItemRequest",
        "MagnetToFileRequest",
        "CreateUsenetDownloadRequest",
        "MainApiSdkRequestDownloadLinksPostRequest2",
        "GetUsenetCachedAvailabilityBatchRequest",
        "EditUsenetItemRequest",
        "CreateWebDownloadRequest",
        "MainApiSdkRequestDownloadLinksPostRequest3",
        "GetWebDownloadCachedAvailabilityBatchRequest",
        "EditWebDownloadItemRequest",
        "GetTokenFromDeviceCodeProcessRequest",
    }
)

__all__ = list(_MODEL_TO_MODULE.keys())

_rebuilt = False


def _load(name):
    module = _MODEL_TO_MODULE.get(name)
    if module is None:
        return None
    obj = getattr(importlib.import_module("." + module, __name__), name)
    globals()[name] = obj
    return obj


def _rebuild(cls, ns):
    """Rebuild ``cls``, loading on demand whatever its forward refs still need.

    A deferred model can forward-reference a name that is not itself a
    BaseModel — a module-level ``Union`` alias is the common case — and
    no amount of rebuilding the BaseModels brings that alias into ``ns``.
    Pydantic names the one it is missing, so load exactly that and retry
    rather than eagerly importing every model, which is the cost this
    module exists to avoid.

    ``PydanticUndefinedAnnotation`` carries ``.name``; the ``name in ns``
    guard is what terminates the loop, since ``_load`` either adds the
    name or there is nothing more to try. The bound on the iteration count
    is a second belt: it holds even if a future pydantic reports a name
    that never equals the key inserted for it, which would otherwise hang
    an SDK rather than fail it.
    """
    for _ in range(len(_MODEL_TO_MODULE) + 1):
        try:
            # _types_namespace is mandatory: pydantic resolves forward refs
            # against caller-frame locals by default, but we're calling from
            # inside a helper — the names live in this module's globals.
            cls.model_rebuild(_types_namespace=ns)
            return
        except pydantic.PydanticUndefinedAnnotation as missing:
            name = missing.name
            if name in ns:
                return
            try:
                obj = _load(name)
            except Exception:
                return
            if obj is None:
                return
            ns[name] = obj
        except Exception:
            return


def _ensure_rebuilt():
    """Resolve forward refs across every BaseModel in one batched pass.

    Individual model files import their cross-references inside a
    ``TYPE_CHECKING`` block, so at runtime each file's globals contain
    only itself. ``model_rebuild()`` walks the call stack to find
    forward-ref names — calling it from this module once every
    BaseModel has been loaded into our globals is what lets pydantic
    resolve circular refs (the same shape the prior eager-import form
    relied on). Enums, Union types, and error models stay lazy until a
    rebuild asks for one.
    """
    global _rebuilt
    if _rebuilt:
        return
    _rebuilt = True
    for name in _REBUILD_NAMES:
        if name not in globals():
            try:
                _load(name)
            except Exception:
                pass
    ns = dict(_BUILTIN_NAMESPACE)
    ns.update(globals())
    for name in _REBUILD_NAMES:
        cls = globals().get(name)
        if cls is None:
            continue
        _rebuild(cls, ns)


def __getattr__(name):
    if name not in _MODEL_TO_MODULE:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    obj = _load(name)
    if name in _REBUILD_NAMES:
        _ensure_rebuilt()
    return obj


def __dir__():
    return sorted(set(globals()).union(_MODEL_TO_MODULE))
