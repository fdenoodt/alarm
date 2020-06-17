import cv2
import numpy as np
import tensorflow as tf
from set_interval import SetInterval
from time import sleep

IMAGE_W = IMAGE_H = 352


def resize(image):
    return cv2.resize(image, (IMAGE_W, IMAGE_H))


def reshape(images):
    xs = np.array(images).reshape(-1, IMAGE_W, IMAGE_H, 3)
    return xs


def predict():
    im = cv2.imread('img.jpg')
    image = resize(im)
    image = reshape(image)

    with session.graph.as_default():
        tf.keras.backend.set_session(session)
        predictions = model.predict([image])
        print(predictions[0][0])


session = tf.Session(graph=tf.Graph())
with session.graph.as_default():
    tf.keras.backend.set_session(session)
    model = tf.keras.models.load_model('./model/model.model')

sleep(10)

t = SetInterval(2, predict)
t.start()

sleep(10)
