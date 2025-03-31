def test_reader_events_list_event_messages_list_event_messages1(message_id):
    assert message_id is not None


def test_reader_events_get_event_message_get_event_message1(create_sdk, message_id):
    s = create_sdk

    assert s is not None

    res = s.reader.get_event_message(message_id=message_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
