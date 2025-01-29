# CreateTorrentRequest

**Properties**

| Name      | Type  | Required | Description                                                                                                                                                                                      |
| :-------- | :---- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| allow_zip | str   | ❌       | Tells TorBox if you want to allow this torrent to be zipped or not. TorBox only zips if the torrent is 100 files or larger.                                                                      |
| as_queued | str   | ❌       | Tells TorBox you want this torrent instantly queued. This is bypassed if user is on free plan, and will process the request as normal in this case. Optional.                                    |
| file      | bytes | ❌       | The torrent's torrent file. Optional.                                                                                                                                                            |
| magnet    | str   | ❌       | The torrent's magnet link. Optional.                                                                                                                                                             |
| name      | str   | ❌       | The name you want the torrent to be. Optional.                                                                                                                                                   |
| seed      | str   | ❌       | Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings. |
