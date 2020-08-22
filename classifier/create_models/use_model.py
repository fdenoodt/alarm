from cv2 import imread, IMREAD_COLOR
from backend import transform_image
import tensorflow as tf

IMAGE_W = 440
IMAGE_H = 380

im = imread('../data/b.jpg', IMREAD_COLOR)

im = transform_image.resize(im)
im = transform_image.reshape(im)

model = tf.keras.models.load_model('../models/v8-128x1.model')

predictions = model.predict([im])
print('predicted value...')
print(predictions[0])
