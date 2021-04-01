import cv2
import matplotlib.pyplot as plt
import torch

# With the help of following links:
# https://colab.research.google.com/drive/1Zr5ozHnN9bKi6NepYVvboQ6v20i8ZO9X?usp=sharing
# https://medium.com/@fractaldle/guide-to-build-faster-rcnn-in-pytorch-95b10c273439

# model evaluation on the test set
model.eval()
images, targets, image_ids = next(iter(testDataLoader))
images = torch.stack(images).to(device)
outputs = model(images)


def filterBoxes(output, nms_th=0.3, score_threshold=0.5):
    ''' Function returns boxes, scores and labels
    for set classes'''

    boxes = output['boxes']
    scores = output['scores']
    labels = output['labels']

    # Non Max Supression
    mask = nms(boxes, scores, nms_th)

    boxes = boxes[mask]
    scores = scores[mask]
    labels = labels[mask]

    boxes = boxes.data.cpu().numpy().astype(np.int32)
    scores = scores.data.cpu().numpy()
    labels = labels.data.cpu().numpy()

    mask = scores >= score_threshold
    boxes = boxes[mask]
    scores = scores[mask]
    labels = labels[mask]

    return boxes, scores, labels


def displayPredictions(image_id, output, nms_th=0.3, score_threshold=0.5):
    ''' Displays predictions drawing bboxes, using the filterBoxes function'''

    boxes, scores, labels = filterBoxes(output, nms_th, score_threshold)

    # Preprocessing
    image = cv2.imread(image_id)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
    image = cv2.resize(image, (512, 512))
    image /= 255.0

    fig, ax = plt.subplots(1, 1, figsize=(16, 8))

    colors = {1: (0, 255, 0), 2: (255, 255, 0), 3: (255, 0, 0)}

    for box, label in zip(boxes, labels):
        image = cv2.rectangle(image,
                              (box[0], box[1]),
                              (box[2], box[3]),
                              colors[label], 2)

    ax.set_axis_off()
    ax.imshow(image)

    plt.show()

# Next function is the same but for video inference, returning the image instead of showing


def displayPredictions(image, output, nms_th=0.3, score_threshold=0.5):

    boxes, scores, labels = filterBoxes(output, nms_th, score_threshold)

    fig, ax = plt.subplots(1, 1, figsize=(16, 8))

    colors = {1: (0, 255, 0), 2: (255, 255, 0), 3: (255, 0, 0)}

    for box, label in zip(boxes, labels):
        image = cv2.rectangle(image,
                              (box[0], box[1]),
                              (box[2], box[3]),
                              colors[label], 2)

    return image


def preprocessImage(frame):
    '''Preprocess frames of the video '''

    frame = cv2.resize(frame, (512, 512))

    frame_ = frame.astype(np.float32)/255.0
    frame_ = torch.as_tensor([frame_]).to(device).permute(0, 3, 1, 2)

    return frame_, frame


def detectTrafficLight(frame, nms_th=0.2, score_th=0.5, model=model):
    '''Detecting the object in the frame of a video'''

    model.eval()

    frame_, frame = preprocessImage(frame)

    output = model(frame_)[0]

    pred = displayPredictions(frame, output, nms_th, score_th)

    return pred

# Stage of reading the video using cv2.videocapture


% % capture

result = cv2.VideoWriter(os.path.join(
    '/content/result-1.mp4'), cv2.VideoWriter_fourcc(*"FMP4"), 10, (512, 512), True)

cap = cv2.VideoCapture(os.path.join(
    '/content/unzipped/project.avi/project.avi'))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    pred = detectTrafficLight(frame, 0.2, 0.0)
    pred = pred.astype(np.uint8)
    pred = cv2.cvtColor(pred, cv2.COLOR_BGR2RGB)

    result.write(pred)

result.release()
cap.release()
