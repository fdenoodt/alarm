from config_manager import ConfigManager
import io
import numpy as np
import cv2
from transform_image import resize, reshape
import os
import datetime


class Camera:
    use_camera = ConfigManager.get_config()['use_camera'] == 'True'

    if use_camera:
        from picamera import PiCamera
        camera = PiCamera()
        camera.resolution = (650, 480)

    @staticmethod
    def capture_screenshot():
        if Camera.use_camera:
            Camera.camera.start_preview()

            stream = io.BytesIO()
            Camera.camera.capture(stream, format='jpeg')

            data = np.fromstring(stream.getvalue(), dtype=np.uint8)
            image = cv2.imdecode(data, cv2.IMREAD_COLOR)

            Camera.camera.stop_preview()
        else:
            im_path = ConfigManager.get_config()['test_image_path']
            image = cv2.imread(im_path)

        return image

    @staticmethod
    def save_image(image, reason='automatic'):
        save_path = ConfigManager.get_config()['save_image_path']
        if reason == ('automatic' and not ConfigManager.get_config()['automatic_save']) or len(save_path) == 0:
            return

        skip = ConfigManager.get_config()['skip_image_count']
        count = len(os.listdir(save_path)) + skip

        now = datetime.datetime.now()
        file_name = '{}_{}_{}_{}_{}_{}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)

        file_path_name = '{}image{}_{}.jpg'.format(save_path, count, file_name)
        cv2.imwrite(file_path_name, image)
