import typing
import jwt
import base64
from datetime import datetime, timezone, timedelta

import requests
from typing import Union
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from ascend_sdk.models.components import Security

from .types import (
    BeforeRequestContext,
    BeforeRequestHook,
)


class ApexAccessTokenHook(BeforeRequestHook):
    access_token: str

    def __init__(self, access_token=None):
        self.access_token = access_token

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: requests.PreparedRequest
    ) -> Union[requests.PreparedRequest, Exception]:
        # modify the request object before it is sent, such as adding headers or query parameters, or raise an exception to stop the request
        sec = hook_ctx.security_source
        if callable(sec):
            sec = sec()
        if sec is None:
            raise Exception("security source is not defined")
        custom_sec = typing.cast(Security, sec)
        if custom_sec.api_key is not None:
            request.headers["x-api-key"] = custom_sec.api_key
        else:
            raise Exception("api key is not defined")

        if custom_sec.service_account_creds is not None:
            accessToken = self.get_access_token(
                extract_origin(request.url),
                custom_sec.api_key,
                custom_sec.service_account_creds,
            )
            request.headers["Authorization"] = f"Bearer {accessToken}"
        else:
            raise Exception("service account creds is not defined")

        return request

    def get_access_token(self, server_url, api_key, service_account_creds):
        if self.access_token_still_valid():
            return self.access_token

        # Update token expiration
        self.access_token_expiration = datetime.now()

        # Create JWS
        jws = get_jws(service_account_creds)

        # Generate new JWT (i.e. access token)
        resp = generate_service_account_token(server_url, api_key, jws)

        if resp.status_code != 200:
            error_message = f"Error generating service account token [url: {resp.url}, status: {resp.status_code}, error_text: {resp.text}]"
            raise Exception(error_message)

        data = resp.json()
        if "access_token" not in data:
            raise Exception("No access_token returned")
        if "expires_in" not in data:
            raise Exception("No expires_in returned")

        self.access_token = data["access_token"]
        self.access_token_expiration += timedelta(minutes=data["expires_in"] / 60)

        return self.access_token

    def access_token_still_valid(self):
        if not self.access_token:
            return False
        # Confirm token expiration is "after now"
        return (
            self.access_token_expiration is not None
            and self.access_token_expiration > datetime.now()
        )


def get_jws(service_account_creds) -> str:
    # Extract the private key, removing headers, footers, and newlines
    private_key_content = (
        service_account_creds.private_key.replace("\n", "")
        .replace("\\n", "")
        .replace("\r", "")
        .replace("\\r", "")
        .replace("-----BEGIN PRIVATE KEY-----", "")
        .replace("-----END PRIVATE KEY-----", "")
    )

    # Decode the base64 private key
    decoded_key = base64.b64decode(private_key_content)
    # Deserialize the key to RSAPrivateKey object
    private_key = serialization.load_der_private_key(
        decoded_key, password=None, backend=default_backend()
    )

    # Prepare claims for the JWT
    now_iso_date_time = datetime.now(timezone.utc).isoformat()
    claims = {
        "iss": "issuer",
        "sub": "subject",
        "name": service_account_creds.name,
        "organization": service_account_creds.organization,
        "datetime": now_iso_date_time,
    }

    # Create a JWS and sign it with the private key using RS256 algorithm
    encoded_jws = jwt.encode(claims, private_key, algorithm="RS256")

    return encoded_jws


def generate_service_account_token(
    server_url: str, api_key: str, jws: str
) -> requests.Response:
    url = f"{server_url}/iam/v1/serviceAccounts:generateAccessToken"
    # Prepare headers
    headers = {"Content-Type": "application/json", "x-api-key": api_key}

    try:
        response = requests.post(url, headers=headers, json={"jws": jws})
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response
    except requests.RequestException as error:
        print(f"Failed to fetch access token from {server_url}: {error}")
        raise


def extract_origin(url) -> str:
    netloc = url.netloc.decode("utf8")
    if url.port is None:
        return f"{url.scheme}://{netloc}"
    else:
        return f"{url.scheme}://{netloc}:{url.port}"
