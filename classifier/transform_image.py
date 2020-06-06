import matplotlib.pyplot as plt
import numpy as np


def show(image):
    plt.imshow(image)
    plt.show()


def crop(image):
    w = 640
    h = 480
    im_arr = image[100:h, 200:w]  # w = 440, h = 380
    return im_arr


def reshape(images, image_w, image_h):
    xs = np.array(images).reshape(-1, image_w, image_h, 3)
    return xs
