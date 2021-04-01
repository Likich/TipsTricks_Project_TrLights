# Creating necessary dataloaders

trainDataset = TrafficLightsDataset(train_df, getTrainTransform())
valDataset = TrafficLightsDataset(val_df, getValTransform())
testDataset = TrafficLightsDataset(test_df, getTestTransform())

trainDataLoader = DataLoader(
    trainDataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=4,
    collate_fn=collate_fn
)

valDataLoader = DataLoader(
    valDataset,
    batch_size=BATCH_SIZE,
    shuffle=False,
    num_workers=4,
    collate_fn=collate_fn
)

testDataLoader = DataLoader(
    testDataset,
    batch_size=BATCH_SIZE,
    shuffle=False,
    num_workers=4,
    collate_fn=collate_fn
)
