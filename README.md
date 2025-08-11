# Introducing the Apex Python SDK

In today's fast-paced digital ecosystem, developers need tools that not only streamline the development process but also unlock new possibilities for innovation and efficiency.

Enter the Apex Python SDK, a cutting-edge software development kit designed to empower fintech app developers like never before.
With our SDK, you can more easily integrate new account creation, optimize trading, and elevate your applications with realtime buying power, all through a seamless, SDK interface.

Whether you're building complex, data-driven platforms or simplified, user-centric applications, Apex Python SDK was created to offer the flexibility, power, and ease of use to bring your visions to life faster and more effectively.
Join us in redefining the boundaries of what your applications can achieve.
Start your journey with Apex today.

## SDK Installation

PIP
```bash
pip install ascend-sdk
```

Poetry
```bash
poetry add ascend-sdk
```
<!-- No SDK Installation [installation] -->

## Supported Python Versions

- Python 3.9 or later

## Initializing the SDK

The following sample shows how to initialise the SDK, using the API Key and Service Account Credentials you received during sign-up:
```python
from ascend_sdk import SDK
from ascend_sdk.models import components

s = SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
)

# With an instance of the SDK, invoke any operation e.g.
resp = s.account_creation.get_account(account_id="VALID_ACCOUNT_ID")
```

<!-- No SDK Example Usage [usage] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKBaseError`](./src/ascend_sdk/models/errors/sdkbaseerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from ascend_sdk import SDK
from ascend_sdk.models import components, errors, operations


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:
    res = None
    try:

        res = sdk.account_creation.get_account(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", view=operations.QueryParamView.FULL)

        assert res.account is not None

        # Handle response
        print(res.account)


    except errors.SDKBaseError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.Status):
            print(e.data.code)  # Optional[int]
            print(e.data.details)  # Optional[List[components.AnyT]]
            print(e.data.message)  # Optional[str]
```

### Error Classes
**Primary errors:**
* [`SDKBaseError`](./src/ascend_sdk/models/errors/sdkbaseerror.py): The base class for HTTP error responses.
  * [`Status`](./src/ascend_sdk/models/errors/status.py): The status message serves as the general-purpose service error message. Each status message includes a gRPC error code, error message, and error details.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKBaseError`](./src/ascend_sdk/models/errors/sdkbaseerror.py)**:
* [`ResponseValidationError`](./src/ascend_sdk/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name   | Server                     | Description                |
| ------ | -------------------------- | -------------------------- |
| `uat`  | `https://uat.apexapis.com` | our uat environment        |
| `prod` | `https://api.apexapis.com` | our production environment |
| `sbx`  | `https://sbx.apexapis.com` | our sandbox environment    |

#### Example

```python
from ascend_sdk import SDK
from ascend_sdk.models import components, operations


with SDK(
    server="sbx",
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.account_creation.get_account(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", view=operations.QueryParamView.FULL)

    assert res.account is not None

    # Handle response
    print(res.account)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from ascend_sdk import SDK
from ascend_sdk.models import components, operations


with SDK(
    server_url="https://uat.apexapis.com",
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.account_creation.get_account(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", view=operations.QueryParamView.FULL)

    assert res.account is not None

    # Handle response
    print(res.account)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from ascend_sdk import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from ascend_sdk import SDK
from ascend_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- No Authentication [security] -->

<!-- No Summary [summary] -->

<!-- No Table of Contents [toc] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [account_creation](docs/sdks/accountcreation/README.md)

* [create_account](docs/sdks/accountcreation/README.md#create_account) - Create Account
* [get_account](docs/sdks/accountcreation/README.md#get_account) - Get Account

### [account_management](docs/sdks/accountmanagement/README.md)

* [list_accounts](docs/sdks/accountmanagement/README.md#list_accounts) - List Accounts
* [update_account](docs/sdks/accountmanagement/README.md#update_account) - Update Account
* [add_party](docs/sdks/accountmanagement/README.md#add_party) - Add Party
* [update_party](docs/sdks/accountmanagement/README.md#update_party) - Update Party
* [replace_party](docs/sdks/accountmanagement/README.md#replace_party) - Replace Party
* [remove_party](docs/sdks/accountmanagement/README.md#remove_party) - Remove Party
* [close_account](docs/sdks/accountmanagement/README.md#close_account) - Close Account
* [create_trusted_contact](docs/sdks/accountmanagement/README.md#create_trusted_contact) - Create Trusted Contact
* [update_trusted_contact](docs/sdks/accountmanagement/README.md#update_trusted_contact) - Update Trusted Contact
* [delete_trusted_contact](docs/sdks/accountmanagement/README.md#delete_trusted_contact) - Delete Trusted Contact
* [create_interested_party](docs/sdks/accountmanagement/README.md#create_interested_party) - Create Interested Party
* [update_interested_party](docs/sdks/accountmanagement/README.md#update_interested_party) - Update Interested Party
* [delete_interested_party](docs/sdks/accountmanagement/README.md#delete_interested_party) - Delete Interested Party
* [list_available_restrictions](docs/sdks/accountmanagement/README.md#list_available_restrictions) - List Available Restrictions
* [create_restriction](docs/sdks/accountmanagement/README.md#create_restriction) - Create Restriction
* [end_restriction](docs/sdks/accountmanagement/README.md#end_restriction) - End Restriction

### [account_transfers](docs/sdks/accounttransfers/README.md)

* [create_transfer](docs/sdks/accounttransfers/README.md#create_transfer) - Create Transfer
* [list_transfers](docs/sdks/accounttransfers/README.md#list_transfers) - List Transfers
* [accept_transfer](docs/sdks/accounttransfers/README.md#accept_transfer) - Accept Transfer
* [reject_transfer](docs/sdks/accounttransfers/README.md#reject_transfer) - Reject Transfer
* [get_transfer](docs/sdks/accounttransfers/README.md#get_transfer) - Get Transfer

### [ach_transfers](docs/sdks/achtransfers/README.md)

* [create_ach_deposit](docs/sdks/achtransfers/README.md#create_ach_deposit) - Create ACH Deposit
* [get_ach_deposit](docs/sdks/achtransfers/README.md#get_ach_deposit) - Get ACH Deposit
* [cancel_ach_deposit](docs/sdks/achtransfers/README.md#cancel_ach_deposit) - Cancel ACH Deposit
* [create_ach_withdrawal](docs/sdks/achtransfers/README.md#create_ach_withdrawal) - Create ACH Withdrawal
* [get_ach_withdrawal](docs/sdks/achtransfers/README.md#get_ach_withdrawal) - Get ACH Withdrawal
* [cancel_ach_withdrawal](docs/sdks/achtransfers/README.md#cancel_ach_withdrawal) - Cancel ACH Withdrawal

### [assets](docs/sdks/assets/README.md)

* [list_assets](docs/sdks/assets/README.md#list_assets) - List Assets
* [get_asset](docs/sdks/assets/README.md#get_asset) - Get Asset
* [list_assets_correspondent](docs/sdks/assets/README.md#list_assets_correspondent) - List Assets (By Correspondent)
* [get_asset_correspondent](docs/sdks/assets/README.md#get_asset_correspondent) - Get Asset (By Correspondent)

### [authentication](docs/sdks/authentication/README.md)

* [generate_service_account_token](docs/sdks/authentication/README.md#generate_service_account_token) - Generate Service Account Token
* [list_signing_keys](docs/sdks/authentication/README.md#list_signing_keys) - List Signing Keys

### [bank_relationships](docs/sdks/bankrelationships/README.md)

* [create_bank_relationship](docs/sdks/bankrelationships/README.md#create_bank_relationship) - Create Bank Relationship
* [list_bank_relationships](docs/sdks/bankrelationships/README.md#list_bank_relationships) - List Bank Relationships
* [get_bank_relationship](docs/sdks/bankrelationships/README.md#get_bank_relationship) - Get Bank Relationship
* [update_bank_relationship](docs/sdks/bankrelationships/README.md#update_bank_relationship) - Update Bank Relationship
* [cancel_bank_relationship](docs/sdks/bankrelationships/README.md#cancel_bank_relationship) - Cancel Bank Relationship
* [verify_micro_deposits](docs/sdks/bankrelationships/README.md#verify_micro_deposits) - Verify Micro Deposits
* [reissue_micro_deposits](docs/sdks/bankrelationships/README.md#reissue_micro_deposits) - Reissue Micro Deposits
* [reuse_bank_relationship](docs/sdks/bankrelationships/README.md#reuse_bank_relationship) - Reuse Bank Relationship

### [basket_orders](docs/sdks/basketorders/README.md)

* [create_basket](docs/sdks/basketorders/README.md#create_basket) - Create Basket
* [add_orders](docs/sdks/basketorders/README.md#add_orders) - Add Orders
* [get_basket](docs/sdks/basketorders/README.md#get_basket) - Get Basket
* [submit_basket](docs/sdks/basketorders/README.md#submit_basket) - Submit Basket
* [list_basket_orders](docs/sdks/basketorders/README.md#list_basket_orders) - List Basket Orders
* [list_compressed_orders](docs/sdks/basketorders/README.md#list_compressed_orders) - List Compressed Orders

### [cash_balances](docs/sdks/cashbalances/README.md)

* [calculate_cash_balance](docs/sdks/cashbalances/README.md#calculate_cash_balance) - Get Cash Balance

### [create_order](docs/sdks/createorder/README.md)

* [create_order](docs/sdks/createorder/README.md#create_order) - Create Order
* [get_order](docs/sdks/createorder/README.md#get_order) - Get Order
* [cancel_order](docs/sdks/createorder/README.md#cancel_order) - Cancel Order

### [data_retrieval](docs/sdks/dataretrieval/README.md)

* [list_snapshots](docs/sdks/dataretrieval/README.md#list_snapshots) - List Snapshots

### [enrollments_and_agreements](docs/sdks/enrollmentsandagreements/README.md)

* [enroll_account](docs/sdks/enrollmentsandagreements/README.md#enroll_account) - Enroll Account
* [list_available_enrollments](docs/sdks/enrollmentsandagreements/README.md#list_available_enrollments) - List Available Enrollments
* [accounts_list_available_enrollments_by_account_group](docs/sdks/enrollmentsandagreements/README.md#accounts_list_available_enrollments_by_account_group) - List Available Enrollments (by Account Group)
* [deactivate_enrollment](docs/sdks/enrollmentsandagreements/README.md#deactivate_enrollment) - Deactivate Enrollment
* [list_enrollments](docs/sdks/enrollmentsandagreements/README.md#list_enrollments) - List Account Enrollments
* [affirm_agreements](docs/sdks/enrollmentsandagreements/README.md#affirm_agreements) - Affirm Agreements
* [list_agreements](docs/sdks/enrollmentsandagreements/README.md#list_agreements) - List Account Agreements
* [list_entitlements](docs/sdks/enrollmentsandagreements/README.md#list_entitlements) - List Account Entitlements

### [fees_and_credits](docs/sdks/feesandcredits/README.md)

* [create_fee](docs/sdks/feesandcredits/README.md#create_fee) - Create Fee
* [get_fee](docs/sdks/feesandcredits/README.md#get_fee) - Get Fee
* [cancel_fee](docs/sdks/feesandcredits/README.md#cancel_fee) - Cancel Fee
* [create_credit](docs/sdks/feesandcredits/README.md#create_credit) - Create Credit
* [get_credit](docs/sdks/feesandcredits/README.md#get_credit) - Get Credit
* [cancel_credit](docs/sdks/feesandcredits/README.md#cancel_credit) - Cancel Credit

### [fixed_income_pricing](docs/sdks/fixedincomepricing/README.md)

* [preview_order_cost](docs/sdks/fixedincomepricing/README.md#preview_order_cost) - Preview Order Cost
* [retrieve_quote](docs/sdks/fixedincomepricing/README.md#retrieve_quote) - Retrieve Quote
* [retrieve_fixed_income_marks](docs/sdks/fixedincomepricing/README.md#retrieve_fixed_income_marks) - Retrieve Fixed Income Marks

### [instant_cash_transfer_ict](docs/sdks/instantcashtransferict/README.md)

* [create_ict_deposit](docs/sdks/instantcashtransferict/README.md#create_ict_deposit) - Create ICT Deposit
* [get_ict_deposit](docs/sdks/instantcashtransferict/README.md#get_ict_deposit) - Get ICT Deposit
* [cancel_ict_deposit](docs/sdks/instantcashtransferict/README.md#cancel_ict_deposit) - Cancel ICT Deposit
* [create_ict_withdrawal](docs/sdks/instantcashtransferict/README.md#create_ict_withdrawal) - Create ICT Withdrawal
* [get_ict_withdrawal](docs/sdks/instantcashtransferict/README.md#get_ict_withdrawal) - Get ICT Withdrawal
* [cancel_ict_withdrawal](docs/sdks/instantcashtransferict/README.md#cancel_ict_withdrawal) - Cancel ICT Withdrawal
* [locate_ict_report](docs/sdks/instantcashtransferict/README.md#locate_ict_report) - Locate ICT Report

### [investigations](docs/sdks/investigations/README.md)

* [get_investigation](docs/sdks/investigations/README.md#get_investigation) - Get Investigations
* [update_investigation](docs/sdks/investigations/README.md#update_investigation) - Update Investigation 
* [list_investigations](docs/sdks/investigations/README.md#list_investigations) - List Investigations
* [link_documents](docs/sdks/investigations/README.md#link_documents) - Link Documents
* [get_watchlist_item](docs/sdks/investigations/README.md#get_watchlist_item) - Get Watchlist Item
* [get_customer_identification](docs/sdks/investigations/README.md#get_customer_identification) - Get Identity Verification

### [investor_docs](docs/sdks/investordocs/README.md)

* [batch_create_upload_links](docs/sdks/investordocs/README.md#batch_create_upload_links) - Batch Create Upload Links
* [list_documents](docs/sdks/investordocs/README.md#list_documents) - List Documents

### [journals](docs/sdks/journals/README.md)

* [retrieve_cash_journal_constraints](docs/sdks/journals/README.md#retrieve_cash_journal_constraints) - Retrieve Cash Journal Constraints
* [create_cash_journal](docs/sdks/journals/README.md#create_cash_journal) - Create Cash Journal
* [get_cash_journal](docs/sdks/journals/README.md#get_cash_journal) - Get Cash Journal
* [cancel_cash_journal](docs/sdks/journals/README.md#cancel_cash_journal) - Cancel Cash Journal
* [check_party_type](docs/sdks/journals/README.md#check_party_type) - Retrieve Cash Journal Party

### [ledger](docs/sdks/ledger/README.md)

* [list_entries](docs/sdks/ledger/README.md#list_entries) - List Entries
* [list_activities](docs/sdks/ledger/README.md#list_activities) - List Activities
* [list_positions](docs/sdks/ledger/README.md#list_positions) - List Positions
* [get_activity](docs/sdks/ledger/README.md#get_activity) - Get Activity
* [get_entry](docs/sdks/ledger/README.md#get_entry) - Get Entry

### [margins](docs/sdks/margins/README.md)

* [get_buying_power](docs/sdks/margins/README.md#get_buying_power) - Get Buying Power

### [person_management](docs/sdks/personmanagement/README.md)

* [create_legal_natural_person](docs/sdks/personmanagement/README.md#create_legal_natural_person) - Create Legal Natural Person
* [list_legal_natural_persons](docs/sdks/personmanagement/README.md#list_legal_natural_persons) - List Legal Natural Persons
* [get_legal_natural_person](docs/sdks/personmanagement/README.md#get_legal_natural_person) - Get Legal Natural Persons
* [update_legal_natural_person](docs/sdks/personmanagement/README.md#update_legal_natural_person) - Update Legal Natural Person
* [assign_large_trader](docs/sdks/personmanagement/README.md#assign_large_trader) - Assign Large Trader
* [end_large_trader_legal_natural_person](docs/sdks/personmanagement/README.md#end_large_trader_legal_natural_person) - End Large Trader
* [create_legal_entity](docs/sdks/personmanagement/README.md#create_legal_entity) - Create Legal Entity
* [list_legal_entities](docs/sdks/personmanagement/README.md#list_legal_entities) - List Legal Entity
* [get_legal_entity](docs/sdks/personmanagement/README.md#get_legal_entity) - Get Legal Entity
* [update_legal_entity](docs/sdks/personmanagement/README.md#update_legal_entity) - Update Legal Entity
* [assign_large_trader_legal_entity](docs/sdks/personmanagement/README.md#assign_large_trader_legal_entity) - Assign Entity Large Trader
* [end_large_trader](docs/sdks/personmanagement/README.md#end_large_trader) - End Entity Large Trader

### [reader](docs/sdks/reader/README.md)

* [list_event_messages](docs/sdks/reader/README.md#list_event_messages) - List Event Messages
* [get_event_message](docs/sdks/reader/README.md#get_event_message) - Get Event Message

### [retirements](docs/sdks/retirements/README.md)

* [list_contribution_summaries](docs/sdks/retirements/README.md#list_contribution_summaries) - List Contribution Summaries
* [retrieve_contribution_constraints](docs/sdks/retirements/README.md#retrieve_contribution_constraints) - Retrieve Contribution Constraints
* [list_distribution_summaries](docs/sdks/retirements/README.md#list_distribution_summaries) - List Distribution Summaries
* [retrieve_distribution_constraints](docs/sdks/retirements/README.md#retrieve_distribution_constraints) - Retrieve Distribution Constraints

### [schedule_transfers](docs/sdks/scheduletransfers/README.md)

* [list_schedule_summaries](docs/sdks/scheduletransfers/README.md#list_schedule_summaries) - List Schedule Summaries
* [create_ach_deposit_schedule](docs/sdks/scheduletransfers/README.md#create_ach_deposit_schedule) - Create ACH Deposit Schedule
* [list_ach_deposit_schedules](docs/sdks/scheduletransfers/README.md#list_ach_deposit_schedules) - List ACH Deposit Schedules
* [get_ach_deposit_schedule](docs/sdks/scheduletransfers/README.md#get_ach_deposit_schedule) - Get ACH Deposit Schedule
* [update_ach_deposit_schedule](docs/sdks/scheduletransfers/README.md#update_ach_deposit_schedule) - Update ACH Deposit Schedules
* [cancel_ach_deposit_schedule](docs/sdks/scheduletransfers/README.md#cancel_ach_deposit_schedule) - Cancel ACH Deposit Schedule
* [create_ach_withdrawal_schedule](docs/sdks/scheduletransfers/README.md#create_ach_withdrawal_schedule) - Create ACH Withdrawal Schedule
* [list_ach_withdrawal_schedules](docs/sdks/scheduletransfers/README.md#list_ach_withdrawal_schedules) - List ACH Withdrawal Schedules
* [get_ach_withdrawal_schedule](docs/sdks/scheduletransfers/README.md#get_ach_withdrawal_schedule) - Get ACH Withdrawal Schedule
* [update_ach_withdrawal_schedule](docs/sdks/scheduletransfers/README.md#update_ach_withdrawal_schedule) - Update ACH Withdrawal Schedule
* [cancel_ach_withdrawal_schedule](docs/sdks/scheduletransfers/README.md#cancel_ach_withdrawal_schedule) - Cancel ACH Withdrawal Schedule
* [create_wire_withdrawal_schedule](docs/sdks/scheduletransfers/README.md#create_wire_withdrawal_schedule) - Create Wire Withdrawal Schedule
* [list_wire_withdrawal_schedules](docs/sdks/scheduletransfers/README.md#list_wire_withdrawal_schedules) - List Wire Withdrawal Schedules
* [get_wire_withdrawal_schedule](docs/sdks/scheduletransfers/README.md#get_wire_withdrawal_schedule) - Get Wire Withdrawal Schedule
* [update_wire_withdrawal_schedule](docs/sdks/scheduletransfers/README.md#update_wire_withdrawal_schedule) - Update Wire Withdrawal Schedule
* [cancel_wire_withdrawal_schedule](docs/sdks/scheduletransfers/README.md#cancel_wire_withdrawal_schedule) - Cancel Wire Withdrawal Schedule


### [subscriber](docs/sdks/subscriber/README.md)

* [create_push_subscription](docs/sdks/subscriber/README.md#create_push_subscription) - Create Push Subscription
* [list_push_subscriptions](docs/sdks/subscriber/README.md#list_push_subscriptions) - List Push Subscriptions
* [get_push_subscription](docs/sdks/subscriber/README.md#get_push_subscription) - Get Push Subscription
* [update_push_subscription](docs/sdks/subscriber/README.md#update_push_subscription) - Update Subscription
* [delete_push_subscription](docs/sdks/subscriber/README.md#delete_push_subscription) - Delete Subscription
* [get_push_subscription_delivery](docs/sdks/subscriber/README.md#get_push_subscription_delivery) - Get Subscription Event Delivery
* [list_push_subscription_deliveries](docs/sdks/subscriber/README.md#list_push_subscription_deliveries) - List Push Subscription Event Deliveries

### [test_simulation](docs/sdks/testsimulation/README.md)

* [force_approve_ach_deposit](docs/sdks/testsimulation/README.md#force_approve_ach_deposit) - ACH Deposit Approval
* [force_noc_ach_deposit](docs/sdks/testsimulation/README.md#force_noc_ach_deposit) - NOC for a Deposit
* [force_reject_ach_deposit](docs/sdks/testsimulation/README.md#force_reject_ach_deposit) - ACH Deposit Rejection
* [force_return_ach_deposit](docs/sdks/testsimulation/README.md#force_return_ach_deposit) - ACH Deposit Return
* [force_approve_ach_withdrawal](docs/sdks/testsimulation/README.md#force_approve_ach_withdrawal) - ACH Withdrawal Approval
* [force_noc_ach_withdrawal](docs/sdks/testsimulation/README.md#force_noc_ach_withdrawal) - ACH Withdrawal NOC
* [force_reject_ach_withdrawal](docs/sdks/testsimulation/README.md#force_reject_ach_withdrawal) - ACH Withdrawal Rejection
* [force_return_ach_withdrawal](docs/sdks/testsimulation/README.md#force_return_ach_withdrawal) - ACH Withdrawal Return
* [get_micro_deposit_amounts](docs/sdks/testsimulation/README.md#get_micro_deposit_amounts) - Get Relationship Micro Deposit Verification
* [force_approve_ict_deposit](docs/sdks/testsimulation/README.md#force_approve_ict_deposit) - Force Approve ICT Deposit
* [force_reject_ict_deposit](docs/sdks/testsimulation/README.md#force_reject_ict_deposit) - Force Reject ICT Deposit
* [force_approve_ict_withdrawal](docs/sdks/testsimulation/README.md#force_approve_ict_withdrawal) - Force Approve ICT Withdrawal
* [force_reject_ict_withdrawal](docs/sdks/testsimulation/README.md#force_reject_ict_withdrawal) - Force Reject ICT Withdrawal
* [force_approve_wire_withdrawal](docs/sdks/testsimulation/README.md#force_approve_wire_withdrawal) - Force Approve Wire Withdrawal
* [force_reject_wire_withdrawal](docs/sdks/testsimulation/README.md#force_reject_wire_withdrawal) - Force Reject Wire Withdrawal
* [force_approve_cash_journal](docs/sdks/testsimulation/README.md#force_approve_cash_journal) - Force Approve Cash Journal
* [force_reject_cash_journal](docs/sdks/testsimulation/README.md#force_reject_cash_journal) - Force Reject Cash Journal

### [trade_allocation](docs/sdks/tradeallocation/README.md)

* [create_trade_allocation](docs/sdks/tradeallocation/README.md#create_trade_allocation) - Create Trade Allocation
* [get_trade_allocation](docs/sdks/tradeallocation/README.md#get_trade_allocation) - Get Trade Allocation
* [cancel_trade_allocation](docs/sdks/tradeallocation/README.md#cancel_trade_allocation) - Cancel Trade Allocation
* [rebook_trade_allocation](docs/sdks/tradeallocation/README.md#rebook_trade_allocation) - Rebook Trade Allocation

### [trade_booking](docs/sdks/tradebooking/README.md)

* [create_trade](docs/sdks/tradebooking/README.md#create_trade) - Create Trade
* [get_trade](docs/sdks/tradebooking/README.md#get_trade) - Get Trade
* [complete_trade](docs/sdks/tradebooking/README.md#complete_trade) - Complete Trade
* [cancel_trade](docs/sdks/tradebooking/README.md#cancel_trade) - Cancel Trade
* [rebook_trade](docs/sdks/tradebooking/README.md#rebook_trade) - Rebook Trade
* [create_execution](docs/sdks/tradebooking/README.md#create_execution) - Create Execution
* [get_execution](docs/sdks/tradebooking/README.md#get_execution) - Get Execution
* [cancel_execution](docs/sdks/tradebooking/README.md#cancel_execution) - Cancel Execution
* [rebook_execution](docs/sdks/tradebooking/README.md#rebook_execution) - Rebook Execution

### [wires](docs/sdks/wires/README.md)

* [get_wire_deposit](docs/sdks/wires/README.md#get_wire_deposit) - Get Wire Deposit
* [create_wire_withdrawal](docs/sdks/wires/README.md#create_wire_withdrawal) - Create Wire Withdrawal
* [get_wire_withdrawal](docs/sdks/wires/README.md#get_wire_withdrawal) - Get Wire Withdrawal
* [cancel_wire_withdrawal](docs/sdks/wires/README.md#cancel_wire_withdrawal) - Cancel Wire Withdrawal

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from ascend_sdk import SDK
from ascend_sdk.models import operations
from ascend_sdk.utils import BackoffStrategy, RetryConfig


with SDK() as sdk:

    res = sdk.authentication.generate_service_account_token(security=operations.AuthenticationGenerateServiceAccountTokenSecurity(
        api_key_auth="<YOUR_API_KEY_HERE>",
    ), request={
        "jws": "eyJhbGciOiAiUlMyNTYifQ.eyJuYW1lIjogImpkb3VnaCIsIm9yZ2FuaXphdGlvbiI6ICJjb3JyZXNwb25kZW50cy8xMjM0NTY3OC0xMjM0LTEyMzQtMTIzNC0xMjM0NTY3ODkxMDEiLCJkYXRldGltZSI6ICIyMDI0LTAyLTA1VDIxOjAyOjI3LjkwMTE4MFoifQ.IMy3KmYoG8Ppf+7hXN7tm7J4MrNpQLGL7WCWvhh4nZWAVKkluL3/u3KC6hZ6Mb/5p7Y54CgZ68aWT2BcP5y4VtzIZR1Chm5pxbLfgE4aJuk+FnF6K3Gc3bBjOWCL58pxY2aTb0iU/exDEA1cbMDvbCzmY5kRefDvorLOqgUS/tS2MJ2jv4RlZFPlmHv5PtOruJ8xUW19gEgGhsPXYYeSHFTE1ZlaDvyXrKtpOvlf+FVc2RTuEw529LZnzwH4/eJJR3BpSpHyJTjQqiaMT3wzpXXYKfCRqnDkSSKJDzCzTb0/uWK/Lf0uafxPXk5YLdis+dbo1zNQhVVKjwnMpk1vLw",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.token is not None

    # Handle response
    print(res.token)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from ascend_sdk import SDK
from ascend_sdk.models import operations
from ascend_sdk.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as sdk:

    res = sdk.authentication.generate_service_account_token(security=operations.AuthenticationGenerateServiceAccountTokenSecurity(
        api_key_auth="<YOUR_API_KEY_HERE>",
    ), request={
        "jws": "eyJhbGciOiAiUlMyNTYifQ.eyJuYW1lIjogImpkb3VnaCIsIm9yZ2FuaXphdGlvbiI6ICJjb3JyZXNwb25kZW50cy8xMjM0NTY3OC0xMjM0LTEyMzQtMTIzNC0xMjM0NTY3ODkxMDEiLCJkYXRldGltZSI6ICIyMDI0LTAyLTA1VDIxOjAyOjI3LjkwMTE4MFoifQ.IMy3KmYoG8Ppf+7hXN7tm7J4MrNpQLGL7WCWvhh4nZWAVKkluL3/u3KC6hZ6Mb/5p7Y54CgZ68aWT2BcP5y4VtzIZR1Chm5pxbLfgE4aJuk+FnF6K3Gc3bBjOWCL58pxY2aTb0iU/exDEA1cbMDvbCzmY5kRefDvorLOqgUS/tS2MJ2jv4RlZFPlmHv5PtOruJ8xUW19gEgGhsPXYYeSHFTE1ZlaDvyXrKtpOvlf+FVc2RTuEw529LZnzwH4/eJJR3BpSpHyJTjQqiaMT3wzpXXYKfCRqnDkSSKJDzCzTb0/uWK/Lf0uafxPXk5YLdis+dbo1zNQhVVKjwnMpk1vLw",
    })

    assert res.token is not None

    # Handle response
    print(res.token)

```
<!-- End Retries [retries] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from ascend_sdk import SDK
def main():

    with SDK() as sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SDK() as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from ascend_sdk import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("ascend_sdk"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
