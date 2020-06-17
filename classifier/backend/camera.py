# from picamera import PiCamera
import io
import numpy as np
import cv2
from transform_image import resize


class Camera():
    def __init__(self):
        pass
        # self.camera = PiCamera()
        # self.camera.resolution = (650, 480)

    def capture_screenshot(self):
        im = cv2.imread('img.jpg')
        image = resize(im)
        # self.camera.start_preview()
        # 
        # stream = io.BytesIO()
        # self.camera.capture(stream, format='jpeg')
        # 
        # data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        # image = cv2.imdecode(data, cv2.IMREAD_COLOR)
        # image = resize(image)
        # 
        # self.camera.stop_preview()
        return image
