from cv2 import imread, IMREAD_COLOR
from backend import transform_image
import tensorflow as tf

IMAGE_W = 440
IMAGE_H = 380

im = imread('/data/b.jpg', IMREAD_COLOR)

im = transform_image.crop(im)
im = transform_image.reshape(im, IMAGE_W, IMAGE_H)

model = tf.keras.models.load_model('../models/cnn-128x1-1591370377.727606.model')
# model = tf.keras.models.load_model('models/cnn-128x1-1591360990.327407.model')

predictions = model.predict([im])
print(predictions[0])
