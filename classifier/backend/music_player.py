from sys import platform
from config_manager import ConfigManager


def is_linux():
    return platform == 'linux' or platform == 'linux2' or platform == 'darwin'


if is_linux():
    import pygame
else:
    import winsound


class MusicPlayer():
    p = None
    is_playing = False
    audio_file = ConfigManager.get_config()['audio_file']

    @staticmethod
    def play():
        if not MusicPlayer.is_playing:
            if is_linux():
                MusicPlayer.play_on_linux()
            else:
                MusicPlayer.play_on_windows()

            MusicPlayer.is_playing = True

    @staticmethod
    def stop():
        if MusicPlayer.is_playing:
            print("Stopping music...")
            if is_linux():
                MusicPlayer.stop_on_linux()
            MusicPlayer.is_playing = False

    @staticmethod
    def play_on_linux():
        print('Playing music linux...')

        pygame.init()
        pygame.mixer.music.load(MusicPlayer.audio_file)
        pygame.mixer.music.play(-1)  # -1 for continuous loop

    @staticmethod
    def play_on_windows():
        print('playing music windows...')
        winsound.PlaySound(MusicPlayer.audio_file, winsound.SND_ASYNC)

    @staticmethod
    def stop_on_linux():
        print('stopping music linux...')
        pygame.mixer.music.stop()

    @staticmethod
    def stop_on_windows():
        print('stopping music windows...')
        winsound.PlaySound(None, winsound.SND_PURGE)
