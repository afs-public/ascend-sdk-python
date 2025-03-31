import os

from ascend_sdk.models import components


def test_investor_docs_investor_docs_batch_create_upload_links_batch_create_upload_links1(
    create_sdk, create_account_id
):
    s = create_sdk

    assert s is not None

    request = components.BatchCreateUploadLinksRequestCreate(
        create_document_upload_link_request=[
            components.CreateUploadLinkRequestCreate(
                account_document_upload_request=components.AccountDocumentUploadRequestCreate(
                    correspondent_id=os.getenv("CORRESPONDENT_ID"),
                    document_type=components.DocumentType.FDIC_SWEEP_PROGRAM_AGREEMENT,
                    account_id=create_account_id,
                ),
                client_batch_source_id="cda89bd0-a6bc-4acc-89da-d35bde30cbf4",
                mime_type="image/jpeg",
            )
        ]
    )
    res = s.investor_docs.batch_create_upload_links(request=request)

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_investor_docs_investor_docs_list_documents_list_documents1(create_sdk):
    s = create_sdk

    assert s is not None

    res = s.investor_docs.list_documents(
        page_size=50, filter_=f'correspondent_id=="{os.getenv("CORRESPONDENT_ID")}"'
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
