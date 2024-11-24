from torbox_api import TorboxApi

sdk = TorboxApi(access_token="YOUR_ACCESS_TOKEN", timeout=10000)

result = sdk.general.get_up_status()

print(result)
