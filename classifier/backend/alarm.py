from datetime import datetime
from music_player import MusicPlayer
from camera import Camera
from model import Model
from config_manager import ConfigManager


class Alarm():
    def __init__(self):
        self.hour = None
        self.minute = None
        self.time_window_hours = 0
        self.time_window_minutes = ConfigManager.get_config()['minutes_to_check']

        self.music_player = MusicPlayer()
        self.camera = Camera()
        self.model = Model()

    def set_alarm(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def verify_alarm(self):
        d = datetime.now()
        hour = int(d.hour)
        minute = int(d.minute)

        if self.in_time_window(hour, minute):
            if self.verify_present():
                self.launch_alarm()
            else:
                self.stop_alarm()

    def verify_present(self):
        image = Camera.capture_screenshot()
        prediction = self.model.predict(image)

        print("Predicted: {}".format(prediction))
        return prediction == 0

    def in_time_window(self, curr_hour, curr_minute):
        if self.hour is None or self.minute is None:
            return False

        after_alarm = self.hour <= curr_hour and self.minute <= curr_minute
        before_wind_end = self.hour + self.time_window_hours >= curr_hour and \
                          self.minute + self.time_window_minutes >= curr_minute
        return after_alarm and before_wind_end

    def launch_alarm(self):
        self.music_player.play()

    def stop_alarm(self):
        self.music_player.stop()
