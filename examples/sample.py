from main_api_sdk import MainApiSdk, Environment

sdk = MainApiSdk(
    access_token="YOUR_ACCESS_TOKEN", base_url=Environment.DEFAULT.value, timeout=10
)

result = sdk.main_api_sdk.get_up_status()

print(result)
