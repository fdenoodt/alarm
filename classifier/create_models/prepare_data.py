import os
from cv2 import imread, IMREAD_COLOR
from backend import transform_image
import random

DATA_DIR = '../data/'
LABELS = ['in', 'out']
# IMAGE_W = 440
# IMAGE_H = 380
# IMAGE_W = 640
# IMAGE_H = 480

IMAGE_W = 352
IMAGE_H = 352

training_data = []

# Load images
for label in LABELS:
    path = os.path.join(DATA_DIR, label)
    for im in os.listdir(path):
        im_arr = imread(os.path.join(path, im), IMREAD_COLOR)
        # im_arr = transform_image.crop(im_arr)
        im_arr = transform_image.resize(im_arr)
        training_data.append([im_arr, LABELS.index(label)])

##

# Spread data evenly
ins = list(filter(lambda x: x[1] == LABELS.index('in'), training_data))
outs = list(filter(lambda x: x[1] == LABELS.index('out'), training_data))
target_length = len(outs)
random.shuffle(ins)
ins = ins[:target_length]
training_data = outs
training_data.extend(ins)

random.shuffle(training_data)

##

xs = []
ys = []

for features, label in training_data:
    xs.append(features)
    ys.append(label)

xs = transform_image.reshape(xs, IMAGE_W, IMAGE_H)

##

# Save images
import pickle

pickle_out = open("../data/X3.pickle", "wb")
pickle.dump(xs, pickle_out)
pickle_out.close()

pickle_out = open("../data/Y3.pickle", "wb")
pickle.dump(ys, pickle_out)
pickle_out.close()

##
