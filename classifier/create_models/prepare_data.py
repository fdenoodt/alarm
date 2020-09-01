import os
from PIL import Image
from backend import transform_image
import random
import imagehash
import pickle
import cv2
from backend.config_manager import ConfigManager as ConfManager

DATA_DIR = '../data/'
LABELS = ['in', 'out']

conf = ConfManager.get_config()['data']

IMAGE_W = conf['image_width']
IMAGE_H = conf['image_height']

image_data = []
image_data_count = 0

# Load images
for label in LABELS:
    path = os.path.join(DATA_DIR, label)
    for im in os.listdir(path):
        image_path = os.path.join(path, im)
        image = Image.open(image_path)  # Use of PIL for hashing later
        hash_code = imagehash.average_hash(image)

        image_data.append(
            [
                image_path,
                LABELS.index(label),
                hash_code
            ]
        )
        image_data_count = image_data_count + 1


##

def other_contain_hash(current_hash_code, current_index):
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


# Handle duplicates
index = 0
training_data = []  # image, label
for data in image_data:
    hash_code = data[2]

    # if remove duplicates = True -> check whether unique or not
    if not conf['remove_duplicates'] or not other_contain_hash(hash_code, index):
        label = data[1]
        cv_image = cv2.imread(data[0])
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        cv_image = transform_image.resize(cv_image)
        training_data.append([cv_image, label])

    index = index + 1

# Spread data evenly
if conf['spread_evenly']:
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
    xs.append(features)
    ys.append(label)


xs = transform_image.reshape(xs)

# Save images
pickle_out = open("../data/X{}.pickle".format(conf['version']), "wb")
pickle.dump(xs, pickle_out)
pickle_out.close()

pickle_out = open("../data/Y{}.pickle".format(conf['version']), "wb")
pickle.dump(ys, pickle_out)
pickle_out.close()
