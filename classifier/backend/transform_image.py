import matplotlib.pyplot as plt
import numpy as np
import cv2

IMAGE_W = IMAGE_H = 352


def show(image):
    plt.imshow(image)
    plt.show()


def resize(image):
    return cv2.resize(image, (IMAGE_W, IMAGE_H))


def reshape(images):
    xs = np.array(images).reshape(-1, IMAGE_W, IMAGE_H, 1)
    return xs


def prepare_for_prediction(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = resize(image)
    image = reshape(image)
    image = image / 255.0
    return image
