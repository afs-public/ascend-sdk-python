def test_pagination(
    create_sdk,
):
    """Test basic pagination"""
    s = create_sdk
    assert s is not None

    # Make the initial request to list assets (first page)
    res = s.assets.list_assets()

    # Verify the response structure is valid
    assert res.http_meta is not None, "HTTP metadata should be present in response"
    assert res.http_meta.response is not None, "HTTP response object should be present"
    assert res.http_meta.response.status_code == 200, (
        "Should receive successful HTTP 200 response"
    )
    assert res.list_assets_response is not None, (
        "Assets response data should be present"
    )

    # Test pagination by only checking the first few pages
    page_count = 0
    max_pages = 3  # Limit to the first 3 pages for testing to avoid long-running tests

    # Iterate through pages until we reach the limit or no more pages exist
    while res is not None and page_count < max_pages:
        print(f"Processing page {page_count + 1}")

        # Verify current page has valid response structure
        assert res.list_assets_response is not None, (
            f"Page {page_count + 1} should have valid assets response"
        )

        # Attempt to get the next page using the SDK's pagination method
        next_res = res.next()

        # If we successfully got the next page, verify it's also valid
        if next_res is not None:
            assert next_res.http_meta.response.status_code == 200, (
                f"Next page should also return HTTP 200"
            )

        # Move to the next page for the next iteration
        res = next_res
        page_count += 1

    print("Pagination test completed successfully.")


def test_empty_initial_response_handling(create_sdk):
    """Test that pagination handles empty initial responses gracefully"""
    s = create_sdk
    assert s is not None

    # Use a filter that should return no results to test empty response handling
    # This filter looks for assets with an impossible condition
    empty_filter = 'name == "NONEXISTENT_ASSET_12345_IMPOSSIBLE"'

    res = s.assets.list_assets(filter_=empty_filter)

    # Verify the response structure is still valid
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
    assert res.list_assets_response is not None

    # Verify that next() returns None for empty responses
    while res is not None:
        # Check if the current response has assets
        if res.list_assets_response.assets:
            assert False, "Expected no assets in response, but found some"

        # Attempt to get the next page
        res = res.next()

    print("Empty initial response handling test completed successfully.")


def test_pagination_with_symbol_filters(create_sdk):
    """Test pagination behavior with symbol filter"""
    s = create_sdk
    assert s is not None

    # Test filter by symbol
    equity_filter = 'symbol == "WTG"'
    res = s.assets.list_assets(filter_=equity_filter)

    assert res.http_meta.response.status_code == 200
    assert res.list_assets_response is not None

    # Count pages with an equity filter
    equity_pages = 0
    equity_assets = 0
    max_pages = 3

    while res is not None and equity_pages < max_pages:
        equity_pages += 1

        if res.list_assets_response.assets:
            current_count = len(res.list_assets_response.assets)
            equity_assets += current_count
            print(f"Symbol filter - Page {equity_pages}: {current_count} assets")

            # Verify all returned assets match the filter (if any)
            for asset in res.list_assets_response.assets:
                if hasattr(asset, "symbol") and asset.symbol is not None:
                    assert asset.symbol == "WTG", (
                        f"Symbol {asset.type} doesn't match filter"
                    )

        res = res.next()

    print(
        f"Filter test completed. Symbol assets found: {equity_assets} across {equity_pages} pages"
    )


def test_pagination_with_usable_filter(create_sdk):
    """Test pagination with usable filtering"""
    s = create_sdk
    assert s is not None

    # Test with a usable filter
    active_filter = "usable == true"
    res = s.assets.list_assets(filter_=active_filter)

    assert res.http_meta.response.status_code == 200
    assert res.list_assets_response is not None

    page_count = 0
    total_active_assets = 0
    max_pages = 3

    while res is not None and page_count < max_pages:
        page_count += 1

        if res.list_assets_response.assets:
            page_assets = len(res.list_assets_response.assets)
            total_active_assets += page_assets
            print(f"Usable filter - Page {page_count}: {page_assets} assets")

            # Verify all returned assets match the filter
            for asset in res.list_assets_response.assets:
                if hasattr(asset, "usable") and asset.usable is not None:
                    assert asset.usable is True, (
                        f"Asset usable status {asset.usable} doesn't match filter"
                    )

        res = res.next()

    print(
        f"Status filter test completed. Active assets: {total_active_assets} across {page_count} pages"
    )


def test_complex_filter_pagination(create_sdk):
    """Test pagination with complex filter expressions"""
    s = create_sdk
    assert s is not None

    # Test with a complex filter combining multiple conditions
    complex_filter = 'type == "EQUITY" && usable == true'
    res = s.assets.list_assets(filter_=complex_filter)

    assert res.http_meta.response.status_code == 200
    assert res.list_assets_response is not None

    page_count = 0
    matching_assets = 0
    max_pages = 3

    while res is not None and page_count < max_pages:
        page_count += 1

        if res.list_assets_response.assets:
            page_assets = len(res.list_assets_response.assets)
            matching_assets += page_assets
            print(f"Complex filter - Page {page_count}: {page_assets} assets")

            # Verify assets match both conditions
            for asset in res.list_assets_response.assets:
                if hasattr(asset, "type") and asset.type is not None:
                    assert asset.type == "EQUITY", (
                        f"Asset type {asset.type} doesn't match filter"
                    )
                if hasattr(asset, "usable") and asset.usable is not None:
                    assert asset.usable is True, (
                        f"Asset usable status {asset.usable} doesn't match filter"
                    )

        res = res.next()

    print(
        f"Complex filter test completed. Matching assets: {matching_assets} across {page_count} pages"
    )
