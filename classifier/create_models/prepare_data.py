import os
from PIL import Image
from backend import transform_image
import random
import imagehash
import numpy as np

DATA_DIR = '../data/'
LABELS = ['in', 'out']

IMAGE_W = 352
IMAGE_H = 352

image_data = []
image_data_count = 0

# Load images
for label in LABELS:
    path = os.path.join(DATA_DIR, label)
    for im in os.listdir(path):
        image = Image.open(os.path.join(path, im))
        hash_code = imagehash.average_hash(image)
        image_data.append([image, LABELS.index(label), hash_code])
        image_data_count = image_data_count + 1


##

def otherContainHash(current_hash_code, current_index):
    contains = False

    for i in range(current_index - 5, current_index + 5):
        if i == index or i < 0 or i > (image_data_count - 1):
            continue

        other_hash = image_data[i][2]
        other_not_yet_tagged = len(image_data[i]) <= 3

        if other_hash == current_hash_code and other_not_yet_tagged:  # don't look at previous images again
            contains = True
            break

    return contains


index = 0
for data in image_data:
    hash_code = data[2]

    if otherContainHash(hash_code, index):
        data.append(False)
    else:  # these are unique
        data.append(True)

    index = index + 1

image_data = list(filter(lambda x: x[3] == True, image_data))  # only keep unique images
training_data = list(map(lambda x: [np.asarray(x[0]), x[1]], image_data))  # transform PIL Image to numpy array

# Spread data evenly
ins = list(filter(lambda x: x[1] == LABELS.index('in'), training_data))
outs = list(filter(lambda x: x[1] == LABELS.index('out'), training_data))

target_length = len(outs) if len(outs) < len(ins) else len(ins)

random.shuffle(ins)
random.shuffle(outs)

percent_data = 1  # 100%
ins = ins[:int(target_length * percent_data)]
outs = outs[:int(target_length * percent_data)]

training_data = outs
training_data.extend(ins)

random.shuffle(training_data)

##

xs = []
ys = []

for features, label in training_data:
    features = transform_image.resize(features)
    xs.append(features)
    ys.append(label)

xs = transform_image.reshape(xs)

##

import pickle

# Save images
pickle_out = open("../data/X8.pickle", "wb")
pickle.dump(xs, pickle_out)
pickle_out.close()

pickle_out = open("../data/Y8.pickle", "wb")
pickle.dump(ys, pickle_out)
pickle_out.close()

##
