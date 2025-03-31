import os


def test_assets_assets_list_assets_by_correspondent1_assets_list_assets_by_correspondent1(
    create_sdk,
):
    s = create_sdk

    assert s is not None

    res = s.assets.list_assets_correspondent(
        correspondent_id=os.getenv("CORRESPONDENT_ID")
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_assets_assets_get_asset_by_correspondent_assets_get_asset_by_correspondent1(
    create_sdk, asset_id
):
    s = create_sdk

    assert s is not None

    res = s.assets.get_asset_correspondent(
        correspondent_id=os.getenv("CORRESPONDENT_ID"), asset_id=asset_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
