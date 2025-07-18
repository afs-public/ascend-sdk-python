"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._hooks import SDKHooks
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from ascend_sdk.models import components
from ascend_sdk.types import OptionalNullable, UNSET
from dataclasses import dataclass
from pydantic import Field
from typing import Callable, Dict, Optional, Tuple, Union


SERVER_UAT = "uat"
r"""our uat environment"""
SERVER_PROD = "prod"
r"""our production environment"""
SERVER_SBX = "sbx"
r"""our sandbox environment"""
SERVERS = {
    SERVER_UAT: "https://uat.apexapis.com",
    SERVER_PROD: "https://api.apexapis.com",
    SERVER_SBX: "https://sbx.apexapis.com",
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: HttpClient
    async_client: AsyncHttpClient
    debug_logger: Logger
    security: Optional[
        Union[components.Security, Callable[[], components.Security]]
    ] = None
    server_url: Optional[str] = ""
    server: Optional[str] = ""
    language: str = "python"
    openapi_doc_version: str = "v1:20250714:uat:1c091aeaf0ad"
    sdk_version: str = "1.5.8"
    gen_version: str = "2.437.1"
    user_agent: str = (
        "speakeasy-sdk/python 1.5.8 2.437.1 v1:20250714:uat:1c091aeaf0ad ascend-sdk"
    )
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if not self.server:
            self.server = SERVER_UAT

        if self.server not in SERVERS:
            raise ValueError(f'Invalid server "{self.server}"')

        return SERVERS[self.server], {}

    def get_hooks(self) -> SDKHooks:
        return self._hooks
