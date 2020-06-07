from datetime import datetime
from music_player import MusicPlayer


class Alarm():
    def __init__(self):
        self.hour = None
        self.minute = None
        self.time_window_hours = 0
        self.time_window_minutes = 1  # seconds

        self.music_player = MusicPlayer()

    def set_alarm(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def verify_alarm(self):
        d = datetime.now()
        hour = int(d.hour)
        minute = int(d.minute)

        if self.in_time_window(hour, minute):
            # als op camera:
            self.launch_alarm()

            # als niet op camera:
            # stop alarm

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
