# ListPushSubscriptionsResponse

A response to a list push subscriptions method


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `next_page_token`                                                                       | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Page token used for pagination; Supplying a page token returns the next page of results | ZXhhbXBsZQo                                                                             |
| `push_subscriptions`                                                                    | List[[components.PushSubscription](../../models/components/pushsubscription.md)]        | :heavy_minus_sign:                                                                      | The returned collection of subscriptions                                                |                                                                                         |