import torch
import time
from tqdm.notebook import tqdm
import datetime


def model_training(EPOCHS):
    ''' Training the model for set number of epochs
        and computing the loss ussing lr scheduler, then saving the model'''
    for epoch in range(EPOCHS):

        start_time = time()
        model.train()
        lossHist.reset()

        for images, targets, image_ids in tqdm(trainDataLoader):

            images = torch.stack(images).to(device)
            targets = [{k: v.to(device) for k, v in t.items()}
                       for t in targets]

            bs = images.shape[0]

            loss_dict = model(images, targets)

            totalLoss = sum(loss for loss in loss_dict.values())
            lossValue = totalLoss.item()

            lossHist.update(lossValue, bs)

            optimizer.zero_grad()
            totalLoss.backward()
            optimizer.step()

        # Learning rate update
        if lr_scheduler is not None:
            lr_scheduler.step(totalLoss)

        print(f"[{str(datetime.timedelta(seconds = time() - start_time))[2:7]}]")
        print(f"Epoch {epoch}/{EPOCHS}")
        print(f"Train loss: {lossHist.avg}")

        torch.save(model.state_dict(), 'fasterrcnn_resnet50_fpn.pth')
