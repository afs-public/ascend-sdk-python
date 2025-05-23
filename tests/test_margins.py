"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ascend_sdk import SDK
from ascend_sdk.models import components
import os


def test_margins_margins_real_time_get_buying_power_get_buying_power1():
    s = SDK(
        server_url="https://uat.apexapis.com",
        security=components.Security(
            api_key=os.getenv("API_KEY", ""),
            service_account_creds=components.ServiceAccountCreds(
                private_key=os.getenv("SERVICE_ACCOUNT_CREDS_PRIVATE_KEY", ""),
                name=os.getenv("SERVICE_ACCOUNT_CREDS_NAME", ""),
                organization=os.getenv("SERVICE_ACCOUNT_CREDS_ORGANIZATION", ""),
                type="serviceAccount",
            ),
        ),
    )

    assert s is not None

    res = s.margins.get_buying_power(account_id="01JHGTEPC6ZTAHCFRH2MD3VJJT")
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
