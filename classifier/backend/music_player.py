import pygame


class MusicPlayer():
    def __init__(self):
        self.p = None
        self.is_playing = False

    def play(self):
        if not self.is_playing:
            print("Playing music...")
            pygame.init()
            pygame.mixer.music.load('audio/audio.mp3')
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        if self.is_playing:
            print("Stopping music...")
            pygame.mixer.music.stop()
            self.is_playing = False
