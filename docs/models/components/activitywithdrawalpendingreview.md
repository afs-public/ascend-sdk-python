# ActivityWithdrawalPendingReview

Used to record the movement of funds to/ from the pending_withdrawal memo location


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `review`                                                                         | [Optional[components.ActivityReview]](../../models/components/activityreview.md) | :heavy_minus_sign:                                                               | Denotes whether the withdrawal is pending or complete                            | REVIEW_STATE_PENDING                                                             |