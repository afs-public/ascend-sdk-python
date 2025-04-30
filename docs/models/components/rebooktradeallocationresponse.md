# RebookTradeAllocationResponse

Rebooking a trade allocation will always return a new resource that contains the rebooked trade allocation.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `new_trade_allocation`                                                                                     | [OptionalNullable[components.NewTradeAllocation]](../../models/components/newtradeallocation.md)           | :heavy_minus_sign:                                                                                         | The new trade allocation that is booked.                                                                   |
| `original_trade_allocation`                                                                                | [OptionalNullable[components.OriginalTradeAllocation]](../../models/components/originaltradeallocation.md) | :heavy_minus_sign:                                                                                         | The original trade allocation that was rebooked.                                                           |