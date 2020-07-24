import tensorflow as tf
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential
import pickle
from tensorflow.keras.callbacks import TensorBoard
from time import time
import os

session_conf = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
sess = tf.Session(config=session_conf)

X = pickle.load(open("../data/X4.pickle", "rb"))
Y = pickle.load(open("../data/Y4.pickle", "rb"))

MODEL_DIR = '../models/'
model_version = len(os.listdir(MODEL_DIR)) + 1

NAME = "v{}-128x1".format(model_version)

tensorBoard = TensorBoard(log_dir='.\\logs\\{}'.format(NAME))

X = X / 255.0
##

target_test_lines = int(len(X) * 10 / 100)  # 10%
x_test = X[:target_test_lines]
y_test = Y[:target_test_lines]

x_train = X[target_test_lines:]
y_train = Y[target_test_lines:]

##

model = Sequential()
model.add(Conv2D(128, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=['accuracy']
)

model.fit(x_train, y_train, batch_size=12, epochs=20, validation_split=0.2, callbacks=[tensorBoard])

val_loss, val_acc = model.evaluate(x_test, y_test)
print("\n", val_loss, val_acc)

model.save(MODEL_DIR + NAME + ".model")

# tensorboard --logdir=logs/
