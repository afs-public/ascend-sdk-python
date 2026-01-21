# ForceRejectPositionJournalRequestCreate

Request to force reject a pending position journal


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | The name of the position journal to force reject           | positionJournals/20230817000319                            |
| `reason`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | The optional reason for force rejecting a position journal | Forced rejection test                                      |