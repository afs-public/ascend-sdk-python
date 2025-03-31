import os
import time

from ascend_sdk.models import components


def test_fixed_income_pricing_orders_preview_order_cost_preview_order_cost1(
    create_sdk, enrolled_account_id, identifier_cusp
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    preview_order_cost_request = components.OrderCostPreviewRequestCreate(
        asset_type=components.AssetType.FIXED_INCOME,
        identifier=identifier_cusp,
        identifier_type=components.IdentifierType.CUSIP,
        parent="accounts/" + enrolled_account_id,
        quantity=components.DecimalCreate(value="5"),
        limit_price=components.LimitPriceCreate(
            price=components.DecimalCreate(value="2"),
            type=components.LimitPriceCreateType.PERCENTAGE_OF_PAR,
        ),
    )

    res = s.fixed_income_pricing.preview_order_cost(
        account_id=enrolled_account_id,
        order_cost_preview_request_create=preview_order_cost_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_fixed_income_pricing_orders_retrieve_quote_retrieve_quote1(
    create_sdk, enrolled_account_id, identifier_cusp
):
    s = create_sdk

    assert s is not None

    retrieve_quote_request_create = components.RetrieveQuoteRequestCreate(
        asset_type=components.AssetType.FIXED_INCOME,
        identifier=identifier_cusp,
        identifier_type=components.IdentifierType.CUSIP,
        parent="accounts/" + enrolled_account_id,
    )

    res = s.fixed_income_pricing.retrieve_quote(
        account_id=enrolled_account_id,
        retrieve_quote_request_create=retrieve_quote_request_create,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_fixed_income_pricing_orders_retrieve_fixed_income_marks(
    create_sdk, identifier_cusp
):
    s = create_sdk

    assert s is not None

    retrieve_fixed_income_marks_request_create = (
        components.RetrieveFixedIncomeMarksRequestCreate(
            parent="correspondents/" + os.getenv("CORRESPONDENT_ID"),
            security_identifiers=[
                components.RetrieveFixedIncomeMarksRequestSecurityIdentifiersCreate(
                    identifier=identifier_cusp,
                    identifier_type=components.IdentifierType.CUSIP,
                )
            ],
        )
    )

    res = s.fixed_income_pricing.retrieve_fixed_income_marks(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        retrieve_fixed_income_marks_request_create=retrieve_fixed_income_marks_request_create,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
