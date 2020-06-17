import tensorflow as tf
from transform_image import reshape


class Model():
    def __init__(self):
        # https://github.com/keras-team/keras/issues/5640
        self.session = tf.Session(graph=tf.Graph())
        with self.session.graph.as_default():
            tf.keras.backend.set_session(self.session)
            self.model = tf.keras.models.load_model('./model/model.model')

    '''
    0 = In bed, 1 = Out of bed
    '''

    def predict(self, image):
        image = reshape(image)

        with self.session.graph.as_default():
            tf.keras.backend.set_session(self.session)
            predictions = self.model.predict([image])
            return predictions[0][0]
