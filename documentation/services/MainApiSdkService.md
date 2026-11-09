# MainApiSdkService

A list of all methods in the `MainApiSdkService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_torrent](#create_torrent)                                                         | ### Overview Creates a torrent under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. ### Rate Limits This endpoint has two limits that apply at the same time: - **300 requests per minute:** a shared ceiling that _every_ request counts against, whether the torrent is cached or uncached. - **60 uncached torrents per hour:** an additional, stricter limit that only uncached torrents count against. The important thing is that cached and uncached requests both draw from the same 300/min pool, but uncached requests _also_ draw from their own separate 60/hour pool. An uncached request therefore counts twice: once against the per-minute limit, and once against the per-hour uncached limit. **Example:** In a single minute you add 250 cached + 50 uncached torrents. That's 300 total, so you've hit the per-minute limit for that minute. But those 50 uncached torrents also came out of your 60/hour uncached budget, leaving only **10 uncached torrents** for the remaining 59 minutes of that hour. (You could still add plenty more _cached_ torrents during that hour, since cached requests aren't capped hourly: only by the 300/min ceiling.) ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [async_create_torrent](#async_create_torrent)                                             | ### Overview Creates a torrent asynchrously under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. The request will return instantly, not returning any data other than a success message. This is the same for failures, as they will return the error in the background, rather than immediately. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [control_torrent](#control_torrent)                                                       | ### Overview Controls a torrent. By sending the torrent's ID and the type of operation you want to perform, it will send that request to the torrent client. Operations are either: - **Reannounce** `reannounces the torrent to get new peers` - **Delete** `deletes the torrent from the client and your account permanently` - **Resume** `resumes a paused torrent` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [request_download_link](#request_download_link)                                           | ### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [request_download_links_get](#request_download_links_get)                                 | ### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [request_download_links_post](#request_download_links_post)                               | ### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_torrent_list](#get_torrent_list)                                                     | ### Overview Gets the user's torrent list. This gives you the needed information to perform other torrent actions. This information only gets updated every 600 seconds, or when the _Request Update On Torrent_ request is sent to the _relay API_. #### Download States: - "downloading" -\> The torrent is currently downloading. - "uploading" -\> The torrent is currently seeding. - "stalled (no seeds)" -\> The torrent is trying to download, but there are no seeds connected to download from. - "paused" -\> The torrent is paused. - "completed" -\> The torrent is completely downloaded. Do not use this for download completion status. - "cached" -\> The torrent is cached from the server. - "metaDL" -\> The torrent is downloading metadata from the hoard. - "checkingResumeData" -\> The torrent is checking resumable data. All other statuses are basic qBittorrent states. [Check out here for the full list](<https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management>). ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [get_torrent_cached_availability](#get_torrent_cached_availability)                       | ### Overview Takes in a list of comma separated torrent hashes and checks if the torrent is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [get_torrent_cached_availability_batch](#get_torrent_cached_availability_batch)           | ### Overview Takes in a list of comma separated torrent hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [export_torrent_data](#export_torrent_data)                                               | ### Overview Exports the magnet or torrent file. Requires a type to be passed. If type is **magnet**, it will return a JSON response with the magnet as a string in the _data_ key. If type is **file**, it will return a bittorrent file as a download. Not compatible with cached downloads. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_torrent_info](#get_torrent_info)                                                     | ### Overview A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant. **It is not recommended to use this for checking TorBox's cache. Please use the GET /checkcache endpoint instead.** ### Authorization None required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [get_torrent_info_1](#get_torrent_info_1)                                                 | ### Overview Same as the GET route, but allows posting data such as magnet, and torrent files. Hashes will have precedence over magnets, and magnets will have precedence over torrent files. Only proper torrent files are accepted. At least one of hash, magnet, or torrent file is required. A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant. **It is not recommended to use this for checking TorBox's cache. Please use the GET /checkcache endpoint instead.** ### Authorization None required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [edit_torrent_item](#edit_torrent_item)                                                   | ### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [magnet_to_file](#magnet_to_file)                                                         | ### Overview Converts any magnet to a torrent file. Does not require the magnet to be on your TorBox account or in the TorBox cache. Free endpoint for public use. ### Authorization None required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [create_usenet_download](#create_usenet_download)                                         | ### Overview Creates a usenet download under your account. Simply send **either** a link, or an nzb file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. #### Post Processing Options: All post processing options that the Usenet client will perform before TorBox's own processing to make the files available. It is recommended you either don't send this parameter, or keep it at `-1` for default, which will give only the wanted files. - `-1`, Default. This runs repairs, and extractions as well as deletes the source files leaving only the wanted downloaded files. - `0`, None. No post-processing at all. Just download all the files (including all PAR2). TorBox will still do its normal processing to make the download available, but no repairs, or extraction will take place. - `1`, Repair. Download files and do a PAR2 verification. If the verification fails, download more PAR2 files and attempt to repair the files. - `2`, Repair and Unpack. Download all files, do a PAR2 verification and unpack the files. The final folder will also include the RAR and ZIP files. - `3`, Repair, Unpack and Delete. Download all files, do a PAR2 verification, unpack the files to the final folder and delete the source files. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [control_usenet_download](#control_usenet_download)                                       | ### Overview Controls a usenet download. By sending the usenet download's ID and the type of operation you want to perform, it will send that request to the usenet client. Operations are either: - **Delete** `deletes the nzb from the client and your account permanently` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [request_download_link_1](#request_download_link_1)                                       | ### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [request_download_links_get_1](#request_download_links_get_1)                             | ### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [request_download_links_post_1](#request_download_links_post_1)                           | ### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_usenet_list](#get_usenet_list)                                                       | ### Overview Gets the user's usenet download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live usenet downloads. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [get_usenet_cached_availability](#get_usenet_cached_availability)                         | ### Overview Takes in a list of comma separated usenet hashes and checks if the usenet download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. To get the hash of a usenet download, you can read [this document](https://support.torbox.app/en/articles/13681109-technical-getting-hashes-for-searches) for all of the strategies. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_usenet_cached_availability_batch](#get_usenet_cached_availability_batch)             | ### Overview Takes in a list of comma separated hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [edit_usenet_item](#edit_usenet_item)                                                     | ### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [get_news_server_connection_information](#get_news_server_connection_information)         | ### Overview Gets the TorBox News Server Connection information. This is a static path, and is not dynamic. ### Authorization No authentication required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [get_news_server_account](#get_news_server_account)                                       | ### Overview Gets the user's TorBox News Server Account with authentication details. Does not show password if not creating the account. Account creation happens on the first request. If you need to get the password, or reset the password, use the `/usenet/provider/account/resetpw` `POST` endpoint. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [reset_news_server_account_password](#reset_news_server_account_password)                 | ### Overview Resets the user's TorBox News Server account password. This password is automatically generated, and is not saved, it is only shown once. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [create_web_download](#create_web_download)                                               | ### Overview Creates a web download under your account. Simply send a link to any file on the internet. Once it has been checked, it will begin downloading assuming your account has available active download slots, and they aren't too large. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [control_web_download](#control_web_download)                                             | ### Overview Controls a web download. By sending the web download's ID and the type of operation you want to perform, it will send that request to the debrid client. Operations are either: - **Delete** `deletes the download from the client and your account permanently` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [request_download_link_2](#request_download_link_2)                                       | ### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [request_download_links_get_2](#request_download_links_get_2)                             | ### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [request_download_links_post_2](#request_download_links_post_2)                           | ### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_web_download_list](#get_web_download_list)                                           | ### Overview Gets the user's web download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live web downloads. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [get_web_download_cached_availability](#get_web_download_cached_availability)             | ### Overview Takes in a list of comma separated usenet hashes and checks if the web download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. To get the hash of a web download you can read [this document](https://support.torbox.app/en/articles/13681109-technical-getting-hashes-for-searches) for all of the strategies. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [get_web_download_cached_availability_batch](#get_web_download_cached_availability_batch) | ### Overview Takes in a list of comma separated hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [get_hoster_list](#get_hoster_list)                                                       | ### Overview A dynamic list of hosters that TorBox is capable of downloading through its paid service. - **Name** - a clean name for display use, the well known name of the service, should be recognizable to users. - **Domains** - an array of known domains that the hoster uses. While each may serve a different purpose it is still included. - **URL** - the main url of the service. This should take you to the home page or a service page of the hoster. - **Icon** - a square image, usually a favicon or logo, that represents the service, should be recognizable as the hoster's icon. - **Status** - whether this hoster can be used on TorBox or not at the current time. It is usually a good idea to check this value before submitting a download to TorBox's servers for download. - **Type** - values are either "hoster" or "stream". Both do the same thing, but is good to differentiate services used for different things. - **Note** - a string value (or null) that may give helpful information about the current status or state of a hoster. This can and should be shown to end users. - **Daily Link Limit** - the number of downloads a user can use per day. As a user submits links, once they hit this number, the API will deny them from adding anymore of this type of link. A zero value means that it is unlimited. - **Daily Link Used** - the number of downloads a user has already used. Usually zero unless you send authentication to the endpoint. This will return accurate values. - **Daily Bandwidth Limit** - the value in bytes that a user is allowed to download from this hoster. A zero value means that it is unlimited. It is recommended to use the Daily Link Limit instead. - **Daily Bandwidth Used** - the value in bytes that a user has already used to download from this hoster. Usually zero unless you send authentication to the endpoint. This will return accurate values. ### Authorization Optional authorization. Authorization is not required in this endpoint unless you want to get the user's live data. Requires an API key using the Authorization Bearer Header to get the live and accurate data for **Daily Link Used** and **Daily Bandwidth Used**.                                                                                                                                                                                                                              |
| [edit_web_download_item](#edit_web_download_item)                                         | ### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [get_up_status](#get_up_status)                                                           | ### Overview Simply gets if the TorBox API is available for use or not. Also might include information about downtimes. ### Authorization None needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [get_stats](#get_stats)                                                                   | ### Overview Simply gets general stats about the TorBox service. ### Authorization None needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [get_changelogs_rss_feed](#get_changelogs_rss_feed)                                       | ### Overview Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for people who want updates on the TorBox changelog. Includes all the necessary items to make this compatible with RSS feed viewers for notifications, and proper HTML viewing. ### Authorization None needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [get_changelogs_json](#get_changelogs_json)                                               | ### Overview Gets most recent changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for developers who want to integrate the changelog into their apps for their users to see. Includes content in HTML for developers to easily render the text in a fancy yet simple way. ### Authorization None needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [get_speedtest_files](#get_speedtest_files)                                               | ### Overview Gets CDN speedtest files. This can be used for speedtesting TorBox for users or other usages, such as checking download speeds for verification. Provides all necessary data such as region, server name, and even coordinates. Uses the requesting IP to determine if the server is the closest to the user. You also have the ability to choose between long tests or short tests via the "test_length" parameter. You may also force the region selection by passing the "region" as a specific region. ### Authorization None needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [get_rss_notification_feed](#get_rss_notification_feed)                                   | ### Overview Gets your notifications in an RSS Feed which allows you to use them with RSS Feed readers or notification services that can take RSS Feeds and listen to updates. As soon as a notification goes to your account, it will be added to your feed. ### Authorization Requires an API key using as a query parameter using the `token` key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [get_notification_feed](#get_notification_feed)                                           | ### Overview Gets your notifications in a JSON object that is easily parsable compared to the RSS Feed. Gives all the same data as the RSS Feed. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [clear_all_notifications](#clear_all_notifications)                                       | ### Overview Marks all of your notifications as read and deletes them permanently. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [clear_single_notification](#clear_single_notification)                                   | ### Overview Marks a single notification as read and permanently deletes it from your notifications. Requires a `notification_id` which can be found by getting your notification feed. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [send_test_notification](#send_test_notification)                                         | ### Overview Sends a test notification to all enabled notification types. This can be useful for validating setups. No need for any body in this request. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [refresh_api_token](#refresh_api_token)                                                   | ### Overview If you want a new API token, or your old one has been compromised, you may request a new one. If you happen to forget the token, go the [TorBox settings page ](https://torbox.app/settings) and copy the current one. If this still doesn't work, you may contact us at our support email for a new one. ### Authorization Requires an API key using the Authorization Bearer Header as well as passing the `session_token` from the website to be passed in the body. You can find the `session_token` in the localStorage of your browser on any TorBox.app page under the key `torbox_session_token`. This is a temporary token that only lasts for 1 hour, which is why it is used here to verify the identity of a user as well as their API token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [get_user_data](#get_user_data)                                                           | ### Overview Gets a users account data and information. ### Plans `0` is Free plan `1` is Essential plan (_$3 plan_) `2` is Pro plan (_$10 plan_) `3` is Standard plan (_$5 plan_) ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [add_referral_to_account](#add_referral_to_account)                                       | ### Overview Automatically adds a referral code to the user's account. This can be used for developers to automatically add their referral to user's accounts who use their service. This will not override any referral a user already has. If they already have one, then it cannot be changed using this endpoint. It can only be done by the user on the [website](https://torbox.app/subscription). ### Authorization Requires an API key using the Authorization Bearer Header. Use the user's API key, not your own.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_confirmation_code](#get_confirmation_code)                                           | ### Overview Requests a 6 digit code to be sent to the user's email for verification. Used to verify a user actually wants to perform a potentially dangerous action. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [start_device_code_authorization_process](#start_device_code_authorization_process)       | ### Overview Starts the device code authorization process. Returns all the necessary information to complete the rest of the flow. This includes the following: - `device_code` - The code your app will use for consecutive requests for getting the user token. - `code` - This is the 6 digit code that you show to the user to be entered at the following verification*url. - `verification_url` - This url which you will show as a QR code. - `friendly_verification_url` - The friendly short url which you can show as plain text to user if they cannot use the QR code method. You may also submit the `app` parameter to this request to show your app name on the `verification_url` page. This concretes user trust in authorizing your application to use their TorBox account. This is not required, but is a good idea. Default is "Third Party App". This name is also only allowed to be alpha-numeric characters (\_A-Z,0-9*). Anything else will be filtered our when being shown to the user. The `friendly_verification_url` will always show "Third Party App" to keep the URL short. The device_code is only valid for 10 minutes. Make sure the user is aware of this time limit so they submit and login before this time limit is over. ### Authorization None required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [get_token_from_device_code_process](#get_token_from_device_code_process)                 | ### Overview Gets the user's API token from the device code authorization process. This endpoint is expected to be polled in interval until it returns success, or until the expiry has passed. All data you need for this request is in the [original request](https://www.postman.com/wamy-dev/workspace/torbox/request/29572726-744bc274-88b7-4faf-a833-e30573c8c1e0?action=share&creator=29572726&ctx=documentation), which includes the interval to be polled by, the expiry time to stop at, and `device_code` to be sent to the API to get the correct data. ### Authorization None required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [get_referral_data](#get_referral_data)                                                   | ### Overview Use this endpoint to get the user's referral data. This includes information such as how many referrals they have made, and their referral code. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [get_subscriptions](#get_subscriptions)                                                   | ### Overview Gets a users subscriptions. This includes active and inactive subscriptions for all payment processors. It should be noted that "plan_code" is not normalized to the standard plan codes such as 1, 2, or 3. These "plan_code"s are payment processor specific and used internally. If you want to display these subscriptions, use the "plan_name". For displaying information to users, use the "status", "gateway", and "plan_name". No other information is relevant to the user, and the rest is used for TorBox internally. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_transactions](#get_transactions)                                                     | ### Overview Use this endpoint to get the user's list of transactions. This data isn't exactly relevant to a third party developer, unless you want to build full parity with TorBox's dashboard, or simply want to show this information. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [get_transaction_pdf](#get_transaction_pdf)                                               | ### Overview Generates a PDF of the transaction information. Requires the transaction ID from the "Get Transactions" request. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [edit_user_settings](#edit_user_settings)                                                 | ### Overview Edits a user's TorBox settings. These values take effect immediately. Please view the body to read about allowed options and parameters. To get the user settings, simply use the "[Get User Data](https://www.postman.com/torbox/workspace/torbox-api/request/29572726-a3775d9b-f3ee-49cd-98a4-fc909ed2923b?action=share&source=copy-link&creator=29572726)" endpoint, while sending the "?settings=true" parameter ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [get_user_stats](#get_user_stats)                                                         | ### Overview Gets a users stats. This data is currently split into two sections, "general" and "bandwidth". General shows general data, such as "Total Data Downloaded", "Total Data Egress", "Overall Ratio", and "Total Downloaded". Bandwidth shows the amount of bandwidth a user has downloaded within the past 30 days. We don't store this data for longer than 30 days, and it can be made more or less granular. Makes cool graphs! ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [add_rss_feed](#add_rss_feed)                                                             | ### Overview Allows adding an RSS feed to your account. This API gives you a lot of customization options, but is best used with the UI on the website. This endpoint only works for Pro users (plan: 2). ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [control_rss_feed](#control_rss_feed)                                                     | ### Overview Controls an RSS Feed. By sending the RSS feed's ID and the type of operation you want to perform, it will perform said action on the RSS feed checker. Operations are either: - **Update** `forces an update on the rss feed` - **Delete** `deletes the rss feed from your account permanently. This also deletes all associated RSS feed items. This does not remove queued items spawned from the RSS feed.` - **Pause** `pauses checking the rss feed on the scan interval` - **Resume** `resumes a paused rss feed` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [edit_rss_feed](#edit_rss_feed)                                                           | ### Overview Allows you to edit the RSS feed based on the RSS feed ID passed. Allows you to change everything about an RSS feed, except for the URL. When updating the "rss_type" or the "torrent_seeding" options, it will update all of the RSS items associated with the RSS feed, including all previous items. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [get_user_rss_feeds](#get_user_rss_feeds)                                                 | ### Overview Gets all of a user's RSS feeds located on their account. Can only be accessed on a Pro (plan: 2) account. Also allows you to get a specific by passing an "id" in the parameters. ##### Type Key The "type" key in the response is used for showing what type of downloads are spawned from this RSS feed. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct. - **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.` - "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.` - "webdl" `uses generic links and adds as a web download when downloaded.` ##### Status Key The "status" key tells the user selected status of the RSS feed. These statuses are **not** the same as the status key for the RSS items associated with the RSS feed. Each feed also includes a "status_message" key which gives a user friendly message about anything about the RSS feed, such as errors and explainations. - "active" `the RSS feed is set to be scraped.` - "paused" `the RSS feed will not be scraped as it is paused by the user.` - "error" `the RSS feed had an error while scraping, and cannot continue.` ##### State Key The "state" key tells you exactly in real time, what the RSS feed is doing. This is useful for realtime status updates. - "idle" `the RSS feed is idle, and is currently not doing anything in the current moment.` - "scraping" `the RSS feed is currently scraping new RSS items.` - "downloading" `the RSS feed is currently downloading the newly scraped RSS items.` ##### Torrent Seeding Key The "torrent_seeding" key is returned with every response, regardless of the type of the RSS feed. This controls what seeding setting the RSS feed is using when it adds new torrents. These are the same options as when adding a torrent using the /torrent/createtorrent endpoint. \> Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings. - 1 `auto, the torrent will seed based on what the user has in their settings.` - 2 `always, TorBox will be instructed to seed this torrent regardless of any other settings.` - 3 `never, TorBox will not seed this torrent.` ### Authorization Requires an API key using the Authorization Bearer Header. |
| [get_rss_feed_items](#get_rss_feed_items)                                                 | ### Overview Gets the first 10,000 RSS feed items associated with an RSS feed. RSS feed items are scraped items from the RSS feed. They contain a direct download link as well as the content name, and additional information. ##### Type Key The "type" key in the response is used for showing what type of downloads this RSS feed item is. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct. When the parent RSS feed's type is changed, it changes all of the items types as well. - **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.` - "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.` - "webdl" `uses generic links and adds as a web download when downloaded.` ##### Status Key The "status" key tells the status of the RSS feed item. This is useful for seeing what the item is doing, and what it will do next. Each item also includes a "status_message" key which gives a user friendly message about anything about the RSS feed item, such as errors and explainations. - "new" `the RSS feed item is set to be downloaded.` - "ignored" `the RSS feed item has been ignored due to the parents RSS feed settings, as it doesn't match the chosen settings. The item will not be downloaded.` - "error" `the RSS feed item had an error while attempting to download. The item will be retried on the next scrape.` - "downloaded" `the RSS feed item has already been downloaded to the user's account. It will not be downloaded again.` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [get_all_jobs](#get_all_jobs)                                                             | ### Overview Gets all the jobs attached to a user account. This is good for an overall view of the jobs, such as on a dashboard, or something similar. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [get_specific_job](#get_specific_job)                                                     | ### Overview Gets a specifc job using the Job's ID. To get the ID, you will have to Get All Jobs, and get the ID you want. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [get_all_jobs_by_hash](#get_all_jobs_by_hash)                                             | ### Overview Gets all jobs that match a specific hash. Good for checking on specific downloads such as a download page, that could contain a lot of jobs. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [cancel_specific_job](#cancel_specific_job)                                               | ### Overview Cancels a job or deletes the job. Cancels while in progess (pending, uploading), or deletes the job any other time. It will delete it from the database completely. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [get_queued_downloads](#get_queued_downloads)                                             | ### Overview Retrieves all of a user's queued downloads by type. If you want to get all 3 types, "torrent", "usenet" and "webdl" then you will need to run this request 3 times, each with the different type. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [control_queued_downloads](#control_queued_downloads)                                     | ### Overview Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent. Operations are either: - **Delete** `deletes the queued download from your account` - **Start** `starts a queued download, cannot be used with the "all" parameter` ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [create_stream](#create_stream)                                                           | ### Overview Creates a new stream based off of the data provided. #### Selecting Subtitles and Audios We use indexes to determine which audio and subtitle you would like to select. To view all available indexes, you must request this endpoint intially with "null" or 0, for the chosen indexes. This will return a metadata dictionary in the response, which will contain the list of audios and subtitles available for this stream. When choosing a subtitle or audio stream, use the **relative index**, starting from 0, rather than the "index" value. This is important for selecting the correct index. Once your user gets a selection of audios and subtitles available, you can submit this to the endpoint again to get the chosen stream. - **null** - Selecting no subtitle. Not available for audio as one must always be selected. - **0** - Selecting first subtitle or audio #### Selecting Resolution Similar to the subtitles and audios, we use indexes to determine the resolution chosen. Unlike the above, these are predetermined. We do not upscale video, so if for example, you pass a 1080p video, and request it with resolution, 7, it will stay at 1080p. Please see the below for options. - **null** - Original video resolution. No downscaling will take place. - **0** - 144p - **1** - 240p - **2** - 360p - **3** - 480p - **4** - 720p - **5** - 1080p - **6** - 1440p - **7** - 2160p #### Types This endpoint allows you to handle torrents, usenet and web downloads all in one. This is why the "type" parameter is available. It defaults to "torrent". - **torrent** - Torrents - **usenet** - Usenet downloads - **webdownload** - Web Downloads #### Important Notes - Only text based subtitles are supported. If a non-text based subtitle is selected, it will be ignored. - If a subtitle or audio index does not exist on the stream, it will be ignored. - There are a lot of edge-case videos, if something doesn't work, don't hesitate to report the download hash and file_id of the failing video file. - This is a **Pro** only feature. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                       |
| [get_stream_data](#get_stream_data)                                                       | ### Overview Gets stream data from an already created stream. Requires the presigned token and user API token from the original request. ### Authorization Requires an API key using the Authorization Bearer Header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## create_torrent

### Overview Creates a torrent under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. ### Rate Limits This endpoint has two limits that apply at the same time: - **300 requests per minute:** a shared ceiling that _every_ request counts against, whether the torrent is cached or uncached. - **60 uncached torrents per hour:** an additional, stricter limit that only uncached torrents count against. The important thing is that cached and uncached requests both draw from the same 300/min pool, but uncached requests _also_ draw from their own separate 60/hour pool. An uncached request therefore counts twice: once against the per-minute limit, and once against the per-hour uncached limit. **Example:** In a single minute you add 250 cached + 50 uncached torrents. That's 300 total, so you've hit the per-minute limit for that minute. But those 50 uncached torrents also came out of your 60/hour uncached budget, leaving only **10 uncached torrents** for the remaining 59 minutes of that hour. (You could still add plenty more _cached_ torrents during that hour, since cached requests aren't capped hourly: only by the 300/min ceiling.) ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/createtorrent`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateTorrentRequest](../models/CreateTorrentRequest.md) | ✅       | The request body. |
| api_version  | str                                                       | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import CreateTorrentRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = CreateTorrentRequest(
    file="",
    magnet="string",
    seed="int",
    allow_zip="boolean",
    name="string",
    as_queued="boolean",
    add_only_if_cached="boolean"
)

result = sdk.main_api_sdk.create_torrent(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## async_create_torrent

### Overview Creates a torrent asynchrously under your account. Simply send **either** a magnet link, or a torrent file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. The request will return instantly, not returning any data other than a success message. This is the same for failures, as they will return the error in the background, rather than immediately. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/asynccreatetorrent`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [AsyncCreateTorrentRequest](../models/AsyncCreateTorrentRequest.md) | ✅       | The request body. |
| api_version  | str                                                                 | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import AsyncCreateTorrentRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = AsyncCreateTorrentRequest(
    file="",
    magnet="string",
    seed="int",
    allow_zip="boolean",
    name="string",
    as_queued="boolean",
    add_only_if_cached="boolean"
)

result = sdk.main_api_sdk.async_create_torrent(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## control_torrent

### Overview Controls a torrent. By sending the torrent's ID and the type of operation you want to perform, it will send that request to the torrent client. Operations are either: - **Reannounce** `reannounces the torrent to get new peers` - **Delete** `deletes the torrent from the client and your account permanently` - **Resume** `resumes a paused torrent` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/controltorrent`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.control_torrent(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## request_download_link

### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/requestdl`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                   |
| :---------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                               |
| token       | str  | ❌       | Your API Key                                                                                                                                  |
| torrent_id  | str  | ❌       | The torrent's ID that you want to download                                                                                                    |
| file_id     | str  | ❌       | The files's ID that you want to download                                                                                                      |
| zip_link    | str  | ❌       | If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given.                                              |
| user_ip     | str  | ❌       | The user's IP to determine the closest CDN. Optional.                                                                                         |
| redirect    | str  | ❌       | If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. |
| append_name | str  | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false.                                                |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.request_download_link(
    api_version="api_version",
    token="token",
    torrent_id="torrent_id",
    file_id="file_id",
    zip_link="zip_link",
    user_ip="user_ip",
    redirect="redirect",
    append_name="append_name"
)

print(result)
```

## request_download_links_get

### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/requestdl/batch`

**Parameters**

| Name        | Type | Required | Description                                                                                    |
| :---------- | :--- | :------- | :--------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                |
| token       | str  | ❌       | Your API Key                                                                                   |
| torrent_id  | str  | ❌       | The torrent's ID that you want to download                                                     |
| file_ids    | str  | ❌       | The files's ID that you want to download                                                       |
| user_ip     | str  | ❌       | The user's IP to determine the closest CDN. Optional.                                          |
| append_name | str  | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.request_download_links_get(
    api_version="api_version",
    token="token",
    torrent_id="torrent_id",
    file_ids="file_ids",
    user_ip="user_ip",
    append_name="append_name"
)

print(result)
```

## request_download_links_post

### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/requestdl/batch`

**Parameters**

| Name         | Type                                                                                                  | Required | Description                                                                                    |
| :----------- | :---------------------------------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------- |
| request_body | [MainApiSdkRequestDownloadLinksPostRequest1](../models/MainApiSdkRequestDownloadLinksPostRequest1.md) | ✅       | The request body.                                                                              |
| api_version  | str                                                                                                   | ✅       |                                                                                                |
| token        | str                                                                                                   | ❌       | Your API Key                                                                                   |
| torrent_id   | str                                                                                                   | ❌       | The torrent's ID that you want to download                                                     |
| user_ip      | str                                                                                                   | ❌       | The user's IP to determine the closest CDN. Optional.                                          |
| append_name  | str                                                                                                   | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import MainApiSdkRequestDownloadLinksPostRequest1

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = MainApiSdkRequestDownloadLinksPostRequest1(
    file_ids=[
        12
    ]
)

result = sdk.main_api_sdk.request_download_links_post(
    request_body=request_body,
    api_version="api_version",
    token="token",
    torrent_id="torrent_id",
    user_ip="user_ip",
    append_name="append_name"
)

print(result)
```

## get_torrent_list

### Overview Gets the user's torrent list. This gives you the needed information to perform other torrent actions. This information only gets updated every 600 seconds, or when the _Request Update On Torrent_ request is sent to the _relay API_. #### Download States: - "downloading" -\> The torrent is currently downloading. - "uploading" -\> The torrent is currently seeding. - "stalled (no seeds)" -\> The torrent is trying to download, but there are no seeds connected to download from. - "paused" -\> The torrent is paused. - "completed" -\> The torrent is completely downloaded. Do not use this for download completion status. - "cached" -\> The torrent is cached from the server. - "metaDL" -\> The torrent is downloading metadata from the hoard. - "checkingResumeData" -\> The torrent is checking resumable data. All other statuses are basic qBittorrent states. [Check out here for the full list](<https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#torrent-management>). ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/mylist`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                   |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                                                                                                               |
| bypass_cache | str  | ❌       | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. |
| id\_         | str  | ❌       | Determines the torrent requested, will return an object rather than list. Optional.                                                                                                           |
| offset       | str  | ❌       | Determines the offset of items to get from the database. Default is 0. Optional.                                                                                                              |
| limit        | str  | ❌       | Determines the number of items to recieve per request. Default is 1000. Optional.                                                                                                             |
| active       | str  | ❌       | Shows only active downloads. Optional                                                                                                                                                         |
| files        | str  | ❌       | Exclude files from response. Optional                                                                                                                                                         |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_torrent_list(
    api_version="api_version",
    bypass_cache="bypass_cache",
    id_="id",
    offset="offset",
    limit="limit",
    active="active",
    files="files"
)

print(result)
```

## get_torrent_cached_availability

### Overview Takes in a list of comma separated torrent hashes and checks if the torrent is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/checkcached`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                              |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                          |
| hash        | str  | ❌       | The list of torrent hashes you want to check. Comma seperated.                                                                                           |
| format      | str  | ❌       | Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list. |
| list_files  | str  | ❌       | Allows you to list the files found inside the cached data.                                                                                               |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_torrent_cached_availability(
    api_version="api_version",
    hash="hash",
    format="object",
    list_files="list_files"
)

print(result)
```

## get_torrent_cached_availability_batch

### Overview Takes in a list of comma separated torrent hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/checkcached`

**Parameters**

| Name         | Type                                                                                              | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [GetTorrentCachedAvailabilityBatchRequest](../models/GetTorrentCachedAvailabilityBatchRequest.md) | ✅       | The request body. |
| api_version  | str                                                                                               | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import GetTorrentCachedAvailabilityBatchRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = GetTorrentCachedAvailabilityBatchRequest(
    hashes=[
        "string"
    ]
)

result = sdk.main_api_sdk.get_torrent_cached_availability_batch(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## export_torrent_data

### Overview Exports the magnet or torrent file. Requires a type to be passed. If type is **magnet**, it will return a JSON response with the magnet as a string in the _data_ key. If type is **file**, it will return a bittorrent file as a download. Not compatible with cached downloads. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/exportdata`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                                                                             |
| :---------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                                                                                         |
| torrent_id  | str  | ❌       | The torrent's ID.                                                                                                                                                                                                       |
| type\_      | str  | ❌       | Either "magnet" or "file". Tells how the API what to get, and what to respond as. If magnet, it returns a JSON response with the magnet as a string in the data key. If file, it responds with a torrent file download. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.export_torrent_data(
    api_version="api_version",
    torrent_id="torrent_id",
    type_="type"
)

print(result)
```

## get_torrent_info

### Overview A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant. **It is not recommended to use this for checking TorBox's cache. Please use the GET /checkcache endpoint instead.** ### Authorization None required.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/torrents/torrentinfo`

**Parameters**

| Name             | Type | Required | Description                                                                                                                                                                                          |
| :--------------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version      | str  | ✅       |                                                                                                                                                                                                      |
| hash             | str  | ❌       | Hash of the torrent you want to get info for. This is required.                                                                                                                                      |
| timeout          | str  | ❌       | The amount of time you want TorBox to search for the torrent on the Bittorrent network. If the number of seeders is low or even zero, this value may be helpful to move up. Default is 10. Optional. |
| use_cache_lookup | str  | ❌       | If you want to use a pre-cached request if sent before. This can save a lot of time. Default false.                                                                                                  |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_torrent_info(
    api_version="api_version",
    hash="hash",
    timeout="30",
    use_cache_lookup="false"
)

print(result)
```

## get_torrent_info_1

### Overview Same as the GET route, but allows posting data such as magnet, and torrent files. Hashes will have precedence over magnets, and magnets will have precedence over torrent files. Only proper torrent files are accepted. At least one of hash, magnet, or torrent file is required. A general route that allows you to give a hash, and TorBox will return data about the torrent. This data is retrieved from the Bittorrent network, so expect it to take some time. If the request goes longer than 10 seconds, TorBox will cancel it. You can adjust this if you like, but the default is 10 seconds. This route is cached as well, so subsequent requests will be instant. **It is not recommended to use this for checking TorBox's cache. Please use the GET /checkcache endpoint instead.** ### Authorization None required.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/torrentinfo`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [GetTorrentInfoRequest](../models/GetTorrentInfoRequest.md) | ✅       | The request body. |
| api_version  | str                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import GetTorrentInfoRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = GetTorrentInfoRequest(
    magnet="string",
    file="",
    hash="string",
    timeout="integer",
    use_cache_lookup="bool",
    peers_only="bool"
)

result = sdk.main_api_sdk.get_torrent_info_1(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## edit_torrent_item

### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `PUT`
- Endpoint: `/{api_version}/api/torrents/edittorrent`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [EditTorrentItemRequest](../models/EditTorrentItemRequest.md) | ✅       | The request body. |
| api_version  | str                                                           | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import EditTorrentItemRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = EditTorrentItemRequest(
    torrent_id=76,
    name="string",
    tags=[
        "string"
    ],
    alternative_hashes=[
        "string"
    ],
    airlocked=False
)

result = sdk.main_api_sdk.edit_torrent_item(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## magnet_to_file

### Overview Converts any magnet to a torrent file. Does not require the magnet to be on your TorBox account or in the TorBox cache. Free endpoint for public use. ### Authorization None required.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/torrents/magnettofile`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [MagnetToFileRequest](../models/MagnetToFileRequest.md) | ✅       | The request body. |
| api_version  | str                                                     | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import MagnetToFileRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = MagnetToFileRequest(
    magnet="string"
)

result = sdk.main_api_sdk.magnet_to_file(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## create_usenet_download

### Overview Creates a usenet download under your account. Simply send **either** a link, or an nzb file. Once they have been checked, they will begin downloading assuming your account has available active download slots, and they aren't too large. #### Post Processing Options: All post processing options that the Usenet client will perform before TorBox's own processing to make the files available. It is recommended you either don't send this parameter, or keep it at `-1` for default, which will give only the wanted files. - `-1`, Default. This runs repairs, and extractions as well as deletes the source files leaving only the wanted downloaded files. - `0`, None. No post-processing at all. Just download all the files (including all PAR2). TorBox will still do its normal processing to make the download available, but no repairs, or extraction will take place. - `1`, Repair. Download files and do a PAR2 verification. If the verification fails, download more PAR2 files and attempt to repair the files. - `2`, Repair and Unpack. Download all files, do a PAR2 verification and unpack the files. The final folder will also include the RAR and ZIP files. - `3`, Repair, Unpack and Delete. Download all files, do a PAR2 verification, unpack the files to the final folder and delete the source files. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/usenet/createusenetdownload`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateUsenetDownloadRequest](../models/CreateUsenetDownloadRequest.md) | ✅       | The request body. |
| api_version  | str                                                                     | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import CreateUsenetDownloadRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = CreateUsenetDownloadRequest(
    file="",
    link="string",
    name="string",
    password="string",
    post_processing="integer",
    as_queued="boolean",
    add_only_if_cached="boolean"
)

result = sdk.main_api_sdk.create_usenet_download(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## control_usenet_download

### Overview Controls a usenet download. By sending the usenet download's ID and the type of operation you want to perform, it will send that request to the usenet client. Operations are either: - **Delete** `deletes the nzb from the client and your account permanently` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/usenet/controlusenetdownload`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.control_usenet_download(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## request_download_link_1

### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/usenet/requestdl`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                   |
| :---------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                               |
| token       | str  | ❌       | Your API Key                                                                                                                                  |
| usenet_id   | str  | ❌       | The usenet download's ID that you want to download                                                                                            |
| file_id     | str  | ❌       | The files's ID that you want to download. Optional if using "zip_link".                                                                       |
| zip_link    | str  | ❌       | If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given.                                              |
| user_ip     | str  | ❌       | The user's IPv4 to determine the closest CDN. Optional.                                                                                       |
| redirect    | str  | ❌       | If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. |
| append_name | str  | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false.                                                |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.request_download_link_1(
    api_version="api_version",
    token="token",
    usenet_id="usenet_id",
    file_id="file_id",
    zip_link="zip_link",
    user_ip="user_ip",
    redirect="redirect",
    append_name="append_name"
)

print(result)
```

## request_download_links_get_1

### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/usenet/requestdl/batch`

**Parameters**

| Name        | Type | Required | Description                                                                                    |
| :---------- | :--- | :------- | :--------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                |
| token       | str  | ❌       | Your API Key                                                                                   |
| usenet_id   | str  | ❌       | The usenet download's ID that you want to download                                             |
| file_ids    | str  | ❌       | The files's ID that you want to download                                                       |
| user_ip     | str  | ❌       | The user's IP to determine the closest CDN. Optional.                                          |
| append_name | str  | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.request_download_links_get_1(
    api_version="api_version",
    token="token",
    usenet_id="usenet_id",
    file_ids="file_ids",
    user_ip="user_ip",
    append_name="append_name"
)

print(result)
```

## request_download_links_post_1

### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/usenet/requestdl/batch`

**Parameters**

| Name         | Type                                                                                                  | Required | Description                                                                                    |
| :----------- | :---------------------------------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------- |
| request_body | [MainApiSdkRequestDownloadLinksPostRequest2](../models/MainApiSdkRequestDownloadLinksPostRequest2.md) | ✅       | The request body.                                                                              |
| api_version  | str                                                                                                   | ✅       |                                                                                                |
| token        | str                                                                                                   | ❌       | Your API Key                                                                                   |
| usenet_id    | str                                                                                                   | ❌       | The usenet downloads' ID that you want to download                                             |
| user_ip      | str                                                                                                   | ❌       | The user's IP to determine the closest CDN. Optional.                                          |
| append_name  | str                                                                                                   | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import MainApiSdkRequestDownloadLinksPostRequest2

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = MainApiSdkRequestDownloadLinksPostRequest2(
    file_ids=[
        49
    ]
)

result = sdk.main_api_sdk.request_download_links_post_1(
    request_body=request_body,
    api_version="api_version",
    token="token",
    usenet_id="usenet_id",
    user_ip="user_ip",
    append_name="append_name"
)

print(result)
```

## get_usenet_list

### Overview Gets the user's usenet download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live usenet downloads. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/usenet/mylist`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                   |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                                                                                                               |
| bypass_cache | str  | ❌       | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. |
| id\_         | str  | ❌       | Determines the usenet download requested, will return an object rather than list. Optional.                                                                                                   |
| offset       | str  | ❌       | Determines the offset of items to get from the database. Default is 0. Optional.                                                                                                              |
| limit        | str  | ❌       | Determines the number of items to recieve per request. Default is 1000. Optional.                                                                                                             |
| active       | str  | ❌       | Shows only active downloads. Optional                                                                                                                                                         |
| files        | str  | ❌       | Exclude files from response. Optional                                                                                                                                                         |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_usenet_list(
    api_version="api_version",
    bypass_cache="bypass_cache",
    id_="id",
    offset="offset",
    limit="limit",
    active="active",
    files="files"
)

print(result)
```

## get_usenet_cached_availability

### Overview Takes in a list of comma separated usenet hashes and checks if the usenet download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. To get the hash of a usenet download, you can read [this document](https://support.torbox.app/en/articles/13681109-technical-getting-hashes-for-searches) for all of the strategies. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/usenet/checkcached`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                              |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                          |
| hash        | str  | ❌       | The list of usenet hashes you want to check. Comma seperated. To find the hash, md5 the link of the usenet link or file.                                 |
| format      | str  | ❌       | Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list. |
| list_files  | str  | ❌       | Allows you to list the files found inside the cached data. Optional.                                                                                     |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_usenet_cached_availability(
    api_version="api_version",
    hash="hash",
    format="format",
    list_files="list_files"
)

print(result)
```

## get_usenet_cached_availability_batch

### Overview Takes in a list of comma separated hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/usenet/checkcached`

**Parameters**

| Name         | Type                                                                                            | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [GetUsenetCachedAvailabilityBatchRequest](../models/GetUsenetCachedAvailabilityBatchRequest.md) | ✅       | The request body. |
| api_version  | str                                                                                             | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import GetUsenetCachedAvailabilityBatchRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = GetUsenetCachedAvailabilityBatchRequest(
    hashes=[
        "string"
    ]
)

result = sdk.main_api_sdk.get_usenet_cached_availability_batch(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## edit_usenet_item

### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `PUT`
- Endpoint: `/{api_version}/api/usenet/editusenetdownload`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [EditUsenetItemRequest](../models/EditUsenetItemRequest.md) | ✅       | The request body. |
| api_version  | str                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import EditUsenetItemRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = EditUsenetItemRequest(
    usenet_download_id=83,
    name="string",
    tags=[
        "string"
    ],
    alternative_hashes=[
        "string"
    ],
    airlocked=False
)

result = sdk.main_api_sdk.edit_usenet_item(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## get_news_server_connection_information

### Overview Gets the TorBox News Server Connection information. This is a static path, and is not dynamic. ### Authorization No authentication required.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/usenet/provider/connection`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_news_server_connection_information(api_version="api_version")

print(result)
```

## get_news_server_account

### Overview Gets the user's TorBox News Server Account with authentication details. Does not show password if not creating the account. Account creation happens on the first request. If you need to get the password, or reset the password, use the `/usenet/provider/account/resetpw` `POST` endpoint. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/usenet/provider/account`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_news_server_account(api_version="api_version")

print(result)
```

## reset_news_server_account_password

### Overview Resets the user's TorBox News Server account password. This password is automatically generated, and is not saved, it is only shown once. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/usenet/provider/account/resetpw`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.reset_news_server_account_password(api_version="api_version")

print(result)
```

## create_web_download

### Overview Creates a web download under your account. Simply send a link to any file on the internet. Once it has been checked, it will begin downloading assuming your account has available active download slots, and they aren't too large. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/webdl/createwebdownload`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateWebDownloadRequest](../models/CreateWebDownloadRequest.md) | ✅       | The request body. |
| api_version  | str                                                               | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import CreateWebDownloadRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = CreateWebDownloadRequest(
    link="string",
    password="string",
    name="string",
    as_queued="boolean",
    add_only_if_cached="boolean"
)

result = sdk.main_api_sdk.create_web_download(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## control_web_download

### Overview Controls a web download. By sending the web download's ID and the type of operation you want to perform, it will send that request to the debrid client. Operations are either: - **Delete** `deletes the download from the client and your account permanently` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/webdl/controlwebdownload`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.control_web_download(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## request_download_link_2

### Overview Requests the download link from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Permalinks Instead of generating many CDN urls by requesting this endpoint, you can instead create a permalink such as: `https://api.torbox.app/v1/api/torrents/requestdl?token=APIKEY&torrent_id=NUMBER&file_id=NUMBER&redirect=true` and when a user clicks on it, it will automatically redirect them to the CDN link. This saves requests and doesn't abuse the API. Use this method rather than saving CDN links as they are not permanent. To invalidate these permalinks, simply reset your API token or delete the item from your dashboard. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/requestdl`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                   |
| :---------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                               |
| token       | str  | ❌       | Your API Key                                                                                                                                  |
| web_id      | str  | ❌       | The web download's ID that you want to download                                                                                               |
| file_id     | str  | ❌       | The files's ID that you want to download                                                                                                      |
| zip_link    | str  | ❌       | If you want a zip link. Required if no file_id. Takes precedence over file_id if both are given.                                              |
| user_ip     | str  | ❌       | The user's IP to determine the closest CDN. Optional.                                                                                         |
| redirect    | str  | ❌       | If you want to redirect the user to the CDN link. This is useful for creating permalinks so that you can just make this request URL the link. |
| append_name | str  | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false.                                                |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.request_download_link_2(
    api_version="api_version",
    token="token",
    web_id="web_id",
    file_id="file_id",
    zip_link="zip_link",
    user_ip="user_ip",
    redirect="redirect",
    append_name="append_name"
)

print(result)
```

## request_download_links_get_2

### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/requestdl/batch`

**Parameters**

| Name        | Type | Required | Description                                                                                    |
| :---------- | :--- | :------- | :--------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                |
| token       | str  | ❌       | Your API Key                                                                                   |
| web_id      | str  | ❌       | The web download's ID that you want to download                                                |
| file_ids    | str  | ❌       | The files's ID that you want to download                                                       |
| user_ip     | str  | ❌       | The user's IP to determine the closest CDN. Optional.                                          |
| append_name | str  | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.request_download_links_get_2(
    api_version="api_version",
    token="token",
    web_id="web_id",
    file_ids="file_ids",
    user_ip="user_ip",
    append_name="append_name"
)

print(result)
```

## request_download_links_post_2

### Overview Requests multiple download links from the server. Because downloads are metered, TorBox cannot afford to allow free access to the links directly. This endpoint opens the link for 3 hours for downloads. Once a download is started, the user has nearly unlilimited time to download the file. The 1 hour time limit is simply for starting downloads. This prevents long term link sharing. ### Authorization Requires an API key as a parameter for the `token` parameter.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/webdl/requestdl/batch`

**Parameters**

| Name         | Type                                                                                                  | Required | Description                                                                                    |
| :----------- | :---------------------------------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------- |
| request_body | [MainApiSdkRequestDownloadLinksPostRequest3](../models/MainApiSdkRequestDownloadLinksPostRequest3.md) | ✅       | The request body.                                                                              |
| api_version  | str                                                                                                   | ✅       |                                                                                                |
| token        | str                                                                                                   | ❌       | Your API Key                                                                                   |
| web_id       | str                                                                                                   | ❌       | The web downloads' ID that you want to download                                                |
| user_ip      | str                                                                                                   | ❌       | The user's IP to determine the closest CDN. Optional.                                          |
| append_name  | str                                                                                                   | ❌       | If you want to add the "filename" parameter to the returned CDN link. Optional. Default false. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import MainApiSdkRequestDownloadLinksPostRequest3

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = MainApiSdkRequestDownloadLinksPostRequest3(
    file_ids=[
        68
    ]
)

result = sdk.main_api_sdk.request_download_links_post_2(
    request_body=request_body,
    api_version="api_version",
    token="token",
    web_id="web_id",
    user_ip="user_ip",
    append_name="append_name"
)

print(result)
```

## get_web_download_list

### Overview Gets the user's web download list. This gives you the needed information to perform other usenet actions. Unlike Torrents, this information is updated on its own every 5 seconds for live web downloads. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/mylist`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                   |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                                                                                                               |
| bypass_cache | str  | ❌       | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. |
| id\_         | str  | ❌       | Determines the torrent requested, will return an object rather than list. Optional.                                                                                                           |
| offset       | str  | ❌       | Determines the offset of items to get from the database. Default is 0. Optional.                                                                                                              |
| limit        | str  | ❌       | Determines the number of items to recieve per request. Default is 1000. Optional.                                                                                                             |
| active       | str  | ❌       | Shows only active downloads. Optional                                                                                                                                                         |
| files        | str  | ❌       | Exclude files from response. Optional                                                                                                                                                         |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_web_download_list(
    api_version="api_version",
    bypass_cache="bypass_cache",
    id_="id",
    offset="offset",
    limit="limit",
    active="active",
    files="files"
)

print(result)
```

## get_web_download_cached_availability

### Overview Takes in a list of comma separated usenet hashes and checks if the web download is cached. This endpoint only gets a max of around 100 at a time, due to http limits in queries. If you want to do more, you can simply do more hash queries. Such as: `?hash=XXXX&hash=XXXX&hash=XXXX` or `?hash=XXXX,XXXX&hash=XXXX&hash=XXXX,XXXX` and this will work too. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. To get the hash of a web download you can read [this document](https://support.torbox.app/en/articles/13681109-technical-getting-hashes-for-searches) for all of the strategies. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/checkcached`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                              |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                          |
| hash        | str  | ❌       | The list of web hashes you want to check. Comma seperated. To find the hash, md5 the link.                                                               |
| format      | str  | ❌       | Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list. |
| list_files  | str  | ❌       | Allows you to list the files found inside the cached data.                                                                                               |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_web_download_cached_availability(
    api_version="api_version",
    hash="hash",
    format="object",
    list_files="false"
)

print(result)
```

## get_web_download_cached_availability_batch

### Overview Takes in a list of comma separated hashes and checks if the torrent is cached. With the POST endpoint you can submit a nearly unlimited hashes compared to the GET endpoint which is limited by url parameters. Performance is very fast. Less than 1 second per 100. Time is approximately O(log n) time for those interested in taking it to its max. That is without caching as well. This endpoint stores a cache for an hour. You may also pass a `format` parameter with the format you want the data in. Options are either `object` or `list`. You can view examples of both below. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/webdl/checkcached`

**Parameters**

| Name         | Type                                                                                                      | Required | Description                                                                                                                                              |
| :----------- | :-------------------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [GetWebDownloadCachedAvailabilityBatchRequest](../models/GetWebDownloadCachedAvailabilityBatchRequest.md) | ✅       | The request body.                                                                                                                                        |
| api_version  | str                                                                                                       | ✅       |                                                                                                                                                          |
| format       | str                                                                                                       | ❌       | Format you want the data in. Acceptable is either "object" or "list". List is the most performant option as it doesn't require modification of the list. |
| list_files   | str                                                                                                       | ❌       | Allows you to list the files found inside the cached data.                                                                                               |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import GetWebDownloadCachedAvailabilityBatchRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = GetWebDownloadCachedAvailabilityBatchRequest(
    hashes=[
        "string"
    ]
)

result = sdk.main_api_sdk.get_web_download_cached_availability_batch(
    request_body=request_body,
    api_version="api_version",
    format="format",
    list_files="list_files"
)

print(result)
```

## get_hoster_list

### Overview A dynamic list of hosters that TorBox is capable of downloading through its paid service. - **Name** - a clean name for display use, the well known name of the service, should be recognizable to users. - **Domains** - an array of known domains that the hoster uses. While each may serve a different purpose it is still included. - **URL** - the main url of the service. This should take you to the home page or a service page of the hoster. - **Icon** - a square image, usually a favicon or logo, that represents the service, should be recognizable as the hoster's icon. - **Status** - whether this hoster can be used on TorBox or not at the current time. It is usually a good idea to check this value before submitting a download to TorBox's servers for download. - **Type** - values are either "hoster" or "stream". Both do the same thing, but is good to differentiate services used for different things. - **Note** - a string value (or null) that may give helpful information about the current status or state of a hoster. This can and should be shown to end users. - **Daily Link Limit** - the number of downloads a user can use per day. As a user submits links, once they hit this number, the API will deny them from adding anymore of this type of link. A zero value means that it is unlimited. - **Daily Link Used** - the number of downloads a user has already used. Usually zero unless you send authentication to the endpoint. This will return accurate values. - **Daily Bandwidth Limit** - the value in bytes that a user is allowed to download from this hoster. A zero value means that it is unlimited. It is recommended to use the Daily Link Limit instead. - **Daily Bandwidth Used** - the value in bytes that a user has already used to download from this hoster. Usually zero unless you send authentication to the endpoint. This will return accurate values. ### Authorization Optional authorization. Authorization is not required in this endpoint unless you want to get the user's live data. Requires an API key using the Authorization Bearer Header to get the live and accurate data for **Daily Link Used** and **Daily Bandwidth Used**.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/webdl/hosters`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_hoster_list(api_version="api_version")

print(result)
```

## edit_web_download_item

### Overview Updates a download item based on the item's ID. Sending a PUT request with valid items overwrites the previous items entirely, so use this endpoint with caution. Please make sure to read the restrictions below as they are important. ### Restrictions - Does not affect the cached database (or any other user's item). - Name must pass validation: - Above 1 character long. - Below 200 characters long. - Cannot contain any non-url or non filesystem safe characters. (This is removed automatically). - Cannot contain any leading or trailing whitespace. You can have spaces in the middle. (This is removed automatically). - Tags follow the same rules as the name. - Alternative hashes must be of MD5, SHA1, or SHA256. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `PUT`
- Endpoint: `/{api_version}/api/webdl/editwebdownload`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EditWebDownloadItemRequest](../models/EditWebDownloadItemRequest.md) | ✅       | The request body. |
| api_version  | str                                                                   | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import EditWebDownloadItemRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = EditWebDownloadItemRequest(
    webdl_id=66,
    name="string",
    tags=[
        "string"
    ],
    alternative_hashes=[
        "string"
    ],
    airlocked=False
)

result = sdk.main_api_sdk.edit_web_download_item(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## get_up_status

### Overview Simply gets if the TorBox API is available for use or not. Also might include information about downtimes. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/`

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_up_status()

print(result)
```

## get_stats

### Overview Simply gets general stats about the TorBox service. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/stats`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_stats(api_version="api_version")

print(result)
```

## get_changelogs_rss_feed

### Overview Gets most recent 100 changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for people who want updates on the TorBox changelog. Includes all the necessary items to make this compatible with RSS feed viewers for notifications, and proper HTML viewing. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/changelogs/rss`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| offset      | str  | ❌       |             |
| limit       | str  | ❌       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_changelogs_rss_feed(
    api_version="api_version",
    offset="0",
    limit="10"
)

with open("output-file.ext", "w") as f:
    f.write(result if isinstance(result, str) else result.decode(errors="replace") if isinstance(result, (bytes, bytearray)) else str(result))
```

## get_changelogs_json

### Overview Gets most recent changelogs from [https://feedback.torbox.app/changelog.](https://feedback.torbox.app/changelog.) This is useful for developers who want to integrate the changelog into their apps for their users to see. Includes content in HTML for developers to easily render the text in a fancy yet simple way. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/changelogs/json`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| offset      | str  | ❌       |             |
| limit       | str  | ❌       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_changelogs_json(
    api_version="api_version",
    offset="0",
    limit="10"
)

print(result)
```

## get_speedtest_files

### Overview Gets CDN speedtest files. This can be used for speedtesting TorBox for users or other usages, such as checking download speeds for verification. Provides all necessary data such as region, server name, and even coordinates. Uses the requesting IP to determine if the server is the closest to the user. You also have the ability to choose between long tests or short tests via the "test_length" parameter. You may also force the region selection by passing the "region" as a specific region. ### Authorization None needed.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/speedtest`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                                                        |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                                                                                                                                                    |
| test_length | str  | ❌       | Determines the size of the file used for the speedtest. May be "long" or "short". Optional.                                                                                                        |
| region      | str  | ❌       | Determines what cdns are returned. May be any region that TorBox is located in. To get this value, send a request without this value to determine all of the available regions that are available. |
| user_ip     | str  | ❌       | Pass a user's IP to get the closest server to them, otherwise will use the calling IP for location.                                                                                                |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_speedtest_files(
    api_version="api_version",
    test_length="short",
    region="region",
    user_ip="user_ip"
)

print(result)
```

## get_rss_notification_feed

### Overview Gets your notifications in an RSS Feed which allows you to use them with RSS Feed readers or notification services that can take RSS Feeds and listen to updates. As soon as a notification goes to your account, it will be added to your feed. ### Authorization Requires an API key using as a query parameter using the `token` key.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/notifications/rss`

**Parameters**

| Name        | Type | Required | Description         |
| :---------- | :--- | :------- | :------------------ |
| api_version | str  | ✅       |                     |
| token       | str  | ❌       | The user's API key. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_rss_notification_feed(
    api_version="api_version",
    token="token"
)

with open("output-file.ext", "w") as f:
    f.write(result if isinstance(result, str) else result.decode(errors="replace") if isinstance(result, (bytes, bytearray)) else str(result))
```

## get_notification_feed

### Overview Gets your notifications in a JSON object that is easily parsable compared to the RSS Feed. Gives all the same data as the RSS Feed. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/notifications/mynotifications`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_notification_feed(api_version="api_version")

print(result)
```

## clear_all_notifications

### Overview Marks all of your notifications as read and deletes them permanently. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/notifications/clear`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.clear_all_notifications(api_version="api_version")

print(result)
```

## clear_single_notification

### Overview Marks a single notification as read and permanently deletes it from your notifications. Requires a `notification_id` which can be found by getting your notification feed. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/notifications/clear/{notification_id}`

**Parameters**

| Name            | Type | Required | Description |
| :-------------- | :--- | :------- | :---------- |
| api_version     | str  | ✅       |             |
| notification_id | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.clear_single_notification(
    api_version="api_version",
    notification_id="notification_id"
)

print(result)
```

## send_test_notification

### Overview Sends a test notification to all enabled notification types. This can be useful for validating setups. No need for any body in this request. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/notifications/test`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.send_test_notification(api_version="api_version")

print(result)
```

## refresh_api_token

### Overview If you want a new API token, or your old one has been compromised, you may request a new one. If you happen to forget the token, go the [TorBox settings page ](https://torbox.app/settings) and copy the current one. If this still doesn't work, you may contact us at our support email for a new one. ### Authorization Requires an API key using the Authorization Bearer Header as well as passing the `session_token` from the website to be passed in the body. You can find the `session_token` in the localStorage of your browser on any TorBox.app page under the key `torbox_session_token`. This is a temporary token that only lasts for 1 hour, which is why it is used here to verify the identity of a user as well as their API token.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/user/refreshtoken`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.refresh_api_token(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## get_user_data

### Overview Gets a users account data and information. ### Plans `0` is Free plan `1` is Essential plan (_$3 plan_) `2` is Pro plan (_$10 plan_) `3` is Standard plan (_$5 plan_) ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/me`

**Parameters**

| Name        | Type | Required | Description                           |
| :---------- | :--- | :------- | :------------------------------------ |
| api_version | str  | ✅       |                                       |
| settings    | str  | ❌       | Allows you to retrieve user settings. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_user_data(
    api_version="api_version",
    settings="false"
)

print(result)
```

## add_referral_to_account

### Overview Automatically adds a referral code to the user's account. This can be used for developers to automatically add their referral to user's accounts who use their service. This will not override any referral a user already has. If they already have one, then it cannot be changed using this endpoint. It can only be done by the user on the [website](https://torbox.app/subscription). ### Authorization Requires an API key using the Authorization Bearer Header. Use the user's API key, not your own.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/user/addreferral`

**Parameters**

| Name        | Type | Required | Description                    |
| :---------- | :--- | :------- | :----------------------------- |
| api_version | str  | ✅       |                                |
| referral    | str  | ❌       | A referral code. Must be UUID. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.add_referral_to_account(
    api_version="api_version",
    referral="referral"
)

print(result)
```

## get_confirmation_code

### Overview Requests a 6 digit code to be sent to the user's email for verification. Used to verify a user actually wants to perform a potentially dangerous action. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/getconfirmation`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_confirmation_code(api_version="api_version")

print(result)
```

## start_device_code_authorization_process

### Overview Starts the device code authorization process. Returns all the necessary information to complete the rest of the flow. This includes the following: - `device_code` - The code your app will use for consecutive requests for getting the user token. - `code` - This is the 6 digit code that you show to the user to be entered at the following verification*url. - `verification_url` - This url which you will show as a QR code. - `friendly_verification_url` - The friendly short url which you can show as plain text to user if they cannot use the QR code method. You may also submit the `app` parameter to this request to show your app name on the `verification_url` page. This concretes user trust in authorizing your application to use their TorBox account. This is not required, but is a good idea. Default is "Third Party App". This name is also only allowed to be alpha-numeric characters (\_A-Z,0-9*). Anything else will be filtered our when being shown to the user. The `friendly_verification_url` will always show "Third Party App" to keep the URL short. The device_code is only valid for 10 minutes. Make sure the user is aware of this time limit so they submit and login before this time limit is over. ### Authorization None required.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/auth/device/start`

**Parameters**

| Name        | Type | Required | Description                                                                                       |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------ |
| api_version | str  | ✅       |                                                                                                   |
| app         | str  | ❌       | The app name that the user will see when verifying the code. This should be the name of your app. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.start_device_code_authorization_process(
    api_version="api_version",
    app="Third Party App"
)

print(result)
```

## get_token_from_device_code_process

### Overview Gets the user's API token from the device code authorization process. This endpoint is expected to be polled in interval until it returns success, or until the expiry has passed. All data you need for this request is in the [original request](https://www.postman.com/wamy-dev/workspace/torbox/request/29572726-744bc274-88b7-4faf-a833-e30573c8c1e0?action=share&creator=29572726&ctx=documentation), which includes the interval to be polled by, the expiry time to stop at, and `device_code` to be sent to the API to get the correct data. ### Authorization None required.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/user/auth/device/token`

**Parameters**

| Name         | Type                                                                                      | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [GetTokenFromDeviceCodeProcessRequest](../models/GetTokenFromDeviceCodeProcessRequest.md) | ✅       | The request body. |
| api_version  | str                                                                                       | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment
from main_api_sdk.models import GetTokenFromDeviceCodeProcessRequest

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = GetTokenFromDeviceCodeProcessRequest(
    device_code="XXXXXXXXXXXXXXXXXXXXXXXXX"
)

result = sdk.main_api_sdk.get_token_from_device_code_process(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## get_referral_data

### Overview Use this endpoint to get the user's referral data. This includes information such as how many referrals they have made, and their referral code. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/referraldata`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_referral_data(api_version="api_version")

print(result)
```

## get_subscriptions

### Overview Gets a users subscriptions. This includes active and inactive subscriptions for all payment processors. It should be noted that "plan_code" is not normalized to the standard plan codes such as 1, 2, or 3. These "plan_code"s are payment processor specific and used internally. If you want to display these subscriptions, use the "plan_name". For displaying information to users, use the "status", "gateway", and "plan_name". No other information is relevant to the user, and the rest is used for TorBox internally. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/subscriptions`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_subscriptions(api_version="api_version")

print(result)
```

## get_transactions

### Overview Use this endpoint to get the user's list of transactions. This data isn't exactly relevant to a third party developer, unless you want to build full parity with TorBox's dashboard, or simply want to show this information. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/transactions`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_transactions(api_version="api_version")

print(result)
```

## get_transaction_pdf

### Overview Generates a PDF of the transaction information. Requires the transaction ID from the "Get Transactions" request. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/transaction/pdf`

**Parameters**

| Name           | Type | Required | Description                                               |
| :------------- | :--- | :------- | :-------------------------------------------------------- |
| api_version    | str  | ✅       |                                                           |
| transaction_id | str  | ❌       | The transaction ID that you want to generate the PDF for. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_transaction_pdf(
    api_version="api_version",
    transaction_id="transaction_id"
)

print(result)
```

## edit_user_settings

### Overview Edits a user's TorBox settings. These values take effect immediately. Please view the body to read about allowed options and parameters. To get the user settings, simply use the "[Get User Data](https://www.postman.com/torbox/workspace/torbox-api/request/29572726-a3775d9b-f3ee-49cd-98a4-fc909ed2923b?action=share&source=copy-link&creator=29572726)" endpoint, while sending the "?settings=true" parameter ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `PUT`
- Endpoint: `/{api_version}/api/user/settings/editsettings`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.edit_user_settings(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## get_user_stats

### Overview Gets a users stats. This data is currently split into two sections, "general" and "bandwidth". General shows general data, such as "Total Data Downloaded", "Total Data Egress", "Overall Ratio", and "Total Downloaded". Bandwidth shows the amount of bandwidth a user has downloaded within the past 30 days. We don't store this data for longer than 30 days, and it can be made more or less granular. Makes cool graphs! ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/user/stats`

**Parameters**

| Name               | Type | Required | Description                                                                                                                                                                                  |
| :----------------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version        | str  | ✅       |                                                                                                                                                                                              |
| general            | str  | ❌       | Retrieve general stats.                                                                                                                                                                      |
| bandwidth          | str  | ❌       | Retrieve bandwidth stats.                                                                                                                                                                    |
| bandwidth_grouping | str  | ❌       | If the "bandwidth" query parameter is sent, this value is used. Allowed is "hour", "day", "week", and "month", this narrates how bandwidth is grouped. More granular shows more information. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_user_stats(
    api_version="api_version",
    general="true",
    bandwidth="false",
    bandwidth_grouping="day"
)

print(result)
```

## add_rss_feed

### Overview Allows adding an RSS feed to your account. This API gives you a lot of customization options, but is best used with the UI on the website. This endpoint only works for Pro users (plan: 2). ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/rss/addrss`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.add_rss_feed(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## control_rss_feed

### Overview Controls an RSS Feed. By sending the RSS feed's ID and the type of operation you want to perform, it will perform said action on the RSS feed checker. Operations are either: - **Update** `forces an update on the rss feed` - **Delete** `deletes the rss feed from your account permanently. This also deletes all associated RSS feed items. This does not remove queued items spawned from the RSS feed.` - **Pause** `pauses checking the rss feed on the scan interval` - **Resume** `resumes a paused rss feed` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/rss/controlrss`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.control_rss_feed(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## edit_rss_feed

### Overview Allows you to edit the RSS feed based on the RSS feed ID passed. Allows you to change everything about an RSS feed, except for the URL. When updating the "rss_type" or the "torrent_seeding" options, it will update all of the RSS items associated with the RSS feed, including all previous items. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/rss/modifyrss`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.edit_rss_feed(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## get_user_rss_feeds

### Overview Gets all of a user's RSS feeds located on their account. Can only be accessed on a Pro (plan: 2) account. Also allows you to get a specific by passing an "id" in the parameters. ##### Type Key The "type" key in the response is used for showing what type of downloads are spawned from this RSS feed. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct. - **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.` - "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.` - "webdl" `uses generic links and adds as a web download when downloaded.` ##### Status Key The "status" key tells the user selected status of the RSS feed. These statuses are **not** the same as the status key for the RSS items associated with the RSS feed. Each feed also includes a "status_message" key which gives a user friendly message about anything about the RSS feed, such as errors and explainations. - "active" `the RSS feed is set to be scraped.` - "paused" `the RSS feed will not be scraped as it is paused by the user.` - "error" `the RSS feed had an error while scraping, and cannot continue.` ##### State Key The "state" key tells you exactly in real time, what the RSS feed is doing. This is useful for realtime status updates. - "idle" `the RSS feed is idle, and is currently not doing anything in the current moment.` - "scraping" `the RSS feed is currently scraping new RSS items.` - "downloading" `the RSS feed is currently downloading the newly scraped RSS items.` ##### Torrent Seeding Key The "torrent_seeding" key is returned with every response, regardless of the type of the RSS feed. This controls what seeding setting the RSS feed is using when it adds new torrents. These are the same options as when adding a torrent using the /torrent/createtorrent endpoint. \> Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings. - 1 `auto, the torrent will seed based on what the user has in their settings.` - 2 `always, TorBox will be instructed to seed this torrent regardless of any other settings.` - 3 `never, TorBox will not seed this torrent.` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/rss/getfeeds`

**Parameters**

| Name        | Type | Required | Description                                                 |
| :---------- | :--- | :------- | :---------------------------------------------------------- |
| api_version | str  | ✅       |                                                             |
| id\_        | str  | ❌       | A specific RSS feed ID that you want to retrieve. Optional. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_user_rss_feeds(
    api_version="api_version",
    id_="id"
)

print(result)
```

## get_rss_feed_items

### Overview Gets the first 10,000 RSS feed items associated with an RSS feed. RSS feed items are scraped items from the RSS feed. They contain a direct download link as well as the content name, and additional information. ##### Type Key The "type" key in the response is used for showing what type of downloads this RSS feed item is. This affects how the item is downloaded, as well as what is scraped, so make sure it is correct. When the parent RSS feed's type is changed, it changes all of the items types as well. - **"**torrent**"** `uses .torrent files and magnet links and adds as torrent when downloaded.` - "usenet" `uses .nzb files and nzb links and adds as a usenet download when downloaded.` - "webdl" `uses generic links and adds as a web download when downloaded.` ##### Status Key The "status" key tells the status of the RSS feed item. This is useful for seeing what the item is doing, and what it will do next. Each item also includes a "status_message" key which gives a user friendly message about anything about the RSS feed item, such as errors and explainations. - "new" `the RSS feed item is set to be downloaded.` - "ignored" `the RSS feed item has been ignored due to the parents RSS feed settings, as it doesn't match the chosen settings. The item will not be downloaded.` - "error" `the RSS feed item had an error while attempting to download. The item will be retried on the next scrape.` - "downloaded" `the RSS feed item has already been downloaded to the user's account. It will not be downloaded again.` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/rss/getfeeditems`

**Parameters**

| Name        | Type | Required | Description                                                                |
| :---------- | :--- | :------- | :------------------------------------------------------------------------- |
| api_version | str  | ✅       |                                                                            |
| rss_feed_id | str  | ❌       | The RSS Feed ID of the RSS Feed you want to retrieve the scraped items of. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_rss_feed_items(
    api_version="api_version",
    rss_feed_id="rss_feed_id"
)

print(result)
```

## get_all_jobs

### Overview Gets all the jobs attached to a user account. This is good for an overall view of the jobs, such as on a dashboard, or something similar. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/integration/jobs`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_all_jobs(api_version="api_version")

print(result)
```

## get_specific_job

### Overview Gets a specifc job using the Job's ID. To get the ID, you will have to Get All Jobs, and get the ID you want. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/integration/job/{job_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| job_id      | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_specific_job(
    api_version="api_version",
    job_id="job_id"
)

print(result)
```

## get_all_jobs_by_hash

### Overview Gets all jobs that match a specific hash. Good for checking on specific downloads such as a download page, that could contain a lot of jobs. ### Statuses - "pending" -\> Upload is still waiting in the queue. Waiting for spot to upload. - "uploading" -\> Upload is uploading to the proper remote. Progress will be updated as upload continues. - "completed" -\> Upload has successfully been uploaded. Progress will be at 1, and the download URL will be populated. - "failed" -\> The upload has failed. Check the Detail key for information. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/integration/jobs/{hash}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| hash        | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_all_jobs_by_hash(
    api_version="api_version",
    hash="hash"
)

print(result)
```

## cancel_specific_job

### Overview Cancels a job or deletes the job. Cancels while in progess (pending, uploading), or deletes the job any other time. It will delete it from the database completely. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `DELETE`
- Endpoint: `/{api_version}/api/integration/job/{job_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| api_version | str  | ✅       |             |
| job_id      | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.cancel_specific_job(
    api_version="api_version",
    job_id="job_id"
)

print(result)
```

## get_queued_downloads

### Overview Retrieves all of a user's queued downloads by type. If you want to get all 3 types, "torrent", "usenet" and "webdl" then you will need to run this request 3 times, each with the different type. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/queued/getqueued`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                   |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version  | str  | ✅       |                                                                                                                                                                                               |
| bypass_cache | str  | ❌       | Allows you to bypass the cached data, and always get fresh information. Useful if constantly querying for fresh download stats. Otherwise, we request that you save our database a few calls. |
| id\_         | str  | ❌       | Determines the queued download requested, will return an object rather than list. Optional.                                                                                                   |
| offset       | str  | ❌       | Determines the offset of items to get from the database. Default is 0. Optional.                                                                                                              |
| limit        | str  | ❌       | Determines the number of items to recieve per request. Default is 1000. Optional.                                                                                                             |
| type\_       | str  | ❌       | The type of the queued download you want to retrieve. Can be "torrent", "usenet" or "webdl". Optional. Default is "torrent".                                                                  |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_queued_downloads(
    api_version="api_version",
    bypass_cache="bypass_cache",
    id_="id",
    offset="offset",
    limit="limit",
    type_="torrent"
)

print(result)
```

## control_queued_downloads

### Overview Controls a queued torrent. By sending the queued torrent's ID and the type of operation you want to perform, it will perform that action on the queued torrent. Operations are either: - **Delete** `deletes the queued download from your account` - **Start** `starts a queued download, cannot be used with the "all" parameter` ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `POST`
- Endpoint: `/{api_version}/api/queued/controlqueued`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | dict | ✅       | The request body. |
| api_version  | str  | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

request_body = {}

result = sdk.main_api_sdk.control_queued_downloads(
    request_body=request_body,
    api_version="api_version"
)

print(result)
```

## create_stream

### Overview Creates a new stream based off of the data provided. #### Selecting Subtitles and Audios We use indexes to determine which audio and subtitle you would like to select. To view all available indexes, you must request this endpoint intially with "null" or 0, for the chosen indexes. This will return a metadata dictionary in the response, which will contain the list of audios and subtitles available for this stream. When choosing a subtitle or audio stream, use the **relative index**, starting from 0, rather than the "index" value. This is important for selecting the correct index. Once your user gets a selection of audios and subtitles available, you can submit this to the endpoint again to get the chosen stream. - **null** - Selecting no subtitle. Not available for audio as one must always be selected. - **0** - Selecting first subtitle or audio #### Selecting Resolution Similar to the subtitles and audios, we use indexes to determine the resolution chosen. Unlike the above, these are predetermined. We do not upscale video, so if for example, you pass a 1080p video, and request it with resolution, 7, it will stay at 1080p. Please see the below for options. - **null** - Original video resolution. No downscaling will take place. - **0** - 144p - **1** - 240p - **2** - 360p - **3** - 480p - **4** - 720p - **5** - 1080p - **6** - 1440p - **7** - 2160p #### Types This endpoint allows you to handle torrents, usenet and web downloads all in one. This is why the "type" parameter is available. It defaults to "torrent". - **torrent** - Torrents - **usenet** - Usenet downloads - **webdownload** - Web Downloads #### Important Notes - Only text based subtitles are supported. If a non-text based subtitle is selected, it will be ignored. - If a subtitle or audio index does not exist on the stream, it will be ignored. - There are a lot of edge-case videos, if something doesn't work, don't hesitate to report the download hash and file_id of the failing video file. - This is a **Pro** only feature. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/stream/createstream`

**Parameters**

| Name                    | Type | Required | Description                                                                                                                                  |
| :---------------------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version             | str  | ✅       |                                                                                                                                              |
| id\_                    | str  | ❌       | The ID of the type of download.                                                                                                              |
| file_id                 | str  | ❌       | The file ID inside of the download you would like to stream.                                                                                 |
| type\_                  | str  | ❌       | The type of download that this is. If choosing the incorrect one, the ID will be incorrect.                                                  |
| chosen_subtitle_index   | str  | ❌       | The relative index of the subtitle you would like to stream. This is default null for none. 0 is the first subtitle found.                   |
| chosen_audio_index      | str  | ❌       | The relative index of the subtitle you would like to stream. Defaults to 0 for the first audio stream found inside the file. Cannot be null. |
| chosen_resolution_index | str  | ❌       | The index of the resolution you would like to stream. This is default null for original.                                                     |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.create_stream(
    api_version="api_version",
    id_="id",
    file_id="0",
    type_="torrent",
    chosen_subtitle_index="chosen_subtitle_index",
    chosen_audio_index="0",
    chosen_resolution_index="chosen_resolution_index"
)

print(result)
```

## get_stream_data

### Overview Gets stream data from an already created stream. Requires the presigned token and user API token from the original request. ### Authorization Requires an API key using the Authorization Bearer Header.

- HTTP Method: `GET`
- Endpoint: `/{api_version}/api/stream/getstreamdata`

**Parameters**

| Name                    | Type | Required | Description                                                                              |
| :---------------------- | :--- | :------- | :--------------------------------------------------------------------------------------- |
| api_version             | str  | ✅       |                                                                                          |
| presigned_token         | str  | ❌       | The presigned token given from the original, /createstream request.                      |
| token                   | str  | ❌       | The user's API token, can also be used from the original, /createstream request.         |
| chosen_subtitle_index   | str  | ❌       | The chosen subtitle index that you are requesting information about.                     |
| chosen_audio_index      | str  | ❌       | The chosen audio index that you are requesting information about.                        |
| chosen_resolution_index | str  | ❌       | The index of the resolution you would like to stream. This is default null for original. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10
)

result = sdk.main_api_sdk.get_stream_data(
    api_version="api_version",
    presigned_token="presigned_token",
    token="token",
    chosen_subtitle_index="chosen_subtitle_index",
    chosen_audio_index="chosen_audio_index",
    chosen_resolution_index="chosen_resolution_index"
)

print(result)
```
