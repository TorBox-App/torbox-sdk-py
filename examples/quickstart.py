"""TORBOX_API_KEY=... python examples/quickstart.py"""
import os

from torbox import TorBox, TorBoxError

client = TorBox(api_key=os.environ["TORBOX_API_KEY"])
me = client.user.get_user_data()
print("signed in as", me.email)

for torrent in client.paginate(client.torrents.get_torrent_list, page_size=100):
    print(torrent.id, torrent.name, torrent.download_state)

try:
    client.torrents.create_torrent(magnet="magnet:?xt=urn:btih:0000000000000000000000000000000000000000")
except TorBoxError as e:
    print("could not add:", e.status, e.error, e.detail)
