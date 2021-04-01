import cv2
import pandas as pd


def resize(dataset, location):
    '''This function reads images from the intial dataset, the changes each image to the new size
    and writes it to a new folder. Then to measure the new size of bounding boxes the scaling
    factor is computed and applied to coordinates. '''

    for i in range(len(dataset)):
        newSize = [1280, 960]
        img = cv2.imread(dataset['image_id'].iloc[i])
        img_new = cv2.resize(
            img, (newSize[0], newSize[1]), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(location+'{i}.jpg'.format(i=i), img_new)

        scale_x = newSize[0] / img.shape[1]
        scale_y = newSize[1] / img.shape[0]

        x_min = dataset['x_min'].iloc[i]
        y_min = dataset['y_min'].iloc[i]
        x_max = dataset['x_max'].iloc[i]
        y_max = dataset['y_max'].iloc[i]

        new_x_min = int(x_min * scale_x)
        new_y_min = int(y_min * scale_y)
        new_x_max = int(x_max * scale_x)
        new_y_max = int(y_max * scale_y)

        dataset['x_min'].iloc[i] = int(new_x_min)
        dataset['y_min'].iloc[i] = int(new_y_min)
        dataset['x_max'].iloc[i] = int(new_x_max)
        dataset['y_max'].iloc[i] = int(new_y_max)
