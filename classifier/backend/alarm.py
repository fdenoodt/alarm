from datetime import datetime
from music_player import MusicPlayer
from camera import Camera
from model import Model
from config_manager import ConfigManager
from transform_image import prepare_for_prediction


class Alarm:
    def __init__(self):
        self.hour = None
        self.minute = None
        self.time_window_hours = ConfigManager.get_config()['hours_to_check']
        self.time_window_minutes = ConfigManager.get_config()['minutes_to_check']

        self.music_player = MusicPlayer()
        self.camera = Camera()
        self.model = Model()

        # for storing images
        self.counter = 0

    def set_alarm(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.stop_alarm()

    def verify_alarm(self):
        d = datetime.now()
        hour = int(d.hour)
        minute = int(d.minute)

        if self.in_time_window(hour, minute):
            is_present, image = self.verify_present()
            if is_present:
                self.launch_alarm()
            else:
                self.stop_alarm()

            self.store_image(image)

    def verify_present(self):
        image = Camera.capture_screenshot()
        predictable_image = prepare_for_prediction(image)
        prediction = self.model.predict(predictable_image)

        print("Predicted: {}".format(prediction))
        return prediction < 0.5, image

    def in_time_window(self, curr_hour, curr_minute):
        if self.hour is None or self.minute is None:
            return False

        if curr_hour is None or curr_minute is None:
            d = datetime.now()
            curr_hour = int(d.hour)
            curr_minute = int(d.minute)

        # Compare hour
        after_alarm = self.hour < curr_hour

        # CCompare minute if needed
        if not after_alarm:
            after_alarm = self.hour == curr_hour and \
                          self.minute <= curr_minute

        target_hour = self.hour + self.time_window_hours
        target_minute = self.minute + self.time_window_minutes

        # Compare hour
        before_wind_end = curr_hour < target_hour

        # Compare minute if needed
        if not before_wind_end:
            before_wind_end = curr_hour == target_hour and \
                              curr_minute <= target_minute

        return after_alarm and before_wind_end

    def launch_alarm(self):
        self.music_player.play()

    def stop_alarm(self):
        self.music_player.stop()

    def store_image(self, image):
        # activates once every 3 iterations
        self.counter = self.counter + 1
        if self.counter >= 2:
            self.counter = 0
            Camera.save_image(image)
