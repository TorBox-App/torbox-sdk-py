"""Runs against a Prism mock of the spec: TORBOX_MOCK_URL=http://127.0.0.1:4011 pytest"""
import os

import pytest

from torbox import TorBox, TorBoxError

MOCK = os.environ.get("TORBOX_MOCK_URL", "http://127.0.0.1:4011")
KEY = "00000000-0000-4000-8000-000000000001"


@pytest.fixture
def client():
    return TorBox(api_key=KEY, base_url=MOCK, timeout=10, max_retries=0)


def test_envelope_is_unwrapped(client):
    me = client.user.get_user_data()
    assert me is not None and not hasattr(me, "success")
    assert me.email


def test_multipart_upload(client):
    data = client.torrents.create_torrent(file=("test.torrent", b"d8:announce0:e"))
    assert data.torrent_id is not None


def test_download_link_takes_the_key_as_token(client):
    link = client.torrents.request_torrent_download_link(torrent_id=1, file_id=0)
    assert isinstance(link, str)


def test_errors_are_typed(client):
    with pytest.raises(TorBoxError) as info:
        client.user.get_user_data(_headers={"Prefer": "code=401"})
    assert info.value.status == 401
    assert info.value.error in ("BAD_TOKEN", "NO_AUTH")
    assert info.value.detail


def test_paginate(client):
    items = list(client.paginate(client.torrents.get_torrent_list, page_size=1000))
    assert isinstance(items, list)
