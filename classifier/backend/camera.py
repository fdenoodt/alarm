from config_manager import ConfigManager
import io
import numpy as np
import cv2
from transform_image import resize


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
            image = resize(image)

            Camera.camera.stop_preview()
        else:
            im_path = ConfigManager.get_config()['test_image_path']
            im = cv2.imread(im_path)
            image = resize(im)

        return image
